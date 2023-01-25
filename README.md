# stsRunViewer

A simple python library for interacting with locally stored Slay The Spire Run History data

## stsRuns Class

The stsRuns Class takes the directory of run history files as an argument on object instantiation. Exact location depends on where your steam library is saved on your system, but should be something like:
C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD"

###  return_wins

This method prints information from winning runs. Optional parameters are deck, relics, and allData. Passing a value of true for decks will return all winning decks, with card descriptions. Relics does the same for relics. allData will return the all raw run history. 

the .run files do not include card or relic descriptions, so there are two helper functions which append that data from relics.json and cards.json. There are placeholder values in the descriptons currently which I need to map actual values to. The meaning behind these placeholders is described in card_description_explainer.py

### write_to_csv

This method saves the passed run data to a CSV. Currently supports passing either all run data, or just winning data.