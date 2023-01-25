
from stsRuns import stsRuns

dDir = r"C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire\runs\DEFECT"
dWins = stsRuns(dDir)

# pass object runs or wins, give a filename for csv
dWins.write_to_csv(dWins.wins, 'dWins')
