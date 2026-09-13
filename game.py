import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")

st.title("🎯 Number Guessing Game")
st.write("1 se 100 ke beech ka secret number guess kijiye! Aapke paas kul 5 attempts hain.")

# Session state initialize karein (Memory banaye rakhne ke liye)
if "secret_num" not in st.session_state:
    st.session_state.secret_num = 42
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 5
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Remaining attempts dikhana
st.metric(label="Chances Left", value=st.session_state.attempts_left)

# Jab game chal raha ho
if not st.session_state.game_over and st.session_state.attempts_left > 0:
    guess = st.number_input(
        "Apna guess daaliye:",
        min_value=1,
        max_value=100,
        step=1,
        key="user_guess"
    )

    if st.button("Submit Guess"):
        # Har guess par 1 attempt kam hoga
        st.session_state.attempts_left -= 1

        if guess < st.session_state.secret_num:
            st.warning("📉 Too Low! Bada number socho.")
        elif guess > st.session_state.secret_num:
            st.warning("📈 Too High! Chhota number socho.")
        else:
            st.success("🎉 Correct Answer! Aap jeet gaye!")
            st.session_state.game_over = True

        # Check agar attempts khatam ho gaye
        if st.session_state.attempts_left == 0 and not st.session_state.game_over:
            st.error(f"💀 Game Over! The secret number was {st.session_state.secret_num}.")
            st.session_state.game_over = True

# Game khatam hone par Restart ka option
if st.session_state.game_over or st.session_state.attempts_left == 0:
    if st.button("Play Again"):
        st.session_state.secret_num = 42
        st.session_state.attempts_left = 5
        st.session_state.game_over = False
        st.rerun()