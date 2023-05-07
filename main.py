import streamlit as st
from streamlit_lottie import st_lottie
import random




st.set_page_config(page_title="Number Guess",page_icon=":tada:",layout="wide")
#lottie_codin = load_lottieurl("https://lottiefiles.com/121675-young-man-having-a-good-idea")

st.markdown("<h1 style='text-align: center; color: red;'>Number Guessing Game</h1>", unsafe_allow_html=True)

with st.container():
    left_column, right_column = st.columns(2)
    
    st.write("---")
    with left_column:   
        st.header('Rules of the game:')
        st.write("1.The game will generate a random number between 1 and 100, and your goal is to guess that number.")
        st.write("2.To make a guess, simply type your number into the text input box and click Enter")
        st.write("3.After each guess, the game will tell you if your guess is too high, too low, or correct.")
        st.write("Have fun and good luck!")


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:   
        guess = st.number_input('Guess a number between 1 and 100', 1, 100, 1 )
    with right_column:
        #st.write("---")
        st.write("You entered:", guess)
        
    #def play_game():


    answer = random.randint(1, 100)
    if guess == answer:
        st.success("You guessed the correct number!")
        st.write("System generated number is {answer}")
    elif guess > answer:
        st.warning("Your guess is too high.")
        st.write("System generated number is ",answer)
    else:
        st.warning("Your guess is too low.")
        st.write("System generated number is ",answer)
# with st.container():
#     st.subheader("Hi Welcome to :wave:")
#     st.title("Number Guessing Game")
#     st.write("The game Rules are:")
#     st.write("1.System already generated a random no between 1 to 100")
#     st.write("2.You have to guess that number")
#     st.write("Lets try Best of Luck! ...")
    



# play_game_button = st.button('Play game')

# if play_game_button:
#     play_game()
