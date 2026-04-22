# 📊 WEEKLY MARKET SNAPSHOT — EXACT REPLICATION PROMPT

You are a **UI rendering engine**.

Your task is to **replicate the reference infographic EXACTLY**.

❌ No creativity
❌ No redesign
❌ No layout change

Only replace data.

---

# 🔴 INPUT DATA

Paste JSON below:

```json
{
  "week_range": "13 Apr – 17 Apr 2026",
  "indian_indices": [
    {
      "name": "Nifty 50",
      "value": 24196.75,
      "change_percent": 1.49,
      "pe_ratio": 18.0
    },
    {
      "name": "Nifty Bank",
      "value": 56086.4,
      "change_percent": 0.87,
      "pe_ratio": 30.0
    },
    {
      "name": "Nifty IT",
      "value": 31817.5,
      "change_percent": 3.74,
      "pe_ratio": 29.0
    },
    {
      "name": "Nifty Auto",
      "value": 26382.75,
      "change_percent": 1.14,
      "pe_ratio": 22.0
    },
    {
      "name": "Nifty FMCG",
      "value": 48377.9,
      "change_percent": 1.7,
      "pe_ratio": 28.0
    }
  ],
  "global_indices": [
    {
      "name": "S&P 500",
      "value": 7041.28,
      "change_percent": 2.25
    },
    {
      "name": "Dow Jones",
      "value": 48578.72,
      "change_percent": 0.75
    },
    {
      "name": "Nasdaq",
      "value": 24102.7,
      "change_percent": 3.96
    },
    {
      "name": "Nikkei 225",
      "value": 59518.34,
      "change_percent": 5.34
    },
    {
      "name": "Hang Seng",
      "value": 26394.26,
      "change_percent": 2.86
    }
  ],
  "commodities": [
    {
      "name": "Gold",
      "value": 4857.6,
      "change_percent": 2.43
    },
    {
      "name": "Silver",
      "value": 81.74,
      "change_percent": 8.23
    },
    {
      "name": "Crude Oil",
      "value": 83.85,
      "change_percent": -15.37
    },
    {
      "name": "USD/INR",
      "value": 93.05,
      "change_percent": -1.55
    }
  ],
  "top_news_headlines": [
    "Ceasefire eases global risk sentiment",
    "Markets rally on falling crude prices",
    "INR strengthens for second week",
    "Equities surge across major sectors"
  ],
  "kapital_gains_views": [
    "Markets stable but volatility may persist",
    "Gradual investing better than timing markets"
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
