from FileLoader import FileLoader
from YoungestFellah import youngestFellah

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

print(youngestFellah(df, 2004))
# expected output
# {'f': 13.0, 'm': 14.0}