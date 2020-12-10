#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
A simple fun pokedex that shows pokemon statistics
Two helper function
first will take the name of the pokemon
that will show the stat and the chart
Upcoming feature: Showing picture with stat
"""

def main():
    def get_pokemon(name):
        """
        input: pokemon name
        returns chart and stat
        """
        def show_stat(name, series):
            columns = ["HP","Attack","Defense","Sp. Atk", "Sp. Def","Speed"]
            series = series.transpose()[columns]
            series.plot(kind="barh")
            plt.title(name.capitalize())
            plt.xlabel("value")
            plt.show()
        try:
            pokemon = df.loc[name]
            show_stat(name, pokemon)
        except KeyError:
            pokemon = "Sorry couldn't find this pokemon! Check the spelling"
        return pokemon
    def search():
        """
        input: user input, sanitize it
        checks if the input is 0 if not then process it for getting stat
        """
        pokemon = input("Enter the pokemon name you want to search and 0 to quit: ").lower()
        if pokemon == "0": return 1
        else:
            pokemon = get_pokemon(pokemon)
        print(pokemon)
        return 0
    """
    main program
    load the main database, creates a infinite loop with break character and then process it further
    """
    try:
        global df
        df = pd.read_csv("pokemon.csv")
        df.drop(["#"], inplace =True, axis = 1)

        df["Name"] = df["Name"].str.lower()
        df.set_index("Name", inplace = True)

        while True:
            response = search()
            if response == 1: break
            else:
                print("\n")
    except FileNotFoundError:
        print("Database doesn't exist, please check required pokemon.csv file or download one")
    except Exception as e:
        print(e)
    finally:
        print("Program will exit now")








main()







