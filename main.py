from todo_list import todo_list
from currency_converter import currency_converter

from password_generator import password_generator

import weather_forecast

print("Welcome to MY DailyTools!")
while True:
    print("\nSelect a program:")
    print("1. TODO list")
    print("2. Currency Converter")
    print("3. Password Generator")
    print("4. Weather Forecast")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        todo_list()
    elif choice == "2":
        currency_converter()
    elif choice == "3":
        password_generator()
    elif choice == "4":
        weather_forecast.main()
    elif choice == "5":
        print("Thank you for using MY DailyTools!")
        break

    else:
        print("Invalid choice. Please try again.")  

