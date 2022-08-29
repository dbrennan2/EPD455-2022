while True:
    try:
        x = int(input("Enter number: "))
        print("Looks good!")
        y = 2*x
        break
    except ValueError:
        print("Try again...")


print("results is:", y)