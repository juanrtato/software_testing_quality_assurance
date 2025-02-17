"""
This module provides a command-line interface for managing hotels,
customers, and reservations.
"""
from hotels_reservation import HotelManager


def handle_hotels(hotel_manager):
    """
    Handles hotel-related operations.
    """
    hotels_list = hotel_manager.current_hotels

    print("\nHotels:")
    print("1. Create Hotel")
    print("2. Delete Hotel")
    print("3. Modify Hotel Info")
    print("4. Display Hotel Info")
    print("5. Display all Hotels Info")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter hotel name: ")
        rooms = int(input("Enter number of rooms: "))
        hotel_manager.create_hotel(name, rooms)
    elif choice == '2':
        hotel_id = input("Enter hotel ID to delete: ")
        if hotel_id not in hotels_list:
            print(f"Hotel with ID {hotel_id} not found.")
        else:
            hotel_manager.delete_hotel(hotel_id)
    elif choice == '3':
        hotel_id = input("Enter hotel ID to modify: ")
        print(hotel_id)
        print(hotels_list)
        print('hello')
        if hotel_id not in hotels_list:
            print(f"Hotel with ID {hotel_id} not found.")
        else:
            print("Current hotel info:")
            hotel_manager.display_hotel_info(hotel_id)
            name = input(
                "Enter new hotel name (leave blank to keep current): "
            ) or None
            rooms = input(
                "Enter new number of rooms (leave blank to keep current): "
            )
            rooms = int(rooms) if rooms else None
            hotel_manager.modify_hotel_info(hotel_id, name, rooms)
    elif choice == '4':
        hotel_id = input("Enter hotel ID to display info: ")
        if hotel_id not in hotels_list:
            print(f"Hotel with ID {hotel_id} not found.")
        else:
            hotel_manager.display_hotel_info(hotel_id)
    elif choice == '5':
        hotel_manager.list_hotels()

    input("Press Enter to return to the main menu...")


def handle_reservations(hotel_manager):
    """
    Handles reservation-related operations.
    """
    hotels_list = hotel_manager.current_hotels

    print("\nReservations:")
    print("6. Make Reservation")
    print("7. Cancel Reservation")

    choice = input("Enter your choice: ")

    if choice == '6':
        hotel_id = input("Enter hotel ID for reservation: ")
        if hotel_id not in hotels_list:
            print(f"Hotel with ID {hotel_id} not found.")
        else:
            customer_id = input(
                "Enter customer ID (leave blank to create a new customer): "
            )
            if customer_id:
                customer = next(
                    (
                        c
                        for c in hotel_manager.customers
                        if c.customer_id == int(customer_id)
                    ), None
                )
                if customer is None:
                    print(f"Customer with ID {customer_id} not found.")
                    return
            else:
                print("Creating a new customer...")
                name = input("Enter customer name: ")
                phone = input("Enter customer phone: ")
                email = input("Enter customer email: ")
                customer = hotel_manager.create_customer(name, phone, email)

            room_count = int(input("Enter number of rooms to reserve: "))
            hotel_manager.make_reservation(hotel_id, customer, room_count)
    elif choice == '7':
        hotel_id = input("Enter hotel ID for cancellation: ")
        if hotel_id not in hotels_list:
            print(f"Hotel with ID {hotel_id} not found.")
        else:
            reservation_id = int(input("Enter reservation ID to cancel: "))
            hotel_manager.cancel_reservation(hotel_id, reservation_id)

    input("Press Enter to return to the main menu...")


def handle_customers(hotel_manager):
    """
    Handles customer-related operations.
    """
    print("\nCustomers:")
    print("8. List Customers")
    print("9. Create Customer")
    print("10. Modify Customer")
    print("11. Delete Customer")
    print("12. Display Customer Info")

    choice = input("Enter your choice: ")

    if choice == '8':
        hotel_manager.list_customers()
    elif choice == '9':
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        email = input("Enter customer email: ")
        hotel_manager.create_customer(name, phone, email)
    elif choice == '10':
        customer_id = int(input("Enter customer ID to modify: "))
        customer = next(
            (
                c
                for c in hotel_manager.customers
                if c.customer_id == customer_id
            ),
            None
        )
        if customer is None:
            print(f"Customer with ID {customer_id} not found.")
        else:
            print("Current customer info:")
            hotel_manager.display_customer_info(customer_id)
            name = input(
                "Enter new customer name (leave blank to keep current): "
            ) or None
            phone = input(
                "Enter new customer phone (leave blank to keep current): "
            ) or None
            email = input(
                "Enter new customer email (leave blank to keep current): "
            ) or None
            hotel_manager.modify_customer_info(customer_id, name, phone, email)
    elif choice == '11':
        customer_id = int(input("Enter customer ID to delete: "))
        customer = next(
            (
                c
                for c in hotel_manager.customers
                if c.customer_id == customer_id
            ),
            None
        )
        if customer is None:
            print(f"Customer with ID {customer_id} not found.")
        else:
            hotel_manager.delete_customer(customer_id)
    elif choice == '12':
        customer_id = int(input("Enter customer ID to display info: "))
        customer = next(
            (
                c
                for c in hotel_manager.customers
                if c.customer_id == customer_id
            ),
            None
        )
        if customer is None:
            print(f"Customer with ID {customer_id} not found.")
        else:
            hotel_manager.display_customer_info(customer_id)

    input("Press Enter to return to the main menu...")


def main():
    """
    Main function for the hotel manager command-line interface.
    """
    hotels_data_path = "./data/hotels.json"
    customers_data_path = "./data/customers.json"
    reservations_data_path = "./data/reservations.json"

    hotel_manager = HotelManager(
        hotels_data_path, customers_data_path, reservations_data_path
    )

    while True:
        print("\nHOTEL MANAGER")
        print("\nA: Hotel Operations")
        print("B: Reservations")
        print("C: Customers")
        print("D: Exit")

        choice = input("Enter your choice: ")

        try:
            if choice in ['A', 'a']:
                handle_hotels(hotel_manager)
            elif choice in ['B', 'b']:
                handle_reservations(hotel_manager)
            elif choice in ['C', 'c']:
                handle_customers(hotel_manager)
            elif choice in ['D', 'd']:
                break
            else:
                print("Invalid choice. Please try again.")
        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
