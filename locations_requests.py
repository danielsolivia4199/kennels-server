LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    return LOCATIONS

#Function with a single parameter
def get_single_location(id):
  #Variable to hold the found locations, if it exists
  requested_location = None
  
  # Iterate the LOCATIONS list above. Very similar to the for ...of loops in JS
  for location in LOCATIONS:
    #dictionaries in python use [] notation to find a key instead of the dot notation in JS
    if location["id"] == id:
        requested_location = location
        
  return requested_location
    
