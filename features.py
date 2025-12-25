def add_features(df):
    df["salary_per_age"] = df["salary"] / df["age"]
    return df