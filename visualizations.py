import plotly.express as px

def top_cities(df, n=10):
    return df['city'].value_counts().head(n)

def plot_caffeine_vs_calories(df):
    # Modified to plot Fat (g) instead of missing Caffeine (mg)
    fig = px.scatter(
        df,
        x="Calories",
        y="Fat (g)",  # Changed from "Caffeine (mg)"
        color="Beverage_category" if "Beverage_category" in df.columns else None,
        hover_name="Beverage" if "Beverage" in df.columns else df.columns[0],
        title="Fat vs Calories in Starbucks Menu"
    )
    return fig
