"""
Module that manages hotels, customers, and reservations.
"""
import json
# pylint: disable=too-few-public-methods


class Hotel:
    """
    Class that represents a hotel with attributes
    name, rooms, and reservations.
    """
    def __init__(self, name: str, rooms: int):
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def get_hotel_info(self):
        """
        Displays information about the hotel.
        """
        print(f"Hotel Name: {self.name}")
        print(f"Rooms: {self.rooms}")
        print(f"Reservations: {len(self.reservations)}")
        print("\n")

    def to_dict(self) -> dict:
        """
        Converts the hotel object to a dictionary.

        Returns:
            dict: A dictionary with hotel attributes.
        """
        return {"name": self.name, "rooms": self.rooms}


class Customer:
    """
    Class that represents a customer with attributes id,
    name, phone, and email.
    """
    def __init__(self, customer_id: int, name: str, phone: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def get_customer_info(self):
        """
        Displays information about the customer.
        """
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print("\n")

    def to_dict(self):
        """
        Converts the customer object to a dictionary.

        Returns:
            dict: A dictionary with customer attributes.
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


class Reservation:
    """
    Class that represents a reservation with attributes id,
    customer_id, and room_count.
    """
    def __init__(self, reservation_id: int, customer_id: int, room_count: int):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.room_count = room_count

    def get_reservation_info(self):
        """
        Displays information about the reservation.
        """
        print(f"Reservation ID: {self.reservation_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Room Count: {self.room_count}")
        print("\n")

    def to_dict(self):
        """
        Converts the reservation object to a dictionary.

        Returns:
            dict: A dictionary with reservation attributes.
        """
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "room_count": self.room_count
        }


class HotelManager:
    """
    Class that manages hotels, including creation, deletion,
    modification, reservation, and information retrieval.
    """
    def __init__(
            self, hotels_file: str, customers_file: str, reservations_file: str
            ):
        self.hotels_file = hotels_file
        self.customers_file = customers_file
        self.reservations_file = reservations_file
        self.current_hotels = self.load_hotels()
        self.customers = self.load_customers()
        self.reservations = self.load_reservations()

    def load_hotels(self) -> dict:
        """
        Loads hotels from a JSON file and converts them into Hotel instances.

        Returns:
            dict: A dictionary with hotel IDs as keys and
                Hotel instances as values.
        """
        try:
            with open(self.hotels_file, "r", encoding="utf-8") as f:
                hotels_data = json.load(f)
                return {
                    hotel_id: Hotel(data["name"], data["rooms"])
                    for hotel_id, data in hotels_data.items()
                }
        except FileNotFoundError:
            print(
                "Hotels data file not found."
                "Starting with an empty hotels list."
            )
            return {}

    def save_hotels(self):
        """
        Saves the current hotels list to a JSON file.
        """
        with open(self.hotels_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    key: hotel.to_dict()
                    for key, hotel
                    in self.current_hotels.items()
                },
                f, indent=4
            )

    def load_customers(self) -> list:
        """
        Loads customers from a JSON file.

        Returns:
            list: A list of Customer objects.
        """
        try:
            with open(self.customers_file, "r", encoding="utf-8") as f:
                customers_data = json.load(f)
                return [Customer(**customer) for customer in customers_data]
        except FileNotFoundError:
            print(
                "Customers data file not found."
                "Starting with an empty customers list."
            )
            return []

    def save_customers(self):
        """
        Saves the current customers list to a JSON file.
        """
        with open(self.customers_file, "w", encoding="utf-8") as f:
            customers_data = (
                [
                    customer.__dict__
                    if isinstance(customer, Customer) else customer
                    for customer in self.customers
                ]
            )
            json.dump(customers_data, f, indent=4)

    def load_reservations(self) -> list:
        """
        Loads reservations from a JSON file.

        Returns:
            list: A list of Reservation objects.
        """
        try:
            with open(self.reservations_file, "r", encoding="utf-8") as f:
                reservations_data = json.load(f)
                return [
                    Reservation(**reservation)
                    for reservation in reservations_data
                ]
        except FileNotFoundError:
            print(
                "Reservations data file not found. "
                "Starting with an empty reservations list."
            )
            return []

    def save_reservations(self):
        """
        Saves the current reservations list to a JSON file.
        """
        with open(self.reservations_file, "w", encoding="utf-8") as f:
            reservations_data = (
                [
                    reservation.__dict__
                    if isinstance(reservation, Reservation) else reservation
                    for reservation in self.reservations
                ]
            )
            json.dump(reservations_data, f, indent=4)

    def create_hotel(self, name: str, rooms: int):
        """
        Creates a new hotel and adds it to the current hotels list.

        Args:
            name (str): The name of the hotel.
            rooms (int): The number of rooms in the hotel.
        """
        hotel_id = str(len(self.current_hotels) + 1)
        hotel = Hotel(name, rooms)
        self.current_hotels[hotel_id] = hotel
        self.save_hotels()
        print(f"Hotel {hotel.name} created successfully with ID {hotel_id}")

    def delete_hotel(self, hotel_id: str):
        """
        Deletes a hotel from the current hotels list.

        Args:
            hotel_id (str): The ID of the hotel to delete.
        """
        if hotel_id not in self.current_hotels:
            raise KeyError(f"Hotel with ID {hotel_id} not found.")

        del self.current_hotels[hotel_id]
        self.save_hotels()
        print(f"Hotel with ID {hotel_id} deleted successfully.")

    def modify_hotel_info(
            self, hotel_id: str, name: str = None, rooms: int = None
            ):
        """
        Modifies the information of an existing hotel.

        Args:
            hotel_id (str): The ID of the hotel to modify.
            name (str, optional): New name of the hotel. Defaults to None.
            rooms (int, optional): New number of rooms in the hotel.
                Defaults to None.

        Raises:
            KeyError: If the hotel with the given ID is not found.
        """
        if hotel_id not in self.current_hotels:
            raise KeyError(f"Hotel with ID {hotel_id} not found.")

        if name:
            self.current_hotels[hotel_id].name = name
        if rooms:
            self.current_hotels[hotel_id].rooms = rooms

        self.save_hotels()
        print(f"Hotel with ID {hotel_id} updated successfully.")

    def display_hotel_info(self, hotel_id: str):
        """
        Displays information about a hotel.

        Args:
            hotel_id (str): The ID of the hotel to display.

        Raises:
            KeyError: If the hotel with the given ID is not found.
        """
        hotel = self.current_hotels.get(hotel_id)
        if hotel is None:
            raise KeyError(f"Hotel with ID {hotel_id} not found.")
        print(f"Hotel ID: {hotel_id}")
        hotel.get_hotel_info()

    def list_hotels(self):
        """
        Displays a list of all hotels.
        """
        if not self.current_hotels:
            print("No hotels available.")
            return

        print("List of Hotels")
        for hotel_id, hotel in self.current_hotels.items():
            print(f"Hotel ID: {hotel_id}")
            hotel.get_hotel_info()

    def create_customer(self, name: str, phone: str, email: str) -> Customer:
        """
        Creates a new customer and adds it to the current customers list.

        Args:
            name (str): The name of the customer.
            phone (str): The phone number of the customer.
            email (str): The email address of the customer.

        Returns:
            Customer: The created customer object.
        """
        customer_id = len(self.customers) + 1
        customer = Customer(customer_id, name, phone, email)
        self.customers = [
            Customer(**customer)
            if isinstance(customer, dict)
            else customer
            for customer in self.customers
        ]
        self.customers.append(customer)
        self.save_customers()
        print(f"Customer {name} created successfully with ID {customer_id}")
        return customer

    def list_customers(self):
        """
        Displays a list of all customers.
        """
        if not self.customers:
            print("No customers available.")
            return

        print("List of Customers:")
        self.customers = [
            Customer(**customer)
            if isinstance(customer, dict)
            else customer
            for customer in self.customers
        ]
        for customer in self.customers:
            customer.get_customer_info()

    def modify_customer_info(self, customer_id: int, name: str = None,
                             phone: str = None, email: str = None):
        """
        Modifies the information of an existing customer.

        Args:
            customer_id (int): The ID of the customer to modify.
            name (str, optional): New name. Defaults to None.
            phone (str, optional): New phone. Defaults to None.
            email (str, optional): New email. Defaults to None.

        Raises:
            KeyError: If the customer with the given ID is not found.
        """
        self.customers = [
            Customer(**customer)
            if isinstance(customer, dict)
            else customer
            for customer in self.customers
        ]
        for customer in self.customers:
            if customer.customer_id == customer_id:
                if name:
                    customer.name = name
                if phone:
                    customer.phone = phone
                if email:
                    customer.email = email

                self.save_customers()
                print(f"Customer with ID {customer_id} updated successfully.")
                return
        raise KeyError(f"Customer with ID {customer_id} not found.")

    def delete_customer(self, customer_id: int):
        """
        Deletes a customer from the current customers list.

        Args:
            customer_id (int): The ID of the customer to delete.

        Raises:
            KeyError: If the customer with the given ID is not found.
            ValueError: If the customer has active reservations.
        """
        self.customers = [
            Customer(**customer)
            if isinstance(customer, dict)
            else customer
            for customer in self.customers
        ]
        customer = next(
            (c for c in self.customers if c.customer_id == customer_id),
            None
        )
        if customer is None:
            raise KeyError(f"Customer with ID {customer_id} not found.")

        if any(
            reservation.customer_id == customer_id
            for reservation
            in self.reservations
        ):
            print(
                f"Customer with ID {customer_id} "
                "has active reservations and cannot be deleted."
            )
            raise ValueError(
                "Please, cancel all reservations for this customer first."
            )

        self.customers.remove(customer)
        self.save_customers()
        print(f"Customer with ID {customer_id} deleted successfully.")

    def display_customer_info(self, customer_id: int):
        """
        Displays information about a customer.

        Args:
            customer_id (int): The ID of the customer to display.

        Raises:
            KeyError: If the customer with the given ID is not found.
        """
        self.customers = [
            Customer(**customer)
            if isinstance(customer, dict)
            else customer
            for customer in self.customers
        ]
        customer = next(
            (c for c in self.customers if c.customer_id == customer_id),
            None
        )
        if customer is None:
            raise KeyError(f"Customer with ID {customer_id} not found.")

        customer.get_customer_info()

    def make_reservation(
            self, hotel_id: str, customer: Customer, room_count: int
            ):
        """
        Makes a reservation for a customer at a hotel.

        Args:
            hotel_id (str): The ID of the hotel.
            customer (Customer): The customer making the reservation.
            room_count (int): The number of rooms to reserve.

        Raises:
            KeyError: If the hotel with the given ID is not found.
            ValueError: If the hotel does not have enough rooms available.
        """
        hotel = self.current_hotels.get(hotel_id)
        if hotel is None:
            raise KeyError(f"Hotel with ID {hotel_id} not found.")

        if room_count > hotel.rooms:
            raise ValueError(
                f"Hotel {hotel_id} does not have {room_count} rooms available."
            )
        reservation_id = len(self.reservations) + 1
        hotel.rooms -= room_count
        hotel.reservations.append(reservation_id)
        reservation = Reservation(
            reservation_id, customer.customer_id, room_count
        )
        self.reservations = [
            Reservation(**reservation)
            if isinstance(reservation, dict)
            else reservation
            for reservation in self.reservations
        ]
        self.reservations.append(reservation)
        self.save_hotels()
        self.save_reservations()
        print("Reservation made successfully.")

    def cancel_reservation(self, hotel_id: str, reservation_id: int):
        """
        Cancels a reservation for a customer at a hotel.

        Args:
            hotel_id (str): The ID of the hotel.
            reservation_id (int): The ID of the reservation to cancel.

        Raises:
            KeyError: If the hotel with the given ID is not found.
            KeyError: If the reservation with the given ID is not found.
        """
        hotel = self.current_hotels.get(hotel_id)
        if hotel is None:
            raise KeyError(f"Hotel with ID {hotel_id} not found.")
        self.reservations = [
            Reservation(**reservation)
            if isinstance(reservation, dict)
            else reservation
            for reservation in self.reservations
        ]
        reservation = next(
            (
                r
                for r in self.reservations
                if r.reservation_id == reservation_id
            ),
            None,
        )
        if reservation is None:
            raise KeyError(f"Reservation with ID {reservation_id} not found.")

        hotel.rooms += reservation.room_count
        hotel.reservations.remove(reservation_id)
        self.reservations.remove(reservation)
        self.save_hotels()
        self.save_reservations()
        print(f"Reservation with ID {reservation_id} cancelled successfully.")
