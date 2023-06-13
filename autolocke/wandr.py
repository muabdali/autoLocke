import pandas as pd
"""
gen1 to 5 use the "self.Gen3TableData".
the coloumns and rows go in order of 

0 - Normal, 1 - Fire, 2 - Water, 3 - Electric, 4 - Grass, 5 - Ice, 6 - Fighting, 7 - Poison, 8 - Ground, 9 - Flying, 10 - Psychic
11 - Bug,12 - Rock, 13 - Ghost,14 - Dragon,15 -Dark, 16 - Steel



"""




class wandr():
    def __init__(self):
        self.Gen3TableData = ('autolocke/Data/1to5.csv')
        
        
    def multiplier(self):
        data = pd.read_csv(self.Gen3TableData)
        df = pd.DataFrame(data)
        print(df)



tf = wandr()
tf.multiplier()