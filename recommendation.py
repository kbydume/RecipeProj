import pandas as pd



class Recommendation:

    def __init__(self, filepath):
        
        """
        Initialize the Recommendation object.

        Args:
            filepath (str): The path to the CSV file containing recipe data.
        """
        
        self.df = pd.read_csv(filepath)

    def get_recommendations(self, keyword):
        
        """
        Get food recommendations based on a keyword.

        Args:
            keyword (str): The keyword to search for in the Ingredients column.

        Returns:
            list: A list of food recommendations.
        """
        
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


