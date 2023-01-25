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
    
    def write_to_csv(self):
        # open the file in the write mode
        with open('csv_file.csv', 'w+', newline='') as f:
            # create the csv writer
            i = 0
            #master headers list
            csv_columns = ["gold_per_floor","floor_reached","playtime","items_purged","score","play_id","local_time","is_ascension_mode","campfire_choices","neow_cost","seed_source_timestamp","circlet_count","master_deck","relics","potions_floor_usage","damage_taken","seed_played","potions_obtained","is_trial","path_per_floor","character_chosen","items_purchased","campfire_rested","item_purchase_floors","current_hp_per_floor","gold","neow_bonus","is_prod","is_daily","chose_seed","campfire_upgraded","win_rate","timestamp","path_taken","build_version","purchased_purges","victory","max_hp_per_floor","card_choices","player_experience","relics_obtained","event_choices","is_beta","boss_relics","items_purged_floors","is_endless","potions_floor_spawned","killed_by","ascension_level","special_seed"]
            # for row in self.runs:
            #     if i == 0:
            #         csv_columns.extend(row.keys())
            #         # print(csv_columns)
            #         i = 1
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for row in (self.runs):
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