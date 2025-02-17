"""
This module contains the unit tests for the hotels_reservation module.
"""
import unittest
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
)
from hotels_reservation import HotelManager

class TestHotelManager(unittest.TestCase):
    """
    Testing class for the HotelManager.
    """
    def setUp(self):
        """
        Set up the test case with sample data.
        """
        self.hotels_file = "test/unit/test_hotels.json"
        self.customers_file = "test/unit/test_customers.json"
        self.reservations_file = "test/unit/test_reservations.json"
        self.hotel_manager = HotelManager(
            self.hotels_file, self.customers_file, self.reservations_file
        )
        self.hotel_manager.current_hotels = {}
        self.hotel_manager.customers = []
        self.hotel_manager.reservations = []
        self.hotel_manager.save_hotels()
        self.hotel_manager.save_customers()
        self.hotel_manager.save_reservations()

    def test_create_hotel(self):
        """
        Test creating a hotel.
        """
        self.hotel_manager.create_hotel("Test Hotel", 10)
        self.assertIn("1", self.hotel_manager.current_hotels)
        hotel = self.hotel_manager.current_hotels["1"]
        self.assertEqual(hotel.name, "Test Hotel")
        self.assertEqual(hotel.rooms, 10)

    def test_delete_hotel(self):
        """
        Test deleting a hotel.
        """
        self.hotel_manager.create_hotel("Test Hotel", 10)
        self.hotel_manager.delete_hotel("1")
        self.assertRaises(KeyError, self.hotel_manager.delete_hotel, 5)

    def test_modify_hotel_info(self):
        """
        Test modifying hotel information.
        """
        self.hotel_manager.create_hotel("Test Hotel", 10)
        self.hotel_manager.modify_hotel_info(
            "1", name="Updated Hotel", rooms=20
        )
        hotel = self.hotel_manager.current_hotels["1"]
        self.assertEqual(hotel.name, "Updated Hotel")
        self.assertEqual(hotel.rooms, 20)
        self.assertRaises(
            KeyError,
            self.hotel_manager.modify_hotel_info, 5,
            "Modified Hotel", 30
        )

    def test_make_reservation(self):
        """
        Test making a reservation.
        """
        self.hotel_manager.create_hotel("Test Hotel", 10)
        customer = self.hotel_manager.create_customer(
            "Reservation Person", "1234567890", "Reservation@example.com"
        )
        self.hotel_manager.make_reservation("1", customer, 2)
        reservation = self.hotel_manager.reservations[0]
        self.assertEqual(reservation.reservation_id, 1)
        self.assertEqual(reservation.customer_id, customer.customer_id)
        self.assertEqual(reservation.room_count, 2)

    def test_cancel_reservation(self):
        """
        Test cancelling a reservation
        """
        self.hotel_manager.create_hotel("Test Hotel", 10)
        customer = self.hotel_manager.create_customer(
            "Reservation Person", "1234567890", "abcd@ex.com"
        )
        self.hotel_manager.make_reservation("1", customer, 2)
        self.hotel_manager.cancel_reservation("1", 1)
        self.assertRaises(
            KeyError, self.hotel_manager.cancel_reservation, 1, 5
        )

    def test_display_hotel_info(self):
        """
        Test displaying hotel information.
        """
        self.assertRaises(KeyError, self.hotel_manager.display_hotel_info, "5")
        self.hotel_manager.create_hotel("Test Hotel", 10)
        self.assertEqual(self.hotel_manager.display_hotel_info("1"), None)

    def test_create_customer(self):
        """
        Test creating a customer.
        """
        customer = self.hotel_manager.create_customer(
            "Person test", "Phone test", "person@test.com"
        )
        self.assertEqual(customer.customer_id, 1)
        self.assertEqual(customer.name, "Person test")
        self.assertEqual(customer.phone, "Phone test")
        self.assertEqual(customer.email, "person@test.com")

    def test_delete_customer(self):
        """
        Test deleting a customer.
        """
        customer = self.hotel_manager.create_customer(
            "Person test", "Phone test", "person@test.com"
        )
        self.assertEqual(customer.customer_id, 1)
        self.assertNotIn(1, self.hotel_manager.customers)
        self.assertRaises(KeyError, self.hotel_manager.delete_customer, 5)


if __name__ == "__main__":
    unittest.main()
