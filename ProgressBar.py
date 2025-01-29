import streamlit as st

goal = 80000
current_amount = 0

st.title("Fundraising Progress")

# Input field to simulate donations
donation = st.number_input("Enter donation amount:", min_value=0, step=100)
if st.button("Add Donation"):
    current_amount += donation
    current_amount = min(current_amount, goal)

# Display progress bar
progress = current_amount / goal
st.progress(progress)

st.write(f"Raised: ${current_amount:,} / ${goal:,}")
