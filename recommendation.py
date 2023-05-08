import pandas as pd
import re


class Recommendation:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def get_recommendations(self, keyword):
        # Find the top 5 items in the Ingredients column that contain the keyword
        ingredient_matches = self.df[self.df['Ingredients'].str.contains(keyword)]
        if len(ingredient_matches) == 0:
            return [f"Sorry, we do not have any options with '{keyword}' as an ingredient."]
        else:
            top_5_ingredients = ingredient_matches['Ingredients'].value_counts().head(5).index.tolist()

            # Get the corresponding name in the Title column for each of the top 5 ingredients
            ingredient_titles = self.df[self.df['Ingredients'].isin(top_5_ingredients)]['Title'].tolist()

            # Return the food recommendations
            return [f"- {title}" for title in ingredient_titles]


