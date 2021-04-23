from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from config import owm_key

owm = OWM(owm_key)
mgr = owm.weather_manager()

# info on looking up cities.
#To make it more precise put the city's name, comma, 2-letter country code (ISO3166). You will get all proper cities in chosen country.
#The order is important - the first is city name then comma then country. Example - London, GB or New York, US.

city = 'Leesburg,US'
short_city = city.split(",", 1)[0]

# Creating an empty "database" or dictionary.
# I'm using this to train myself in dictionaries and how to read them.
database = {}

# Searching location for data on owm
location = mgr.weather_at_place(city)
w = location.weather

# Create key + value
database['wind'] = w.wind()
database['temp'] = w.temperature('fahrenheit')

# printing out the default looking dictionary
print(database)

# Print out the status of the dictionary
print(f"Wind Speed for {city} : {database['wind']['speed']}")

# Printing out the temp instead
print(f"Temp for {short_city} = {database['temp']['temp']}")
print(f"The high for today in {short_city} is, {database['temp']['temp_max']}")