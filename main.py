# Lets promt the iser for the file name at thye beggining
filename = input("What is your file name? ")

# Then we will prompt the user for their name, street address, and phone number
name = input("Enter your name: ")
street_address = input("Enter your street address: ")
phone_number = input("Enter your phone number: ")

# We will follow up by writing the user's information to the file
with open(filename, 'w') as file:
    file.write(f"{name},{street_address},{phone_number}")

# Now we read the file and display the contents
with open(filename, 'r') as file:
    contents = file.read()
    print(contents)