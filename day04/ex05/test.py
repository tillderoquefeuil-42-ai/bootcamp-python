from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

print(howManyMedalsByCountry(df, 'China'))