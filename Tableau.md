# 📊 Tableau Analysis Workflow – Customer Review Project

## 🎯 Goal
Build an interactive dashboard to visualize customer satisfaction, product performance, and key insights derived from review data.

---

## 🔹 Step 1: Connect Data
- Open Tableau Public
- Connect to: `data/processed/cleaned_reviews.csv`
- Verify fields:
  - rating (numeric)
  - sentiment (dimension)
  - asin (dimension)
  - verified (boolean)
  - helpful (numeric)
  - review_length (numeric)
  - date (date)

---

## 🔹 Step 2: Data Preparation (Light in Tableau)
- Convert `verified` → Dimension (True/False)
- Convert `sentiment` → Dimension
- Ensure `rating` is numeric (measure)
- Create calculated field (if needed):
  
  ### ⭐ Avg Rating

---

## 🔹 Step 3: Build Core Visualizations

### 📊 1. Rating Distribution
- Chart: Bar Chart
- Columns → rating
- Rows → COUNT(rating)
- Purpose:
- Understand rating spread (1–5)

---

### 📊 2. Sentiment Distribution
- Chart: Pie Chart / Bar Chart
- Use sentiment
- Show % distribution
- Purpose:
- Overall customer satisfaction

---

### 📊 3. Product Performance (CRITICAL)
- Chart: Bar Chart
- Columns → asin
- Rows → AVG(rating)
- Sort ascending

👉 Create 2 views:
- Worst products
- Best products

---

### 📊 4. Verified vs Rating
- Chart: Side-by-side Bar / Box Plot
- Columns → verified
- Rows → AVG(rating)

👉 Insight:
- Compare trustworthiness of reviews

---

### 📊 5. Review Length vs Rating
- Chart: Box Plot / Scatter
- Columns → rating
- Rows → review_length

👉 Insight:
- Longer reviews → complaints?

---

### 📊 6. Helpful Votes Analysis
- Chart: Scatter Plot
- X → rating
- Y → helpful

👉 Insight:
- Which reviews users find helpful

---

## 🔹 Step 4: Add Filters (MANDATORY)
Add at least 1–2 interactive filters:

- asin (product filter)
- sentiment
- verified

👉 Place filters on dashboard for user interaction

---

## 🔹 Step 5: Build Dashboard Layout

### 🧩 Suggested Layout:

[ Top Section ]
- KPI Cards:
- Avg Rating
- Total Reviews
- % Positive Reviews

[ Middle Section ]
- Rating Distribution
- Sentiment Distribution

[ Bottom Section ]
- Product Performance
- Verified vs Rating
- Helpful Analysis

[ Side Panel ]
- Filters (asin, sentiment, verified)

---

## 🔹 Step 6: Add Interactivity
- Enable filter actions (click on product → filter dashboard)
- Add tooltips:
- Show rating, sentiment, helpful votes

---

## 🔹 Step 7: Design & Polish
- Use consistent colors:
- Positive → Green
- Negative → Red
- Add titles and captions
- Keep layout clean (no clutter)

---

## 🔹 Step 8: Publish Dashboard
- Publish on Tableau Public
- Copy dashboard link
- Save in:
`tableau/dashboard_links.md`

---

## 🔹 Step 9: Export Screenshots
- Save:
- Full dashboard
- Key charts
- Store in:
`tableau/screenshots/`

---

## 🎯 Expected Outcome
- Interactive dashboard showing:
- Customer sentiment trends
- Product performance
- Key behavioral insights

---

## ⚠️ Important Notes
- Do NOT clean data in Tableau (already done in Python)
- Focus on visualization + insights
- Every chart must answer a business question