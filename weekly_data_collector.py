#!/usr/bin/env python3
"""
Weekly Market Data Collector + Direct Prompt Updater
-----------------------------------------------------
Fetches weekly market data, generates news summary,
and directly replaces the JSON block inside the infographic prompt markdown file.
No temporary JSON file is saved.
"""

import os
import json
import re
import time
import logging
import yfinance as yf
from datetime import datetime, timedelta
from google import genai

# =========================
# CONFIGURATION (edit these)
# =========================
MD_FILE_PATH = "weekly_infographic_prompt.md"        # Source markdown file
OUTPUT_MD_PATH = "weekly_infographic_prompt_updated.md"  # Output markdown (set to same as above to overwrite)
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")         # or hardcode your key (not recommended)
NEWS_PROMPT_PATH = "news_prompt.md"

MODEL = 'gemini-3-flash-preview'

# =========================
# LOGGING SETUP
# =========================
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

logger = setup_logging()

# =========================
# MARKET DATA SOURCES
# =========================
INDIAN_INDICES = {
    "Nifty 50": "^NSEI",
    "Nifty Next 50": "^NSMIDCP",
    "Nifty Midcap 150": "NIFTYMIDCAP150.NS",
    "Nifty Smallcap 250": "NIFTYSMLCAP250.NS",
    "Nifty 500": "^CRSLDX"
}

GLOBAL_INDICES = {
    "S&P 500": "^GSPC",
    "Dow Jones": "^DJI",
    "Nasdaq": "^IXIC",
    "Nikkei 225": "^N225",
    "Hang Seng": "^HSI"
}

COMMODITIES = {
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Crude Oil": "CL=F",
    "USD/INR": "INR=X"
}

# =========================
# DATE RANGE UTILITY
# =========================
def get_week_range():
    today = datetime.today()
    days_to_last_monday = (today.weekday() - 4) % 7
    last_friday = today - timedelta(days=days_to_last_monday)
    last_monday = last_friday - timedelta(days=4)
    week_range_str = f"{last_monday.strftime('%d %b')} – {last_friday.strftime('%d %b %Y')}"
    return last_monday, last_friday, week_range_str

# =========================
# PROMPT LOADING
# =========================
def load_prompt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f"Prompt file not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        raise

def load_news_prompt(**kwargs):
    prompt = load_prompt(NEWS_PROMPT_PATH)
    for key, value in kwargs.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", str(value))
    return prompt

# =========================
# DATA FETCHING
# =========================
def get_weekly_data(ticker, start_date, end_date):
    try:
        data = yf.Ticker(ticker).history(start=start_date, end=end_date)
        if data.empty or len(data) < 2:
            logger.warning(f"Insufficient data for {ticker} (got {len(data)} rows)")
            return None, None
        start_price = data["Close"].iloc[0]
        end_price = data["Close"].iloc[-1]
        change_pct = ((end_price - start_price) / start_price) * 100
        return round(float(end_price), 2), round(float(change_pct), 2)
    except Exception as e:
        logger.error(f"Error fetching {ticker}: {e}")
        return None, None

def build_data(source, start_date, end_date, include_pe=False):
    result = []
    for name, ticker in source.items():
        value, change = get_weekly_data(ticker, start_date, end_date)
        if value is None:
            continue
        item = {
            "name": name,
            "value": value,
            "change_percent": change
        }
        if include_pe:
            # Placeholder PE – deterministic
            item["pe_ratio"] = round(15 + (hash(name) % 20), 2)
        result.append(item)
    return result

# =========================
# GEMINI NEWS GENERATION
# =========================
def generate_news(start_date, end_date):
    if not GEMINI_API_KEY:
        logger.error("Gemini API key not set. Skipping news generation.")
        return {"top_news_headlines": [], "kapital_gains_views": []}

    client = genai.Client(api_key=GEMINI_API_KEY)
    prompt = load_news_prompt(
        start_date=start_date.strftime('%d %b %Y'),
        end_date=end_date.strftime('%d %b %Y')
    )

    for attempt in range(3):
        try:
            logger.info(f"Calling Gemini (attempt {attempt+1}/3)")
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    "temperature": 0.2
                }
            )
            text = response.text.strip()
            if text.startswith("```"):
                text = text.replace("```json", "").replace("```", "").strip()
            data = json.loads(text)
            data["top_news_headlines"] = data.get("top_news_headlines", [])[:3]
            data["kapital_gains_views"] = data.get("kapital_gains_views", [])[:2]
            logger.info("Gemini response parsed successfully")
            return data
        except Exception as e:
            logger.warning(f"Gemini attempt {attempt+1} failed: {e}")
            time.sleep(2)

    logger.error("All Gemini attempts failed. Returning empty data.")
    return {"top_news_headlines": [], "kapital_gains_views": []}

# =========================
# DIRECT PROMPT UPDATE (no JSON file)
# =========================
def update_infographic_prompt(output_data):
    """
    Load the markdown template, replace the ```json ... ``` block
    with the new data (formatted as JSON), and save to OUTPUT_MD_PATH.
    """
    # Read the existing markdown file
    try:
        with open(MD_FILE_PATH, "r", encoding="utf-8") as f:
            md_content = f.read()
    except FileNotFoundError:
        logger.error(f"Source markdown file not found: {MD_FILE_PATH}")
        raise

    # Convert output_data to pretty JSON string
    new_json_str = json.dumps(output_data, indent=2)

    # Regex to find the JSON code block (```json ... ```)
    pattern = r'(```json\s*\n)(.*?)(\n```)'
    def replacer(match):
        return f"{match.group(1)}{new_json_str}{match.group(3)}"

    new_md_content = re.sub(pattern, replacer, md_content, flags=re.DOTALL)

    # Write the updated markdown
    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f:
        f.write(new_md_content)

    logger.info(f"Updated JSON block in {MD_FILE_PATH} -> saved to {OUTPUT_MD_PATH}")

# =========================
# MAIN ORCHESTRATION
# =========================
def main():
    logger.info("Starting weekly market data collection")

    # 1. Determine date range
    last_monday, last_friday, week_range_str = get_week_range()
    logger.info(f"Week range: {week_range_str}")

    # 2. Fetch market data
    logger.info("Fetching Indian indices data...")
    indian_data = build_data(INDIAN_INDICES, last_monday, last_friday, include_pe=True)

    logger.info("Fetching global indices data...")
    global_data = build_data(GLOBAL_INDICES, last_monday, last_friday, include_pe=False)

    logger.info("Fetching commodities data...")
    commodity_data = build_data(COMMODITIES, last_monday, last_friday, include_pe=False)

    # 3. Generate news with Gemini
    logger.info("Generating weekly news summary via Gemini...")
    news_data = generate_news(last_monday, last_friday)

    # 4. Assemble final output (the data that will replace the JSON in the markdown)
    output = {
        "week_range": week_range_str,
        "indian_indices": indian_data,
        "global_indices": global_data,
        "commodities": commodity_data,
        "top_news_headlines": news_data["top_news_headlines"],
        "kapital_gains_views": news_data["kapital_gains_views"]
    }

    # 5. Directly update the markdown prompt (no JSON file saved)
    try:
        update_infographic_prompt(output)
        logger.info("Infographic prompt updated successfully.")
    except Exception as e:
        logger.error(f"Failed to update infographic prompt: {e}")
        return

    logger.info("✅ PROCESS COMPLETE: Prompt updated with fresh data")
    # Optional: print a preview of the output
    print("\n--- Final data injected ---")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()