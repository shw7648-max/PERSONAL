"""Streamlit launcher for the standalone Takotako HTML game."""
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="타코타코! 타코야끼 가게",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# This project ships its own trusted HTML and JS.
st.iframe(
    Path(__file__).parent / "index.html",
    width="stretch",
    height="content",
)
