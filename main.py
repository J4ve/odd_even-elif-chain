# main.py
# Community-powered odd/even checker
# Each contributor adds exactly one elif block for one number

def main():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # Starting chain
    if num == 1:
        print("odd")
    elif num == 2:
        print("even")
    elif num == 3:
        print("odd")
    elif num == 4:
        print("even")

    elif num == 18:
        print("even") #I WAS HERE RAAAH -Kento
    
    elif num == 28:
        print("even") # Birthday ko yan -Elmo
    # Add more xdddd

    else:
        print("Number not yet supported. Contribute to add it!")

if __name__ == "__main__":
    main()


