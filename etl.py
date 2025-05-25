import pandas as pd

def load_data(path):
    return pd.read_excel(path)

def clean_data(df):
    # Drop rows with missing values
    df_clean = df.dropna()
    return df_clean

def feature_engineering(df):
    # Calculate 'adjusted_value' for BEV's using a multiplier
    df['adjusted_value'] = df.apply(
        lambda row: row['value'] * 1.1 if row['powertrain'] == 'BEV' else row['value'],
        axis=1
    )

    # Flag if battery electric
    df['is_battery_electric'] = df['powertrain'] == 'BEV'

    # Combined region and category
    df['region_category'] = df['region'] + " - " + df['category']

    # Ranking value within each year (highest value = rank 1)
    df['value_rank_within_year'] = df.groupby('year')['value'].rank(ascending=False)


    return df

if __name__ == "__main__":
    input_path = (r"C:/Users/Miguel/OneDrive/Documents/ALY 4983/mlops-data-lab/IEA-EV-dataEV salesHistoricalCars.xlsx")
    output_path = (r"C:/Users/Miguel/OneDrive/Documents/ALY 4983/mlops-data-lab/data/processed/IEA-EV-dataEV salesHistoricalCars_clean.xlsx")

    df = load_data(input_path)
    df = clean_data(df)
    df = feature_engineering(df)
    df.to_excel(output_path, index=False)
    print("ETL pipeline completed successfully!")
