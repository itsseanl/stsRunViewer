import json 
import os

# stsRuns class takes the directory of slay the spire .run files as an argument on instantiation
# ex: r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD"
class stsRuns:
    def __init__(self, dir):
        self.dir = dir
        self.runs = []
        self.wins = []
         # retrieve list of run files
        runs = os.listdir(dir)
        # loop through run files, find wins
        for run in runs:
            file = dir + "\\" + run
            # open file
            with open(file) as user_file:
                file_contents = user_file.read()    
                # parse JSON into dict
                parsed_json = json.loads(file_contents)
                (self.runs).append(parsed_json)
                # if win, add to self.wins
                if (parsed_json["victory"] and parsed_json["victory"] == True):
                    (self.wins).append(parsed_json)  

    # returns wins
    def return_wins(self, deck=None, relics=None, allData=None):
        if (deck):
            for win in self.wins:
                print("winning deck: ")
                print(win["master_deck"])
        if (relics):
            for win in self.wins:
                print("winning relic: ")
                print(win["relics"])
        if (allData):
            print(self.wins)