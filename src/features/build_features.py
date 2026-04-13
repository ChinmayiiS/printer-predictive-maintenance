def build_features(df):
    # Example feature engineering
    df["usage_intensity"] = df["print_count"] / (df["toner_level"] + 1)
    return df
