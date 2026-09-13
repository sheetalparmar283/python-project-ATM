x="radar"
y=x[::-1]
if (x==y):
   print('palindrome')
else:
   print('not')

import streamlit as st

st.set_page_config(page_title="Python ATM", page_icon="💳")

# Session state initialize (Memory management)
if "balance" not in st.session_state:
    st.session_state.balance = 5000
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "attempts" not in st.session_state:
    st.session_state.attempts = 3

CORRECT_PIN = 1234

st.title("💳 Python ATM Simulator")

# Screen 1: PIN Verification
if not st.session_state.authenticated:
    if st.session_state.attempts > 0:
        pin_input = st.number_input("Enter 4-Digit PIN", min_value=0, max_value=9999, step=1, format="%d")
        
        if st.button("Login"):
            if pin_input == CORRECT_PIN:
                st.session_state.authenticated = True
                st.success("Login Successful!")
                st.rerun()
            else:
                st.session_state.attempts -= 1
                st.error(f"Incorrect PIN! Attempts left: {st.session_state.attempts}")
    else:
        st.error("Card Blocked! Too many wrong attempts.")

# Screen 2: ATM Dashboard
else:
    st.metric(label="Current Balance", value=f"Rs {st.session_state.balance}")
    
    tab1, tab2, tab3 = st.tabs(["Withdraw", "Deposit", "Exit"])
    
    with tab1:
        withdraw_amt = st.number_input("Amount to Withdraw", min_value=100, step=100, key="withdraw_box")
        if st.button("Confirm Withdrawal"):
            if st.session_state.balance - withdraw_amt >= 500:
                st.session_state.balance -= withdraw_amt
                st.success(f"Withdrawn Rs {withdraw_amt}! Remaining: Rs {st.session_state.balance}")
                st.rerun()
            else:
                st.warning("Failed! Minimum balance of Rs 500 must remain.")
                
    with tab2:
        deposit_amt = st.number_input("Amount to Deposit", min_value=100, step=100, key="deposit_box")
        if st.button("Confirm Deposit"):
            st.session_state.balance += deposit_amt
            st.success(f"Deposited Rs {deposit_amt}! Updated Balance: Rs {st.session_state.balance}")
            st.rerun()
            
    with tab3:
        if st.button("Logout / Take Card"):
            st.session_state.authenticated = False
            st.session_state.attempts = 3
            st.info("Thank you for using Python ATM!")
            st.rerun()