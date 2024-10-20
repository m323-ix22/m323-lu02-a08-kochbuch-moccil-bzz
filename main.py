"""
mmy
"""
import json


# Dein Code kommt hier hin
def adjust_recipe(original_recipe, num_people):
    for i in original_recipe["ingredients"]:
        original_recipe["ingredients"][i] = original_recipe["ingredients"][i] / original_recipe["servings"] * num_people
    original_recipe["servings"] = num_people
    return original_recipe

def load_recipe(json_string):
    return json.loads(json_string)


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    print(load_recipe(recipe_json))
