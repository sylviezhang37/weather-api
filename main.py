from api import is_valid_country_code, weather

def main():
    while True:
        zipcode = input("Please enter your zipcode: ")
        checkEndProgram(zipcode)
        country = input("Enter two-letter country code, or hit ENTER to search in the US: ")
        checkEndProgram(country)
        if not is_valid_country_code(country) and country != '':
            print("You've entered an invalid country code. Try again.")
            continue

        if weather(zipcode, country):
            break
        else:
            print("Please try again, or enter \'end\' at any time to stop the program.")
    print("Have a nice day :)")

def checkEndProgram(input):
    if (input.lower() == 'end'):
        exit()

if __name__ == "__main__":
    main()