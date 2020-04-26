from FileLoader import FileLoader
from HowManyMedals import howManyMedals

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

print(howManyMedals(df, 'Kjetil Andr Aamodt'))
# expected output
# {
#   1992: {'G': 1, 'S': 0, 'B': 1}, 
#   1994: {'G': 0, 'S': 2, 'B': 1}, 
#   1998: {'G': 0, 'S': 0, 'B': 0}, 
#   2002: {'G': 2, 'S': 0, 'B': 0}, 
#   2006: {'G': 1, 'S': 0, 'B': 0}
# }