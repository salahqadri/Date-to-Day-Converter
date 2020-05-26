import calendar

#Dictionary that convert number value of days to day names
dayConversions = {
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "3": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday",
}
#User input being taken for the date
userInput = input("What is the date?(dd/mm/yyyy)")
#User input is split by / to separate day, month and year values
userInput = userInput.split("/")
#User input is used to find the weekday number value
weekday = calendar.weekday(int(userInput[2]), int(userInput[1]), int(userInput[0]))
#Weekday is converted to day name from number
weekday = dayConversions[str(weekday)]
#Final result is printed
print("It's " + str(weekday) + " today!")