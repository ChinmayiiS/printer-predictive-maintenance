def validate_data(df):
    assert df.isnull().sum().sum() < 100, "Too many missing values"
    required_cols = ["temperature", "print_count", "error_count", "toner_level", "failure"]
    
    for col in required_cols:
        assert col in df.columns, f"{col} missing"

    return True
