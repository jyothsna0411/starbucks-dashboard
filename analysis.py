import pandas as pd

def load_store_data():
    return pd.read_csv("data/starbucks_locations.csv")

def load_menu_data():
    df = pd.read_csv("data/starbucks_menu.csv")
    df = df.dropna(subset=["Calories", "Fat (g)"])
    return df
