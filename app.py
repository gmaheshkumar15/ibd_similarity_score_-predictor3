import streamlit as st
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from merge import merge_features  # your merging logic

# -----------------------------
# Load models safely
# -----------------------------
try:
    log_model = joblib.load("logistic_final.pkl")
    svc_model = joblib.load("svc_final.pkl")
    ann_model = load_model("ann_final.h5")
    scaler = joblib.load("scaler_final.pkl")
except Exception as e:
    st.error(f"Error loading models: {e}")

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="IBD Risk Prediction", layout="wide")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
    .stApp { background-color: #ADD8E6; }
    .stSelectbox>div>div>div>select { text-align: center; } 
    .stSelectbox label {
        font-weight: bold !important;
        font-size: 22px !important;
        color: #000000 !important;
        text-align: center;
        width: 100%; 
        display: block; 
        margin-bottom: 5px; 
    }
    .stSelectbox select {
        border: 2px solid black; 
        border-radius: 5px; 
        padding: 5px 10px; 
    }
    .logo-left, .logo-right { width: 120px; display:block; margin:auto; }
    .institute-name { text-align:center; font-weight:bold; font-size:16px; margin-top:5px; }
    .large-score {
        font-size: 70px !important;
        font-weight: bold;
        color: #8B0000;
        text-align: center;
        margin-top: 20px;
    }
    .intro-paragraph {
        margin-bottom: 0px; 
        padding-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Logos and Title (Row 1)
# -----------------------------
col_logo_left, col_title, col_logo_right = st.columns([1, 5, 1])

with col_logo_left:
    st.markdown('<img src="https://brandlogovector.com/wp-content/uploads/2022/04/IIT-Delhi-Icon-Logo.png" class="logo-left">', unsafe_allow_html=True)
    st.markdown('<div class="institute-name">Indian Institute of Technology Delhi</div>', unsafe_allow_html=True)

with col_title:
    st.markdown(
        "<h1 style='text-align:center; font-size:36px; color:black;'>DMCH-IITD Machine Learning Tool for Estimating the Diet Percentage Similarity with Respect to Diets Consumed by Inflammatory Bowel Disease Patients Prior to Diagnosis</h1>",
        unsafe_allow_html=True
    )

with col_logo_right:
    st.markdown('<img src="https://tse2.mm.bing.net/th/id/OIP.fNb1hJAUj-8vwANfP3SDJgAAAA?pid=Api&P=0&h=180" class="logo-right">', unsafe_allow_html=True)
    st.markdown('<div class="institute-name">Dayanand Medical College and Hospital Ludhiana</div>', unsafe_allow_html=True)

# -----------------------------
# Intro Paragraph
# -----------------------------
st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align:left; font-size:20px; color:black; line-height:1.5;'>
This tool uses a machine learning model to estimate the similarity of your diet with those consumed by patients prior to an Inflammatory Bowel Disease (IBD) diagnosis. 
It uses a Logistic Regression model to estimate prediction. The ML model was trained based on data from a dietary survey conducted by DMCH Ludhiana among IBD patients and controls without IBD. 
IBD patients were asked to report their dietary habits prior to diagnosis, and controls were asked to report current food habits.
</p>
""", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid black;'>", unsafe_allow_html=True)

# -----------------------------
# File Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload Excel file with 81 features", type=["xlsx"])

if uploaded_file:
    try:
        df_raw = pd.read_excel(uploaded_file, engine="openpyxl")
        st.subheader("Raw Data")
        st.dataframe(df_raw.head())

        # Step 1: Merge raw features → 22 merged features
        df_merged = merge_features(df_raw)

        # Step 2: Scale merged features
        df_scaled = scaler.transform(df_merged)

        # Step 3: Predictions
        log_prob = log_model.predict_proba(df_scaled)[:, 1]
        svc_prob = svc_model.predict_proba(df_scaled)[:, 1]
        ann_prob = ann_model.predict(df_scaled).flatten()

        df_predictions = df_merged.copy()
        df_predictions["Logistic_Prob"] = log_prob
        df_predictions["SVC_Prob"] = svc_prob
        df_predictions["ANN_Prob"] = ann_prob

        # Step 4: Layout — Left (features) | Right (predictions)
        col_left, col_right = st.columns([2, 1])

        # ---------- Left Column ----------
        with col_left:
            st.subheader("Merged 22 Features")

            # Split into two equal halves
            feature_names = df_merged.columns.tolist()
            first_half = feature_names[:11]
            second_half = feature_names[11:]

            c1, c2 = st.columns(2)

            # Create display DataFrames
            df_display1 = pd.DataFrame({
                "No.": range(1, len(first_half) + 1),
                "Feature": first_half,
                "Value": [df_merged.iloc[0][f] for f in first_half]
            })

            df_display2 = pd.DataFrame({
                "No.": range(len(first_half) + 1, len(first_half) + len(second_half) + 1),
                "Feature": second_half,
                "Value": [df_merged.iloc[0][f] for f in second_half]
            })

            # Format Value column to 2 decimals
            df_display1["Value"] = df_display1["Value"].map("{:.2f}".format)
            df_display2["Value"] = df_display2["Value"].map("{:.2f}".format)

            # Remove any existing index
            df_display1 = df_display1.reset_index(drop=True)
            df_display2 = df_display2.reset_index(drop=True)

            # Apply styling (center all text, bold headers)
            styler1 = df_display1.style.set_table_styles([
                {"selector": "th", "props": [("font-weight", "bold"), ("text-align", "center")]},
                {"selector": "td", "props": [("text-align", "center")]}
            ])
            styler2 = df_display2.style.set_table_styles([
                {"selector": "th", "props": [("font-weight", "bold"), ("text-align", "center")]},
                {"selector": "td", "props": [("text-align", "center")]}
            ])

            # Display without index
            with c1:
                st.dataframe(styler1, use_container_width=True, hide_index=True)
            with c2:
                st.dataframe(styler2, use_container_width=True, hide_index=True)

        # ---------- Right Column ----------
        with col_right:
            st.subheader("Similarity Score")
            st.markdown(f"**Logistic Regression:** {log_prob[0] * 100:.0f}%")
            st.markdown(f"**Support Vector Classifier:** {svc_prob[0] * 100:.0f}%")
            st.markdown(f"**Artificial Neural Network:** {ann_prob[0] * 100:.0f}%")

            # Step 5: Download Results
            output_excel = "prediction_results.xlsx"
            df_predictions.to_excel(output_excel, index=False, engine="openpyxl")

            with open(output_excel, "rb") as f:
                st.download_button(
                    label="Download Results as Excel",
                    data=f,
                    file_name="prediction_results.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    except Exception as e:
        st.error(f"Error processing file: {e}")
