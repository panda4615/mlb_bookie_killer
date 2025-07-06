import os

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
import streamlit as st
import pandas as pd
import json
from datetime import date
import glob

st.set_page_config(page_title="MLB Bookie Killer Dashboard", layout="wide")

st.title("⚾️ MLB Bookie Killer Dashboard")

# Load bankroll data
try:
    with open("data/bankroll.json", "r") as f:
        bankroll_data = json.load(f)
    history_df = pd.json_normalize(bankroll_data["history"], record_path=["results"], meta=["date", "ending_bankroll"])
    st.success(f"Current Bankroll: ${bankroll_data['bankroll']:.2f}")
    st.line_chart(history_df.groupby("date")["bankroll"].max())
except Exception as e:
    st.warning(f"Could not load bankroll data: {e}")

# Load today's picks
today = date.today().strftime("%Y-%m-%d")
try:
    picks_files = glob.glob(f"data/pipeline_picks_{today}.json")
    if picks_files:
        with open(picks_files[0], "r") as f:
            picks = json.load(f)
        picks_df = pd.DataFrame(picks)
        st.subheader(f"📈 Today's Picks ({len(picks_df)})")
        st.dataframe(picks_df)
    else:
        st.info("No picks file found for today.")
except Exception as e:
    st.warning(f"Could not load picks: {e}")

# Show win/loss breakdown
try:
    win_count = history_df[history_df["result"] == "Win"].shape[0]
    loss_count = history_df[history_df["result"] == "Loss"].shape[0]
    st.metric("✅ Wins", win_count)
    st.metric("❌ Losses", loss_count)
except:
    st.info("Win/loss data not available yet.")

st.caption("Built for your MLB Bookie Killer pipeline 🚀")
