# E-Commerce Customer Intelligence & Churn Prediction System

[🇬🇧 English](#english) | [🇩🇪 Deutsch](#deutsch)

---

## Dashboard Preview
![Dashboard Preview](dashboard_preview.png)

---

<a name="english"></a>
## 🇬🇧 English
This project leverages advanced data analytics and machine learning to optimize e-commerce performance. By utilizing the *Online Retail II* dataset, the system implements a two-fold analytical approach: **Customer Segmentation** to maximize Customer Lifetime Value (CLV) and **Churn Prediction** to proactively retain customers.

### Key Capabilities
- **RFM Analysis:** Segmentation of customers into high-value, casual, and at-risk groups using K-Means clustering.
- **Predictive Analytics:** Random Forest classification model to identify churn probability.
- **Interactive Dashboard:** A comprehensive Streamlit interface providing actionable business intelligence.

---

<a name="deutsch"></a>
## 🇩🇪 Deutsch
Dieses Projekt nutzt Data Analytics und Machine Learning zur Optimierung der E-Commerce-Performance. Auf Basis des *Online Retail II*-Datensatzes verfolgt das System einen zweistufigen analytischen Ansatz: **Kundensegmentierung** zur Steigerung des Customer Lifetime Value (CLV) und **Churn-Prävention** zur proaktiven Kundenbindung.

### Kernfunktionen
- **RFM-Analyse:** Segmentierung der Kunden in profitable, Gelegenheits- und abwanderungsgefährdete Gruppen mittels K-Means-Clustering.
- **Predictive Analytics:** Random-Forest-Klassifikationsmodell zur Identifikation von Abwanderungswahrscheinlichkeiten.
- **Interaktives Dashboard:** Ein umfassendes Streamlit-Interface zur Bereitstellung handlungsorientierter Business-Insights.

---

## How to Run the Project

### 1. Prerequisites
Ensure you have Python installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```
## 2. Prepare Data
### 2. Prepare Data
Download the **Online Retail II** dataset from the official [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii).

> **Note:** After downloading, please place the file `online_retail_II.xlsx` in the **root folder** of this project.

## 3. Launch Dashboard
Run the following command in your terminal to start the interactive dashboard:
```bash
streamlit run app.py
```
## Tech Stack
- Languages: Python

- Libraries: Pandas, Scikit-Learn, Seaborn, Streamlit

This system translates complex statistical models into clear, strategic recommendations for business optimization.
