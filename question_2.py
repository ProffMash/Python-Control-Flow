def ask_for_input():
    while True:
        user_input = input("Enter a word (type 'exit' to stop): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        print("You entered:", user_input)

ask_for_input()
