while True:
    try:
        x = int(input("Enter number: "))
        print("Looks good!")
        break
    except ValueError:
        print("Try again...")