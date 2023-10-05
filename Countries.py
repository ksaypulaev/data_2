import numpy as np
import pandas as pd
import json as js


path = "/Users/ksaypulaev/Desktop/utility/prog/python/data/countries.json"

class Countries:
    def __init__(self):
        self.country_list = np.array([[1, "USSR", 400000000], [2, "USA", 200000000], 
                                [3, "France", 20000000], [4, "Spain", 15000000]])
        print(self.country_list)

        '''self.json_object = js.dumps(self.country_list)
        with open(path, "w") as self.json_file:
            self.json_file'''
        
        input()

cn = Countries()