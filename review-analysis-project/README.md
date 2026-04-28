# 📊 Customer Review Analysis – Project Workflow

## 🚀 Overview
This project analyzes product reviews to identify customer satisfaction drivers and detect underperforming products using Python and Tableau.

---

## 🔹 Step 1: Data Extraction
- Load dataset from `data/raw/reviews.json` (JSONL format)
- Use `pandas.read_json(..., lines=True)`
- Standardize column names (e.g., `text → review_text`)

---

## 🔹 Step 2: Data Cleaning & Preprocessing
- Handle missing values (`review_text`, `rating`)
- Remove duplicate records
- Convert timestamp → datetime
- Clean text (lowercase, remove special characters)
- Create new features:
  - `sentiment` (from rating)
  - `review_length` (word count)

---

## 🔹 Step 3: Exploratory Data Analysis (EDA)
- Analyze rating distribution
- Compare sentiment breakdown
- Identify top & worst products (ASIN-level)
- Compare verified vs non-verified reviews
- Extract common words from reviews

---

## 🔹 Step 4: Statistical Analysis
- Perform correlation analysis
- Run hypothesis testing (e.g., t-test for verified vs non-verified ratings)

---

## 🔹 Step 5: Data Preparation for Tableau
- Export cleaned dataset → `data/processed/cleaned_reviews.csv`
- Ensure required fields are present:
  `rating, sentiment, asin, verified, helpful, review_length`

---

## 🔹 Step 6: Dashboard (Tableau Public)
- Build interactive dashboard with:
  - Rating distribution
  - Sentiment split
  - Product performance
  - Verified vs rating comparison
- Add at least one interactive filter (ASIN / sentiment)

---

## 🔹 Step 7: Final Deliverables
- Cleaned dataset
- Tableau dashboard (published)
- Project report
- Presentation slides
- Resume & portfolio entry

---

## 👥 Team Guidelines
- Push regular commits with clear messages
- Use separate notebooks per step
- Keep code clean and documented
- Ensure reproducibility

---

## 🎯 Goal
Deliver actionable insights on customer satisfaction and product performance using data-driven analysis.