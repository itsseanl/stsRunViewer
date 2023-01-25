
from stsRuns import stsRuns

# C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD
icDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD"
tsDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\THE_SILENT"
dDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DEFECT"
twDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\WATCHER"

dWins = stsRuns(dDir)
dWins.return_wins(True, True)



