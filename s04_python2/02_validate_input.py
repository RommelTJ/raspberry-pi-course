if __name__ == "__main__":
    number_string = input("Please enter a number between 1 and 100: ")
    try:
        number = int(number_string)
        if number > 1 and number < 100:
            print("Valid number")
        else:
            print("Invalid number")
            exit()
    except ValueError:
        print("Invalid number")
        exit()
