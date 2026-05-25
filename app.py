
import streamlit as st
import pandas as pd

# 1. Konfiguration
st.set_page_config(page_title="E-Commerce Customer Insights Dashboard", layout="wide")

# 2. Titel
st.title("📊 E-Commerce Customer Insights & Churn Dashboard")

# 3. KPI-Karten
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Gesamtkunden", "5.878")
with col2: st.metric("Umsatz-Champions", "Cluster 2")
with col3: st.metric("Gelegenheitskäufer", "Cluster 0")
with col4: st.metric("Churn-Risiko", "Cluster 1", delta="⚠️")

st.markdown("---")

# 4. Erste Zeile: Hauptanalysen (Clustering & Churn)
left_chart, right_chart = st.columns(2)
with left_chart:
    st.subheader("🎯 Visuelle Cluster-Trennung")
    st.image("cluster_plot.jpg", caption="K-Means Segmentierung")
with right_chart:
    st.subheader("📉 Churn-Analyse")
    st.image("confusion_matrix.png", caption="Confusion Matrix des Random Forest")

# 5. Zweite Zeile: Methodik (Elbow-Plot)
st.markdown("---")
st.subheader("⚙️ Mathematische Methodik")
st.markdown("Hier wurde die optimale Cluster-Anzahl über die Ellbogen-Methode definiert:")
st.image("elbow_plot.png", caption="Elbow-Plot zur Bestimmung der Cluster-Anzahl", width=600)

st.success("✅ Dashboard vollständig mit Methodik-Einblick.")
