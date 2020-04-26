from FileLoader import FileLoader
from Komparator import Komparator

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

k = Komparator(df)

k.compare_box_plots("Sex", "Height")
k.density("Sex", "Height")
k.compare_histograms("Sex", "Height", False)
k.compare_histograms("Sex", "Height", True)
