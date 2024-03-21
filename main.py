import streamlit as st
import numpy as np
import datetime
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AirlineReservation:
    def __init__(self):
        self.head = None


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
        if current.name["name"] == name:
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
            f"Reservation for {name} @ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} is successful."
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

        # if st.button("Reserve"):
        #     if name:
        #         reserve_ticket(st.session_state.airline, name)

        #         # Display success message for 3 seconds
        #         success = st.success(
        #             f"Reservation for {name} @ {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} is successful."
        #         )
        #         time.sleep(3)
        #         success.empty()
        #     else:
        #         success = st.error(f"Wrong input, please enter a valid name.")
        #         time.sleep(3)
        #         success.empty()
        # display_reservation_code()

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
