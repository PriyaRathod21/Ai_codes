flights = []
cargos = []

def add_flight(flight):
    flights.append(flight)

def search_flights(departure, destination):
    return [flight for flight in flights if flight['departure'] == departure and flight['destination'] == destination]

def add_cargo(cargo):
    cargos.append(cargo)

def search_cargos(origin, destination):
    return [cargo for cargo in cargos if cargo['origin'] == origin and cargo['destination'] == destination]

def main():
    add_flight({'flight_number': "F001", 'departure': "Pune", 'destination': "Chennai",
                'departure_time': "08:00", 'arrival_time': "11:00"})

    add_flight({'flight_number': "F002", 'departure': "Mumbai", 'destination': "Delhi",
                'departure_time': "15:30", 'arrival_time': "18:00"})

    add_flight({'flight_number': "F003", 'departure': "Chennai", 'destination': "Pune",
                'departure_time': "18:30", 'arrival_time': "21:30"})

    add_cargo({'cargo_id': "C001", 'flight_number': "F001", 'weight': 500,
               'origin': "Pune", 'destination': "Chennai"})

    add_cargo({'cargo_id': "C002", 'flight_number': "F002", 'weight': 300,
               'origin': "Mumbai", 'destination': "Delhi"})

    add_cargo({'cargo_id': "C003", 'flight_number': "F003", 'weight': 700,
               'origin': "Chennai", 'destination': "Pune"})

    while True:
        print("1. Add Flight")
        print("2. Add Cargo")
        print("3. Search Flights")
        print("4. Search Cargos")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight = {
                'flight_number': input("Enter flight number: "),
                'departure': input("Enter departure: "),
                'destination': input("Enter destination: "),
                'departure_time': input("Enter departure time: "),
                'arrival_time': input("Enter arrival time: ")
            }
            add_flight(flight)
            print("Flight added successfully.")

        elif choice == '2':
            cargo = {
                'cargo_id': input("Enter cargo ID: "),
                'flight_number': input("Enter flight number: "),
                'weight': float(input("Enter cargo weight: ")),
                'origin': input("Enter origin: "),
                'destination': input("Enter destination: ")
            }
            add_cargo(cargo)
            print("Cargo added successfully.")

        elif choice == '3':
            departure = input("Enter departure: ")
            destination = input("Enter destination: ")
            results = search_flights(departure, destination)
            if results:
                print("Flights found:")
                for flight in results:
                    print(f"Flight Number: {flight['flight_number']}")
                    print(f"Departure: {flight['departure']}")
                    print(f"Destination: {flight['destination']}")
                    print(f"Departure Time: {flight['departure_time']}")
                    print(f"Arrival Time: {flight['arrival_time']}")
                    print()
            else:
                print("No flights found for the given departure and destination.")

        elif choice == '4':
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            results = search_cargos(origin, destination)
            if results:
                print("Cargos found:")
                for cargo in results:
                    print(f"Cargo ID: {cargo['cargo_id']}")
                    print(f"Flight Number: {cargo['flight_number']}")
                    print(f"Weight: {cargo['weight']}")
                    print(f"Origin: {cargo['origin']}")
                    print(f"Destination: {cargo['destination']}")
                    print()
            else:
                print("No cargos found for the given origin and destination.")

        elif choice == '5':
            print("Exiting...Thank You!")
            break
            
main()


