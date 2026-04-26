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
  "week_range": "20 Apr – 24 Apr 2026",
  "indian_indices": [
    {
      "name": "Nifty 50",
      "value": 23897.95,
      "change_percent": -1.92,
      "pe_ratio": 26.0
    },
    {
      "name": "Nifty Next 50",
      "value": 69883.95,
      "change_percent": -0.65,
      "pe_ratio": 27.0
    },
    {
      "name": "Nifty Midcap 150",
      "value": 21875.95,
      "change_percent": -0.68,
      "pe_ratio": 25.0
    },
    {
      "name": "Nifty 500",
      "value": 22570.05,
      "change_percent": -1.29,
      "pe_ratio": 15.0
    }
  ],
  "global_indices": [
    {
      "name": "S&P 500",
      "value": 7165.08,
      "change_percent": 1.43
    },
    {
      "name": "Dow Jones",
      "value": 49230.71,
      "change_percent": 0.17
    },
    {
      "name": "Nasdaq",
      "value": 24836.6,
      "change_percent": 2.38
    },
    {
      "name": "Nikkei 225",
      "value": 59716.18,
      "change_percent": 1.52
    },
    {
      "name": "Hang Seng",
      "value": 25978.07,
      "change_percent": -1.45
    }
  ],
  "commodities": [
    {
      "name": "Gold",
      "value": 4722.3,
      "change_percent": 0.51
    },
    {
      "name": "Silver",
      "value": 76.38,
      "change_percent": -0.04
    },
    {
      "name": "Crude Oil",
      "value": 94.4,
      "change_percent": 2.46
    },
    {
      "name": "USD/INR",
      "value": 94.11,
      "change_percent": 1.63
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
