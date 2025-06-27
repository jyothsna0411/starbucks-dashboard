import streamlit as st
from analysis import load_store_data, load_menu_data
from visualizations import top_cities, plot_caffeine_vs_calories

st.set_page_config(layout="wide")
st.title("☕ Starbucks Dashboard")

# Load the data
menu_df = load_menu_data()
store_df = load_store_data()  

# Show chart
st.header("📊 Fat vs Calories in Starbucks Menu")
fig = plot_caffeine_vs_calories(menu_df)
st.plotly_chart(fig)

# Show top cities chart
st.header("🏙️ Top 10 Cities with Most Starbucks Stores")
top_cities_data = top_cities(store_df)
st.bar_chart(top_cities_data)
