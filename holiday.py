'''
The code is a Python program that helps users calculate the total cost of a holiday based on the cost of a flight to a chosen destination, the cost of a hotel stay, and the cost of renting a car.

The program defines several functions to prompt the user for information, including a function to retrieve a list of destinations and display them to the user, a function to prompt the user to choose a destination and retrieve the price of the flight, a function to prompt the user for the number of nights they will be staying in a hotel, a function to prompt the user for the number of days they will be renting a car, and a function to calculate the total cost of the holiday.

The program then calls these functions in sequence to gather the necessary information, calculate the total cost of the holiday, and display a breakdown of the costs to the user.
'''
def get_destinations():
    destinations = [
        ("1. HKIA - Hong Kong International Airport", 820.00),
        ("2. JFK - John F. Kennedy International Airport", 420.00),
        ("3. MEX - Mexico City International Airport", 850.00),
        ("4. CPT - Cape Town International Airport", 810.00),
        ("5. MAN - Manchester Airport", 200.00),
    ]
    return destinations

def display_destinations(destinations):
    print("Select your holiday destination:\n")
    for code, (city, price) in enumerate(destinations, 1):
        print(f"{code}. {city} ({price:.2f} GBP)")
    print()

def choose_destination():
    while True:
        try:
            selection = int(input("Type the corresponding number to choose a destination: "))
            if selection < 1 or selection > 5:
                raise ValueError("Invalid selection")
            break
        except ValueError:
            print("Invalid selection, please choose a number between 1 and 5.")
    destinations = get_destinations()
    return destinations[selection - 1][1]

def get_hotel_cost():
    num_nights = int(input("How many nights will you be staying? "))
    return num_nights * 125.00

def get_car_rental_cost():
    num_days = int(input("How many days will you be renting a vehicle? "))
    return num_days * 75.00

def calculate_holiday_cost(hotel_cost, car_rental_cost, flight_cost):
    return hotel_cost + car_rental_cost + flight_cost

destinations = get_destinations()
display_destinations(destinations)
flight_cost = choose_destination()
hotel_cost = get_hotel_cost()
car_rental_cost = get_car_rental_cost()
subtotal = calculate_holiday_cost(hotel_cost, car_rental_cost, flight_cost)
VAT = subtotal * 0.2
total_cost = subtotal + VAT

print("\n\nBreakdown of Total Cost")
print("-----------------------")
print(f"Hotel Cost: £{hotel_cost:.2f}")
print(f"Car Rental Cost: £{car_rental_cost:.2f}")
print(f"Flight Cost: £{flight_cost:.2f}")
print("-----------------------")
print(f"Subtotal: £{subtotal:.2f}")
print(f"VAT (20%): £{VAT:.2f}")
print("-----------------------")
print(f"Total Cost (excluding VAT): £{subtotal:.2f}")
print(f"Total Cost (including VAT): £{total_cost:.2f}")
print("\n*VAT (Value Added Tax) is not included in the total cost.")
