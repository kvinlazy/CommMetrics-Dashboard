import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Mock data for demonstration purposes
def generate_mock_data():
    dates = pd.date_range(start="2023-01-01", end="2023-01-31")
    data = {
        "Date": dates,
        "Message Volume": np.random.randint(50, 200, len(dates)),
        "Response Time (minutes)": np.random.randint(5, 30, len(dates)),
        "Referrals Processed": np.random.randint(10, 50, len(dates)),
    }
    return pd.DataFrame(data)

# Load data
data = generate_mock_data()

# Streamlit app
st.title("Communication Data Dashboard")

# Tabs for organizing metrics
tab1, tab2, tab3 = st.tabs(["Message Volume", "Response Times", "Referrals Processed"])

# Tab 1: Message Volume
with tab1:
    st.subheader("Message Volume Over Time")
    fig_volume = px.line(data, x="Date", y="Message Volume", title="Message Volume Over Time")
    st.plotly_chart(fig_volume, use_container_width=True)

# Tab 2: Response Times
with tab2:
    st.subheader("Response Times")
    fig_response = px.bar(data, x="Date", y="Response Time (minutes)", title="Average Response Times")
    st.plotly_chart(fig_response, use_container_width=True)

# Tab 3: Referrals Processed
with tab3:
    st.subheader("Number of Referrals Processed")
    fig_referrals = px.scatter(
        data, x="Date", y="Referrals Processed", size="Referrals Processed",
        title="Referrals Processed Over Time", color="Referrals Processed"
    )
    st.plotly_chart(fig_referrals, use_container_width=True)

# Summary Table
st.sidebar.header("Summary Statistics")
summary = data[["Message Volume", "Response Time (minutes)", "Referrals Processed"]].describe()
st.sidebar.dataframe(summary)

# Footer
st.markdown("### Data Source")
st.markdown("This dashboard visualizes communication metrics for January 2023. Replace the mock data with actual metrics for real insights.")
