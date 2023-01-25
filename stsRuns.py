import json 
import os
import csv

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
    
    def write_to_csv(self, dataToWrite, fileName):
        # open the file in the write mode
        with open(fileName+'.csv', 'w+', newline='') as f:
            #master headers list
            csv_columns = []
            print(dataToWrite)
            for row in dataToWrite:
                for key in row.keys():
                    if(key not in csv_columns):
                        csv_columns.append(key)
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for row in (dataToWrite):
                # write row to the csv file
                writer.writerow(row)
               
    # returns wins
    def return_wins(self, deck=None, relics=None, allData=None):
            for win in self.wins:
                if (deck):
                    print("winning deck: ")
                    self.return_deck(win["master_deck"])
                if (relics):
                        print("winning relics: ")
                        self.return_relics(win["relics"])
                if (allData):
                    print(self.wins)
   
    # return deck with card desciptions
    def return_deck(self, deck):
        deck_descriptions = []
        with open("./cards.json", "r") as cards_list:
            file_contents = cards_list.read()
            master_cards = json.loads(file_contents)
        for card in deck:
            for k, v in master_cards.items():
                if (card.__contains__(k)):
                    deck_descriptions.append({'name': card, 'description': v["DESCRIPTION"] })
        print(deck_descriptions)
    
    #return relics with descriptions
    def return_relics(self, relics):
        relics_descriptions = []
        with open("./relics.json", "r") as relic_list:
            file_contents = relic_list.read()
            master_relics = json.loads(file_contents)
        for relic in relics:
            for k, v in master_relics.items():
                if (relic == k):
                    s = " "
                    relics_descriptions.append({'name': k, 'description': s.join(v["DESCRIPTIONS"]) })
        print(relics_descriptions)