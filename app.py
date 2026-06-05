import streamlit as st

# Title of the app
st.title("Day 2: 180-Day Placement Challenge! 🚀🔥")

# Header text
st.header("Welcome to my Python & DSA Journey")

# A cool checklist to display your target
st.subheader("Today's Progress:")
st.checkbox("Python Environment Setup", value=True)
st.checkbox("Streamlit Framework Testing", value=True)
st.checkbox("Ready for Day 3 Basics (Variables & Logic)", value=False)

# Outro message
st.write("Stay tuned! Follow for Part 03.")