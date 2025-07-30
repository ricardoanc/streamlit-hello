import streamlit as st
import pandas as pd
import numpy as np
import io

st.set_page_config(page_title="Insight Genie", layout="wide")
st.title("🔍 Insight Genie – First Look Analyst")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📈 Basic Info")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    st.write(f"Missing values: {df.isnull().sum().sum()}")

    st.subheader("🧠 Insight Suggestions")

    # Column types
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    text_cols = df.select_dtypes(include='object').columns.tolist()
    date_cols = df.select_dtypes(include='datetime').columns.tolist()

    if numeric_cols:
        st.markdown(f"**Numeric columns detected:** {', '.join(numeric_cols)}")
        st.markdown("- ➕ Try regression or clustering.")
        st.markdown("- 📊 Explore histograms or boxplots.")

    if text_cols:
        st.markdown(f"**Text columns detected:** {', '.join(text_cols)}")
        st.markdown("- 💬 Run sentiment or keyword analysis.")
        st.markdown("- 🧠 Use NLP tools for deeper insight.")

    if date_cols:
        st.markdown(f"**Datetime columns detected:** {', '.join(date_cols)}")
        st.markdown("- 📆 Try time series plots or seasonality checks.")

    st.subheader("⚠️ Data Quality Checks")
    for col in df.columns:
        nulls = df[col].isnull().sum()
        if nulls > 0:
            st.warning(f"Column '{col}' has {nulls} missing values.")

        if df[col].dtype == 'object' and df[col].nunique() > 50:
            st.info(f"Column '{col}' has high cardinality ({df[col].nunique()} unique values).")

    st.success("✅ Insight generation complete!")