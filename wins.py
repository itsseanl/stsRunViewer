
from stsRuns import stsRuns

# C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD
icDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\IRONCLAD"
tsDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\THE_SILENT"
dDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DEFECT"
twDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\WATCHER"


# run list_wins function
icWins = stsRuns(icDir)
icWins.return_wins(True, True)




