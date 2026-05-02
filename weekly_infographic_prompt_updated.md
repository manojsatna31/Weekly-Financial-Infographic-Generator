# 📊 WEEKLY MARKET SNAPSHOT — EXACT REPLICATION PROMPT

You are a **UI rendering engine**.

Your task is to **replicate the reference infographic EXACTLY**.

❌ No creativity
❌ No redesign
❌ No layout change

Only replace data.

---

# 🔴 INPUT DATA

```json
{
  "week_range": "27 Apr \u2013 01 May 2026",
  "indian_indices": [
    {
      "name": "Nifty 50",
      "value": 23997.55,
      "change_percent": -0.39,
      "pe_ratio": 27
    },
    {
      "name": "Nifty Next 50",
      "value": 69643.9,
      "change_percent": -1.63,
      "pe_ratio": 25
    },
    {
      "name": "Nifty Midcap 150",
      "value": 22000.05,
      "change_percent": -0.89,
      "pe_ratio": 28
    },
    {
      "name": "Nifty 500",
      "value": 22683.55,
      "change_percent": -0.6,
      "pe_ratio": 34
    }
  ],
  "global_indices": [
    {
      "name": "S&P 500",
      "value": 7209.01,
      "change_percent": 0.49
    },
    {
      "name": "Dow Jones",
      "value": 49652.14,
      "change_percent": 0.99
    },
    {
      "name": "Nasdaq",
      "value": 24892.31,
      "change_percent": 0.02
    },
    {
      "name": "Nikkei 225",
      "value": 59284.92,
      "change_percent": -2.07
    },
    {
      "name": "Hang Seng",
      "value": 25776.53,
      "change_percent": -0.58
    }
  ],
  "commodities": [
    {
      "name": "Gold",
      "value": 4625.6,
      "change_percent": -1.07
    },
    {
      "name": "Silver",
      "value": 75.84,
      "change_percent": 1.12
    },
    {
      "name": "Crude Oil",
      "value": 102.5,
      "change_percent": 6.36
    },
    {
      "name": "USD/INR",
      "value": 94.76,
      "change_percent": 0.54
    }
  ],
  "top_news_headlines": [
    "Nifty 50 hits record high on strong corporate earnings.",
    "RBI maintains interest rates to balance growth.",
    "Tech stocks surge as AI integration drives profits."
  ],
  "kapital_gains_views": [
    "Strong corporate earnings signal a bullish trend for mid-cap stocks.",
    "Focus on long-term growth in the renewable energy sector."
  ]
}
```

---

# 🔴 DATA RULES

* Use ONLY provided data
* Do NOT generate headlines
* Do NOT generate views
* Use text EXACTLY as given

---

# 🔴 CANVAS

* Aspect Ratio: 16:9
* Background: Light grey
* Center white card

---

# 🔴 HEADER (TOP BAR)

* Full width dark blue bar
* Left: Logo placeholder + "KAPITAL-GAINS"
* Center:

  * Small text: "KAPITAL-GAINS PRESENTS..."
  * Title: "WEEKLY MARKET SNAPSHOT" (ALL CAPS, BOLD)
  * Subtitle: week_range

---

# 🔴 LEFT PANEL (TABLES)

## 🟢 Indian Indices

Table columns:
INDEX | VALUE | CHANGE | CURR. P/E

* Header row dark blue
* White rows
* Thin borders
* ▲ green for positive
* ▼ red for negative

---

## 🌍 Global Indices

Columns:
INDEX | VALUE | CHANGE %

---

## 📦 Commodities & FX

Columns:
ASSET | VALUE | CHANGE %

---

# 🔴 RIGHT PANEL

## 📰 Top News Headlines

* Dark blue box
* White text
* Title: "Top News Headlines"

Render:

* Each headline as **separate line block**
* No bullets
* Equal spacing
* Keep EXACT wording

---

## 💡 Kapital-Gains Views

* Dark blue box
* Title: "Kapital-Gains Views"
* Small avatar icon on left

Render:

* Combine both points into paragraph style
* Keep tone clean
* No extra words

---

# 🔴 FOOTER

Full-width dark blue strip:

Text:
"DISCLAIMER - Not investment advice | Numbers compiled from multiple sources; errors may occur"

---

# 🔴 COLORS (LOCKED)

* Dark Blue: #2f5d73
* Green: #2ecc71
* Red: #e74c3c
* White + light grey background

---

# 🔴 ALIGNMENT

* Left panel: 60%
* Right panel: 40%
* Perfect grid alignment

---

# 🔴 OUTPUT RULES

* Output ONLY image
* No text
* No explanation
* No deviation from layout

---

# 🔴 FINAL COMMAND

Render infographic EXACTLY like reference image.

Only replace data.
