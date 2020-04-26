from FileLoader import FileLoader
from ProportionBySport import proportionBySport

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

print(proportionBySport(df, 2004, 'Tennis', 'F'))
# expected output
# 0.01935634328358209