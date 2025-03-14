import requests

# JokeAPI: https://v2.jokeapi.dev/
# 1. Random Joke: https://v2.jokeapi.dev/joke/Any
# 2. Programming Joke: https://v2.jokeapi.dev/joke/Programming
# 3. Miscellaneous Joke: https://v2.jokeapi.dev/joke/Miscellaneous

def get_random_joke():
    #Fetch a random joke.
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)#this will send the request and the response is stored in response variable
    if response.status_code == 200:#converts into python dictionary
        data = response.json()#checks if request was successful
        if data['type'] == 'single':
            print(f"Joke: {data['joke']}")
        else:
            print(f"Setup: {data['setup']}")
            print(f"Delivery: {data['delivery']}")
    else:
        print("Error fetching joke.")

def get_programming_joke():
    #Fetch a programming joke.
    url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(url)#similar code to the first thing but uses of different area of API
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            print(f"Joke: {data['joke']}")
        else:
            print(f"Setup: {data['setup']}")
            print(f"Delivery: {data['delivery']}")
    else:
        print("Error fetching joke.")

def get_miscellaneous_joke():
    #Fetch a miscellaneous joke.
    url = "https://v2.jokeapi.dev/joke/Miscellaneous"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            print(f"Joke: {data['joke']}")
        else:
            print(f"Setup: {data['setup']}")
            print(f"Delivery: {data['delivery']}")
    else:
        print("Error fetching joke.")

def menu():
    #Menu for selecting different types of jokes.
    while True:
        print("\nJoke App Menu:")
        print("1. Get Random Joke")
        print("2. Get Programming Joke")
        print("3. Get Miscellaneous Joke")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            get_random_joke()
        elif choice == '2':
            get_programming_joke()
        elif choice == '3':
            get_miscellaneous_joke()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice, try again.")

# Run the menu
menu()
