class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"


class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Recipe: {self.name}\nIngredients: {', '.join([str(ingredient) for ingredient in self.ingredients])}\nInstructions: {self.instructions}"


class Bakery:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def find_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name == recipe_name:
                return recipe
        return None

    def make_recipe(self, recipe_name):
        recipe = self.find_recipe(recipe_name)
        if recipe:
            print(f"Making {recipe_name}...")
            for ingredient in recipe.ingredients:
                print(f"Using {ingredient}")
            print(f"Follow these instructions:\n{recipe.instructions}")
        else:
            print(f"Recipe '{recipe_name}' not found in the bakery!")


# Example usage:

# Create some ingredients
flour = Ingredient("Flour", 2, "cups")
sugar = Ingredient("Sugar", 1, "cup")
eggs = Ingredient("Eggs", 3, "units")
butter = Ingredient("Butter", 1, "cup")

# Create a recipe
chocolate_chip_cookies = Recipe(
    "Chocolate Chip Cookies",
    [flour, sugar, eggs, butter],
    "1. Preheat the oven to 350°F.\n2. Mix all ingredients together.\n3. Bake for 10-12 minutes."
)

# Create a bakery
my_bakery = Bakery()

# Add the recipe to the bakery
my_bakery.add_recipe(chocolate_chip_cookies)

# Make the recipe
my_bakery.make_recipe("Chocolate Chip Cookies")