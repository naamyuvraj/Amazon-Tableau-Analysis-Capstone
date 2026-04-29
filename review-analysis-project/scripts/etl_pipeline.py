# ==========================================
# ETL PIPELINE: Customer Review Analysis
# ==========================================

import pandas as pd
import re
import os

# ==============================
# 1. EXTRACT
# ==============================
def extract_data(file_path):
    print("📥 Extracting data...")
    df = pd.read_json(file_path, lines=True)
    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")
    return df


# ==============================
# 2. CLEAN
# ==============================
def clean_data(df):
    print("🧹 Cleaning data...")

    # Rename columns
    df = df.rename(columns={
        "text": "review_text",
        "helpful_vote": "helpful",
        "verified_purchase": "verified"
    })

    # Convert timestamp → datetime
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    # Handle missing values
    df = df.dropna(subset=["review_text", "rating"])

    # Drop columns with unhashable types before deduplication
    df = df.drop(columns=["images"], errors="ignore")

    # Remove duplicates
    df = df.drop_duplicates()

    # Fix data types
    df["rating"] = df["rating"].astype(float)
    df["verified"] = df["verified"].astype(bool)

    print("Cleaning completed")
    return df


# ==============================
# 3. TRANSFORM
# ==============================
def transform_data(df):
    print("🔄 Transforming data...")

    # Text cleaning
    def clean_text(text):
        text = str(text).lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    df["cleaned_text"] = df["review_text"].apply(clean_text)

    # Sentiment feature
    def sentiment(r):
        if r >= 4:
            return "Positive"
        elif r == 3:
            return "Neutral"
        else:
            return "Negative"

    df["sentiment"] = df["rating"].apply(sentiment)

    # Review length
    df["review_length"] = df["cleaned_text"].apply(lambda x: len(x.split()))

    # Fill missing helpful votes
    df["helpful"] = df["helpful"].fillna(0)

    # Drop unnecessary columns
    df = df.drop(columns=["images", "user_id", "parent_asin", "timestamp"], errors="ignore")

    print("Transformation completed")
    return df


# ==============================
# 4. LOAD
# ==============================
def load_data(df, output_path):
    print("💾 Saving processed data...")

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Data saved to: {output_path}")


# ==============================
# 5. MAIN PIPELINE
# ==============================
def run_pipeline():
    print("🚀 Starting ETL Pipeline...\n")

    raw_path = "../data/raw/Subscription_Boxes.jsonl"
    output_path = "../data/processed/final_reviews.csv"

    # Run steps
    df = extract_data(raw_path)
    df = clean_data(df)
    df = transform_data(df)
    load_data(df, output_path)

    print("\n✅ ETL Pipeline Completed Successfully!")


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    run_pipeline()