import streamlit as st
import numpy as np
import datetime
import time
from linkedlist import *

def reserve_ticket(airline, data):
    if not data:
        st.write("Please enter a valid data.")
        return
    new_node = Node(data)
    if not airline.head or airline.head.data["name"] > data["name"]:
        new_node.next = airline.head
        airline.head = new_node
    else:
        current = airline.head
        while current.next and current.next.data["name"] < data["name"]:
            current = current.next
        new_node.next = current.next
        current.next = new_node


def cancel_reservation(airline, name):
    if not airline.head:
        st.error("No reservations found.")
        return
    if airline.head.data == name:
        airline.head = airline.head.next

        success = st.success(f"Reservation for {name} is cancelled.")
        time.sleep(3)
        success.empty()
        return
    current = airline.head
    while current.next:
        if current.next.data == name:
            current.next = current.next.next
            st.write(f"Reservation for {name} cancelled.")
            return
        current = current.next
    error = st.error(f"No reservation found for {name}.")
    time.sleep(3)
    error.empty()


def check_reservation(airline, name):
    current = airline.head
    while current:
        if name in current.data["name"].upper() or name in current.data["name"].title() or name in current.data["name"].lower():
            st.dataframe(current.data)
            st.write(f"Reservation found for **{name}**.")
            return
        current = current.next
    st.write(f"No reservation found for *{name}*.")


def display_passengers(airline):
    current = airline.head
    rows = []  # List to hold each row as a dictionary
    counter = 1
    if not current:
        st.write("No reservations found.")
        return
    st.write("Passengers:")
    while current:
        # Each row is represented as a dictionary with headers as keys
        row = {
            "No.": counter,
            "Passenger Name": current.data["name"],
            "Age": current.data["age"],
            "Travel Type": current.data["class"],
        }
        rows.append(row)
        counter += 1
        current = current.next
    # Creating columns to center the dataframe
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:  # This places the dataframe in the middle column
        st.dataframe(rows, use_container_width=True)


def display_reservation_code():
    st.markdown("### Reservation Code")
    st.code(
        """
def reserve_ticket(airline, name):
    if not name:
        st.write("Please enter a valid name.")
        return
    new_node = Node(name)
    if not airline.head or airline.head.name > name:
        new_node.next = airline.head
        airline.head = new_node
    else:
        current = airline.head
        while current.next and current.next.name < name:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    """
    )


def display_cancel_code():
    st.markdown("### Cancel Reservation Code")
    st.code(
        """
def cancel_reservation(airline, name):
    if not airline.head:
        st.error("No reservations found.")
        return
    if airline.head.name == name:
        airline.head = airline.head.next
        
        success = st.success(f"Reservation for {name} is cancelled.")
        time.sleep(3)
        success.empty() 
        return
    current = airline.head
    while current.next:
        if current.next.name == name:
            current.next = current.next.next
            st.write(f"Reservation for {name} cancelled.")
            return
        current = current.next
    st.write(f"No reservation found for {name}.")
    """
    )


def display_check_code():
    st.markdown("### Check Reservation Code")
    st.code(
        """
def check_reservation(airline, name):
    current = airline.head
    while current:
        if current.name == name:
            st.write(f"Reservation found for **{name}**.")
            return
        current = current.next
    st.write(f"No reservation found for *{name}*.")
    """
    )


def play_sound():
    audio_file = open("./media/sound/ambient-piano-logo-165357.mp3", "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")


def handle_submit(input):
    if input:
        reserve_ticket(st.session_state.airline, input)
        # Display success message for 3 seconds
        success = st.success(
            f"Reservation for {input['name']} @ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} is successful."
        )
        time.sleep(3)
        success.empty()
    else:
        success = st.error(f"Wrong input, please enter a valid name.")
        time.sleep(3)
        success.empty()
    display_reservation_code()


def display_passengers_code():
    st.markdown("### Display Passengers Code")
    st.code(
        """
def display_passengers(airline):
    current = airline.head
    rows = [] 
    counter = 1
    if not current:
        st.write("No reservations found.")
        return
    st.write("Passengers:")
    while current:
        row = {"No.": counter, "Passenger Name": current.name}
        rows.append(row)
        counter += 1
        current = current.next
    col1, col2, col3 = st.columns([1,2,1])  # Adjust the ratio as needed
    with col2:  
        st.dataframe(rows, use_container_width=True)
    """
    )
