
from stsRuns import stsRuns

# C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD
icDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD"
tsDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\THE_SILENT"
dDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DEFECT"
twDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\WATCHER"

dWins = stsRuns(dDir)
# return_wins supports 3 optional arguments: decks, relics, and allData
# The following example returns decks and relics
dWins.return_wins(True, True)



