import streamlit as st
import numpy as np
import datetime
import time
from linkedlist import *
from functions import *


def main():
    st.balloons()
    time.sleep(1)
    if "airline" not in st.session_state:
        st.session_state.airline = AirlineReservation()

    st.title("Airline Ticket Reservation System")

    options = [
        "Reserve a ticket",
        "Cancel a reservation",
        "Check reservation",
        "Display passengers",
    ]
    choice = st.sidebar.selectbox("Select an option", options)
    travel_classes = ["Business Class", "First Class", "Normal Class"]
    if choice == "Reserve a ticket":

        with st.form("my_form"):

            name = st.text_input("Enter passenger's name:")
            age = st.text_input("Enter passenger's age")
            class_choice = st.selectbox("Select the time of travel", travel_classes)
            checkbox_val = st.checkbox("Form checkbox")
            data = {"name": name, "age": age, "class": class_choice}

            #  submit button.
            submitted = st.form_submit_button("Submit")

            if submitted:
                handle_submit(input=data)
                st.write("slider", slider_val, "checkbox", checkbox_val)

    elif choice == "Cancel a reservation":
        name = st.text_input("Enter passenger name to cancel reservation:")
        with st.spinner("Wait for it..."):
            display_passengers(st.session_state.airline)

        if st.button("Cancel Reservation"):
            cancel_reservation(st.session_state.airline, name)
        display_cancel_code()

    elif choice == "Check reservation":
        name = st.text_input("Enter passenger name to check reservation:")
        if st.button("Check"):
            check_reservation(st.session_state.airline, name)
        display_check_code()

    elif choice == "Display passengers":
        display_passengers(st.session_state.airline)
        display_passengers_code()


if __name__ == "__main__":
    main()
