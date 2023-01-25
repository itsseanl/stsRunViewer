
from stsRuns import stsRuns

dDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DEFECT"
dWins = stsRuns(dDir)
dWins.write_to_csv()