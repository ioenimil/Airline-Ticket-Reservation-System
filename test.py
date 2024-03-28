

import unittest



class TestAirlineReservationFunctions(unittest.TestCase):

    def setUp(self):
        self.airline = Node(None)  # Assuming Node class is present

    def test_reserve_ticket(self):
        data = {
            "name": "Thomas Shelby",
            "email": "tommys@example.com",
            "class": "Business",
            "origin": "ABC",
            "destination": "XYZ",
            "departure date": "2024-03-30",
            "departure time": "10:00 AM"
        }
        reserve_ticket(self.airline, data)
        self.assertEqual(self.airline.head.data["name"], "John Doe")

    def test_cancel_reservation(self):
        data = {
            "name": "Jimmy Butler",
            "email": "jayb@example.com",
            "class": "Economy",
            "origin": "DEF",
            "destination": "UVW",
            "departure date": "2024-04-01",
            "departure time": "12:00 PM"
        }
        reserve_ticket(self.airline, data)
        cancel_reservation(self.airline, "Jane Doe")
        self.assertIsNone(self.airline.head)

    def test_check_reservation(self):
        data = {
            "name": "Jimmy Butler",
            "email": "jayb@example.com",
            "class": "First Class",
            "origin": "GHI",
            "destination": "PQR",
            "departure date": "2024-04-02",
            "departure time": "02:00 PM"
        }
        reserve_ticket(self.airline, data)
        self.assertTrue(check_reservation(self.airline, "Alice Smith"))

if __name__ == '__main__':
    unittest.main()