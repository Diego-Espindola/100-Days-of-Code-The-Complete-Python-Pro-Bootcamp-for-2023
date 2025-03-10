class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(flight_data):
    """
    Parses flight data received from the Amadeus API to identify the cheapest flight option among
    multiple entries.
    Args:
        data (dict): The JSON data containing flight information returned by the API.
    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.
    This function initially checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assuming the first
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
     the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
     FlightData object with the details of the most affordable flight.
    """
    
    # Handle empty data if no flight or Amadeus rate limit exceeded
    if flight_data is None or not flight_data['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    # Data from the first flight in the json
    first_flight = flight_data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in flight_data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
    
    """
    # Iterando sobre as ofertas de voos e exibindo os preços
    for offer in flight_data.get('data', []):
        for itinerarie in offer["itineraries"]:
            for segments in itinerarie["segments"]:
                print(segments)

        # Acessando a estrutura de preços dentro das ofertas
        price = offer.get('price', {})
        total = price.get('total')
        currency = price.get('currency')

        # Exibindo informações de preços
        print(f"Preço: {total} {currency}")
        """
