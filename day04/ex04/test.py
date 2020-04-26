from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

sp = SpatioTemporalData(df)
print(sp.where(1896))
# expected output
# ['Athina']
print(sp.where(2016))
# expected output
# ['Rio de Janeiro']
print(sp.when('Athina'))
# expected output
# [2004, 1906, 1896]
print(sp.when('Paris'))
# expected output
# [1900, 1924]
