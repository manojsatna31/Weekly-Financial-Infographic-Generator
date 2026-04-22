import os
import yfinance as yf
import json
import yaml
from datetime import datetime, timedelta

# =========================
# STEP 1: DATE RANGE
# =========================
today = datetime.today()

last_friday = today - timedelta(days=(today.weekday() - 4) % 7)
last_monday = last_friday - timedelta(days=4)

week_range = f"{last_monday.strftime('%d %b')} – {last_friday.strftime('%d %b %Y')}"
# =========================
# STEP 2: FETCH DATA
# =========================
def get_weekly_data(ticker):
    try:
        data = yf.Ticker(ticker).history(start=last_monday, end=last_friday)

        if data.empty or len(data) < 2:
            return None, None

        start = data["Close"].iloc[0]
        end = data["Close"].iloc[-1]

        change = ((end - start) / start) * 100

        # return round(end, 2), round(change, 2)
        return float(round(end, 2)), float(round(change, 2))

    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        return None, None


# =========================
# STEP 3: MARKET CONFIG
# =========================
indian_indices = {
    "Nifty 50": "^NSEI",
    "Nifty Bank": "^NSEBANK",
    "Nifty IT": "^CNXIT",
    "Nifty Auto": "^CNXAUTO",
    "Nifty FMCG": "^CNXFMCG"
}

global_indices = {
    "S&P 500": "^GSPC",
    "Dow Jones": "^DJI",
    "Nasdaq": "^IXIC",
    "Nikkei 225": "^N225",
    "Hang Seng": "^HSI"
}

commodities = {
    "Gold": "GC=F",
    "Silver": "SI=F",
    "Crude Oil": "CL=F",
    "USD/INR": "INR=X"
}

# =========================
# STEP 4: BUILD DATA
# =========================

def build_data(source, include_pe=False):
    result = []

    for name, ticker in source.items():
        value, change = get_weekly_data(ticker)

        if value is None:
            continue

        item = {
            "name": str(name),
            "value": float(value),
            "change_percent": float(change)
        }

        if include_pe:
            item["pe_ratio"] = float(round(15 + (hash(name) % 20), 2))

        result.append(item)

    return result

indian_data = build_data(indian_indices, include_pe=True)
global_data = build_data(global_indices)
commodity_data = build_data(commodities)

json_file = "weekly_market_data.json"

existing_data = {}

if os.path.exists(json_file):
    try:
        with open(json_file, "r") as f:
            existing_data = json.load(f)
    except:
        existing_data = {}



# =========================
# STEP 5: FINAL STRUCTURE
# =========================
output = {
    # AUTO UPDATED
    "week_range": week_range,
    "indian_indices": indian_data,
    "global_indices": global_data,
    "commodities": commodity_data,

    # PRESERVE MANUAL INPUT
    "top_news_headlines": existing_data.get("top_news_headlines", []),
    "kapital_gains_views": existing_data.get("kapital_gains_views", [])
}

# =========================
# STEP 6: SAVE JSON
# =========================

with open(json_file, "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ JSON saved to {json_file}")


# =========================
# STEP 8: PRETTY PRINT
# =========================
print("\n--- JSON OUTPUT ---\n")
print(json.dumps(output, indent=2))

# =========================
# STEP 9: UPDATE PROMPT FILE
# =========================

prompt_file = "weekly_infographic_prompt.md"

START_MARKER = "```json"
END_MARKER = "```"

try:
    with open(prompt_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Convert JSON safely (no unicode escaping)
    json_block = json.dumps(output, indent=2, ensure_ascii=False)

    start_index = content.find(START_MARKER)
    end_index = content.find(END_MARKER, start_index + len(START_MARKER))

    if start_index == -1 or end_index == -1:
        raise ValueError("JSON block markers not found in prompt file")

    # Build new content
    new_content = (
        content[:start_index + len(START_MARKER)]
        + "\n"
        + json_block
        + "\n"
        + content[end_index:]
    )

    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ Prompt file updated successfully (no regex issues)")

except Exception as e:
    print(f"❌ Error updating prompt file: {e}")