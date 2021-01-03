#Import requests, json, and time to use throughout the program.
import requests
import json
import time

print("Program starting...")
time.sleep(0.5)

print("""
****WELCOME TO THE WEATHER PROGRAM***
""")

time.sleep(0.5)
#Use a function to get the data
def weather_data(base_url, api_key):

    city_name = input("Enter city name: ")
    zip_code = input("Enter zip code (Leave blank to skip): ")

    quit = False
    #While loop to loop through the weather program until the user wants to stop.
    while quit == False:
      #Try block to make sure the code is running smoothly.
      try:
        complete_url = base_url + city_name + ','+ zip_code + "&appid=" + api_key
        #use requests to get data from the website.
        response = requests.get(complete_url)
        #use json to make the data readable to the user.
        w_data = response.json()

        description = w_data['weather'][0]['description']
        humidity = w_data['main']['humidity']
        wind = w_data['wind']['speed']
        #we need to convert kelvin to fahrenheit.
        temp = (w_data['main']['temp'] - 273.15) * (9/5) + 32
        temp_min = (w_data['main']['temp_min'] - 273.15) * (9/5) + 32
        temp_max = (w_data['main']['temp_max'] - 273.15) * (9/5) + 32
        feels_like = (w_data['main']['feels_like'] - 273.15) * (9/5) + 32

        print("\n")
        print("Loading your weather data...\n")

        time.sleep(.75)

        print("---------------------------")
        print("Today's Forecast for {}".format(city_name))
        print("---------------------------\n")
        print("Day:\t\t{}".format(description))
        print("Temp now:\t{}".format(round(temp,1)))
        print("Humidity:\t{}".format(humidity))
        print("Temp low:\t{}".format(round(temp_min,1)))
        print("Temp high:\t{}".format(round(temp_max,1)))
        print("Wind:\t\t{}mph".format(wind))
        print("Feels like:\t{}".format(round(feels_like,1)))
      #exception key if the data was not found.
      except KeyError:
        print('Sorry. The weather data was not found for the info you entered.')
      #exception key if something went wrong with the program.
      except Exception:
        print('Sorry. Something went wrong.')

      user_input = input("Would you like to try again? (Y|N) ")
      #if elif else statement to see if the user wants to use the program again or if the user entered invalid data.
      if user_input.upper() == 'Y':
        city_name = input("Enter city: ")
        zip_code = input("Enter zip code: ")
      elif user_input.upper() == 'N':
        print("Program exiting...")
        time.sleep(.75)
        print("See you next time!")
        quit = True
      else:
        print("Invalid input")
        city_name = input("Enter city: ")
        zip_code = input("Enter zip code: ")
#use of the main function to execute the weather_data function.
def main():
    api_key = '55592219da64379c5a1872dccb250590'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

    weather_data(base_url, api_key)
#if statement to use the main function.
if __name__ == "__main__":
    main()