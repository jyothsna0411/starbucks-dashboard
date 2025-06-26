

## ✅ **Starbucks Streamlit Dashboard — Step-by-Step Guide**

### 🔹 1. **Set Up Your Environment**

#### a. Create a project folder

```bash
mkdir starbucks_dashboard
cd starbucks_dashboard
```

#### b. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### c. Install Streamlit and other dependencies

```bash
pip install streamlit pandas plotly
```

---

### 🔹 2. **Add Your CSV Data Files**

* Create a folder called `data` inside your project directory.
* Add the following CSVs into it:

  * `starbucks_menu.csv`
  * `starbucks_locations.csv`
---

### 🔹 3. **Write Python Scripts**

#### a. `app.py` – Main Streamlit file

This file runs the dashboard and displays visualizations.

#### b. `analysis.py` – For loading the CSVs

```python
import pandas as pd

def load_menu_data():
    return pd.read_csv("data/starbucks_menu.csv")

def load_store_data():
    return pd.read_csv("data/starbucks_locations.csv")
```

#### c. `visualizations.py` – For creating charts

```python
import plotly.express as px

def top_cities(df, n=10):
    return df['city'].value_counts().head(n)

def plot_caffeine_vs_calories(df):
    fig = px.scatter(
        df,
        x="Calories",
        y="Fat (g)",  # Replaced missing Caffeine
        hover_name=df.columns[0],
        title="Fat vs Calories in Starbucks Menu"
    )
    return fig
```

---

### 🔹 4. **Test the Dashboard Locally**

```bash
streamlit run app.py
```
---

### 🔹 5. **Initialize Git & Push to GitHub**

#### a. Initialize Git

```bash
git init
git add .
git commit -m "Initial commit: Starbucks Streamlit dashboard"
```

#### b. Push to GitHub

```bash
git remote add origin https://github.com/jyothsna0411/starbucks-dashboard.git
git branch -M main
git push -u origin main
```

---

### 🔹 6. **Deploy to Streamlit Cloud**

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Log in → Click **"New App"**
3. Connect to your GitHub repo: `jyothsna0411/starbucks-dashboard`
4. Select:

   * Branch: `main`
   * File: `app.py`
5. Click **Deploy**

---

### 🔹 7. **Add `requirements.txt` for Deployment**

You added this file to specify dependencies:

```txt
streamlit==1.46.1
pandas==2.3.0
plotly==6.2.0
# and other packages...
```
---

### 🔹 8. **Final Touches**

* Verified the deployed app:

  * Scatter plot: Fat vs Calories
  * Bar chart: Top 10 Cities by number of stores
* Resolved encoding issues for city names (some appear in Chinese – that's expected from data).

---

## 🚀 Done!

You now have a **fully working, deployed Streamlit dashboard** showing:

* Nutritional info from Starbucks’ menu
* Top cities by Starbucks store count
  And it's hosted at:
  👉 `https://starbucks-dashboard-3zo3xed5akcnhiran3ntib.streamlit.app/`

---
