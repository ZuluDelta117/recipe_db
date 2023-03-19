import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



def initialize_firsestore():
    """
    Create database connection
    """

    cred = credentials.Certificate("recipe-2a811-firebase-adminsdk-y0kav-f9dd2bd7f9.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db


def add_new_recipe(db, type):
    """"
    Allows user to add a new recipie folder into database
    """

    name = input("Recipe Name: ")
    name = name.title()
    print()

    # Get the database information
    result = db.collection(type).document(name).get()

    # Make sure recipie does not already exist
    if result.exists:
        print("Recipe already exists")
        return

    finished = input("Would you like to add any ingredients? (Y/N) ")
    finished = finished.upper()



    data = {}
    while finished == "Y":

        ingredient = input("Ingredient: ")
        ingredient = ingredient.title()
        qty = input("Ingredient Quantity: ")

        # Add ingredient to dictonary
        data[ingredient] = qty

        print()
        finished = input("Would you like to add any ingredients? (Y/N) ")
        finished = finished.upper()
        

    # Update database
    db.collection(type).document(name).set(data)
        

    print(f"You have added {name} to your database!")


def add_ingredients(db, type):
    """
    Add ingredients to existing recipe
    """

    name = input("Recipe Name: ")
    name = name.title()
    print()

    # Get the database information
    result = db.collection(type).document(name).get()

    # Make sure recipie does exist
    if not result.exists:
        print("Recipe does not exists")
        return
    
    


    finished = "Y"

    # Convert database to a dictionary
    data = result.to_dict()
    
    while finished == "Y":

        ingredient = input("Ingredient: ")
        ingredient = ingredient.title()
        qty = input("Ingredient Quantity: ")

        # Add ingredient to dictionary
        data[ingredient] = qty

        print()
        finished = input("Would you like to add another ingredient? (Y/N) ")
        finished = finished.upper()

    # Update database
    db.collection(type).document(name).set(data)

    print(f"You have added ingredients to {name} in your database!")


def remove_ingredient(db, type):
    """
    Remove ingredients from recipe
    """

    name = input("Recipe Name: ")
    name = name.title()
    print()

    # Get the database information
    result = db.collection(type).document(name).get()

    # Make sure recipie does exist
    if not result.exists:
        print("Recipe does not exists")
        return
    
    # Convert database to a dictionary
    data = result.to_dict()
    
    ingredient = input("What ingredient would you like to remove: ")
    ingredient = ingredient.title()

    # Remove ingredient from dictonary
    del data[ingredient]

    # Update database
    db.collection(type).document(name).set(data)

    print(f"You removed {ingredient} from {name}.")


def search_recipes(db, type):
    """
    Search recipies
    """
    name = None

    # Find out what recipe(s) the user whats to view
    print("Select Query")
    print("1) Show all recipes")
    print("2) Show certain recipe")
    # print("3) Show recipies by ingredient")
    choice = input("> ")
    print()

    # Query what user wants
    if choice == "1":
        results = db.collection(type).get()
    elif choice == "2":
        name = input("Recipe Name: ")
        name = name.title()
        results = db.collection(type).document(name).get()
    # TODO: Adjust Database to be able to search by ingredient
    # elif choice == "3":
    #     ingredient = input("Ingredient: ")
    #     ingredient = ingredient.title()
    #     results = db.collection(type).where(type, 'array_contains', ingredient).get()
    else:
        print("Invalid selection")
        return
    
    print("")
    print("Search Results")
    # Display results based on user input
    if choice == "2":
        data = results.to_dict()
        print(f"\n{name}")
        for key in data:
            print(f"{key}: {data[key]}")
    else:
        for result in results:
            data = result.to_dict()
            print(f"\n{result.id}")
            print("-------------------")
            for key in data:
                print(f"{key}: {data[key]}")


def main():
    db = initialize_firsestore()
    choice = None
    
    # Find out what type the user wants to look at
    print("\nRecipe types:")
    print("Breakfast")
    print("Desserts")
    print("Recipe")
    print("Soup")
    print()
    type = input("What is your recipie type? ")
    type = type.title()

    while choice != "0":
        # Get user input on what they want to do with database
        print()
        print("0) Exit")
        print("1) Add New Recipe")
        print("2) Add or Adjust Ingredient")
        print("3) Remove Ingredient")
        print("4) Search Recipes")
        print("5) Change Recipe Type")
        choice = input("> ")


        # Change or display database based on user input
        if choice == "1":
            add_new_recipe(db, type)
        elif choice == "2":
            add_ingredients(db, type)
        elif choice == "3":
            remove_ingredient(db, type)
        elif choice == "4":
            search_recipes(db, type)
        elif choice == "5":
            print("\nRecipe types:")
            print("Breakfast")
            print("Desserts")
            print("Recipe")
            print("Soup")
            print()
            type = input("What is your new recipie type? ")
            type = type.title()
        


if __name__ == "__main__":
    main()
