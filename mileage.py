print("How many kilometers did you cycle today?") # initial line
kms = input() # asks user to put in an input, gets a string
miles = float(kms)/1.60934 # need to change input from string to a float to be divided into miles
miles = round(miles, 2) # round(num, num of dec places you want)
print(f"That is equal to {miles} miles") # interpolation