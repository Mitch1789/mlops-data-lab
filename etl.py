import pandas as pd

def load_data(path):
    return pd.read_excel(path)

def clean_data(df):
    # Drop rows with missing values
    df_clean = df.dropna()
    return df_clean

def feature_engineering(df):
    # Add feature engineering logic here if needed
    return df

if __name__ == "__main__":
    input_path = (r"C:/Users/Miguel/OneDrive/Documents/ALY 4983/mlops-data-lab/IEA-EV-dataEV salesHistoricalCars.xlsx")
    output_path = (r"C:/Users/Miguel/OneDrive/Documents/ALY 4983/mlops-data-lab/data/processed/IEA-EV-dataEV salesHistoricalCars_clean.xlsx")

    df = load_data(input_path)
    df = clean_data(df)
    df = feature_engineering(df)
    df.to_excel(output_path, index=False)
    print("ETL pipeline completed successfully!")
