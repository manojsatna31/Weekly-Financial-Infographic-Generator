# 📊 Weekly Financial Infographic Generator

A fully automated system to generate **professional weekly market infographics** using:

* 📈 Real financial data (Python)
* 📰 Manual curated insights
* 🎨 AI-powered image generation (Banana-2)

---

# 🚀 Project Overview

This project generates a **Weekly Market Snapshot Infographic** with:

✅ Indian Indices
✅ Global Indices
✅ Commodities & FX
✅ Top News Headlines (manual)
✅ Kapital-Gains Views (manual)

👉 Output: **Consistent, high-quality infographic image (weekly)**

---

# 🧩 Architecture

```
[Python Script]
      ↓
[JSON Data]
      ↓
[Auto Inject into Prompt]
      ↓
[Banana-2 Image Generation]
```

---

# 📂 Project Structure

```
Weekly-Financial-Infographic-Generator/
│
├── weekly_data_collector.py      # Data pipeline (auto + preserve manual)
├── weekly_market_data.json       # Main editable data
├── weekly_infographic_prompt.md  # Banana-2 prompt (auto-updated)
├── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd Weekly-Financial-Infographic-Generator
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Weekly Execution Flow

---

## 🔹 STEP 1 — Run Data Collector

```bash
python weekly_data_collector.py
```

### ✅ What it does:

✔ Fetches latest market data
✔ Updates:

* `week_range`
* `indian_indices`
* `global_indices`
* `commodities`

✔ Preserves:

* `top_news_headlines`
* `kapital_gains_views`

✔ Generates:

* `weekly_market_data.json`
* `weekly_market_data.yml`

✔ **NEW:** Automatically injects JSON into prompt file

---

## 🔹 STEP 2 — Update Manual Sections (ONLY FIRST TIME / WEEKLY)

Open:

```
weekly_market_data.json
```

Update:

```json
{
  "top_news_headlines": [
    "Headline 1",
    "Headline 2",
    "Headline 3",
    "Headline 4"
  ],
  "kapital_gains_views": [
    "View point 1",
    "View point 2"
  ]
}
```

---

### 🔴 Rules

| Field           | Limit      |
| --------------- | ---------- |
| Headlines       | Max 4      |
| Headline length | ≤ 60 chars |
| Views           | Max 2      |
| View length     | ≤ 80 chars |

---

## 🔹 STEP 3 — Generate Infographic

1. Open:

```
weekly_infographic_prompt.md
```

2. Copy full content

3. Paste into Banana-2

4. Generate image ✅

---

# 🔥 NEW FEATURE — AUTO PROMPT UPDATE

The system now automatically updates this section:

````markdown
```json
<auto-injected latest data>
````

```

---

## ✅ How It Works

- Script reads existing prompt file
- Finds JSON block using markers:
```

```json
## Replace Me
```

```
- Replaces ONLY that block
- Preserves full prompt design

---

## 🚨 Important Rules

✔ Only ONE JSON block allowed  
✔ Do NOT modify prompt structure  
✔ Keep markers intact  

---

# 📊 Data Sources

- Market Data → Yahoo Finance (via `yfinance`)
- Headlines → Manual input
- Views → Manual input

---

# ⚠️ Known Issues & Fixes

---

## ❌ YAML shows `!!python/object`

### Fix:
Handled in script (converted to float)

---

## ❌ Regex / `\u` Error (FIXED)

Old issue:
```

bad escape \u

````

### ✅ Fix applied:
- Removed regex
- Implemented marker-based replacement
- Used:
```python
json.dumps(..., ensure_ascii=False)
````

---

## ❌ Missing Index Data

Some tickers may fail:

* Nifty Smallcap
* Custom indices

👉 Use fallback or replace symbol

---

# 🔧 Customization

---

## Add / Remove Indices

Edit in:

```text
weekly_data_collector.py
```

---

## Modify Design

Edit:

```
weekly_infographic_prompt.md
```

(Change colors, layout, fonts)

---

# 💡 Best Practices

* ✅ Always edit JSON (not YAML)
* ✅ Keep prompt unchanged
* ✅ Validate data before rendering
* ❌ Do not edit injected JSON manually

---

# 🚀 Future Enhancements

* 🔄 Auto news fetching
* 🤖 AI-generated market insights
* 🖼 Direct image generation (no manual copy)
* 🌐 Web UI
* 📱 LinkedIn carousel export

---

# 🏁 Final Workflow (1-Min Process)

1. Run script
2. Update headlines (optional)
3. Copy prompt
4. Generate image

---

# 👨‍💻 Author

Manoj Mishra

---

# 📜 License

MIT License
