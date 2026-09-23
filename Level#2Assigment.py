#using upper
trip_questions = input("Are you planning a road trip? (Y/N): ").upper()

#road trip planner
traveler_name = input("What is your name?: ")

#Destination
destination_name = input("Where are you going?: ")

#One-way Distance in miles
one_way_distance = float(input("How many miles is the one-way trip?: "))

#Vehicle miles per gallon
vehicle_miles_per_gallon = float(input("How many miles to the gallon does your vehicle get?: "))

#Gas price per gallon
gas_price_per_gallon = float(input("How much does gas cost per gallon?: "))

#number of travelers
number_of_travelers = int(input("How many people will be traveling?: "))


#calculations
total_distance = one_way_distance * 2
total_gallons_needed = total_distance / vehicle_miles_per_gallon
estimated_gas_cost = total_gallons_needed * gas_price_per_gallon
estimated_gas_cost_per_person = estimated_gas_cost / number_of_travelers

#decorative line
print("\n*" + "*" * 50)

#Trip Summary
print("\nTrip Summary:")

print("\nTraveler: " + traveler_name)
print("Destination: " + destination_name)
print("Estimated Gas Cost: $" + str(estimated_gas_cost))
print("Estimated Gas Cost per Person: $" + str(estimated_gas_cost_per_person))

print(f"\n{traveler_name} is planning a road trip to {destination_name}. The total distance for the round trip is {total_distance} miles. \nThe estimated gas cost for the entire trip is ${estimated_gas_cost:.2f}, which comes out to ${estimated_gas_cost_per_person:.2f} per person for {number_of_travelers} travelers.")

#decorative line
print("\n*" + "*" * 50)