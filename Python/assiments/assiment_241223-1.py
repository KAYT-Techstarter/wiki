fried_egg = ["Egg", "Salt", "Paprika", "Pepper"]
vegetable_stir_fry = ["Bell Pepper", "Zucchini", "Carrot", "Onion", "Garlic", "Olive Oil"]
pasta_with_pesto = ["Pasta", "Pesto", "Parmesan", "Pine Nuts"]


recipes = {
    "Fried Egg": fried_egg,
    "Vegetable Stir Fry": vegetable_stir_fry,
    "Pasta with Pesto": pasta_with_pesto,
}

def main_program():
    print("Welcome to the Recipe Selection Program!")
    print("The following recipes are available:")

    for recipe in recipes:
        print(recipe)

    selection = input("Please enter the name of the recipe you want to see: ")

    # Check if the entered recipe exists in the recipes dictionary
    if selection in recipes:
        print(f"The ingredients for {selection} are:")
        for ingredient in recipes[selection]:
            print(f"- {ingredient}")
    else:
        print("This recipe is not available. Please try again.")

main_program()