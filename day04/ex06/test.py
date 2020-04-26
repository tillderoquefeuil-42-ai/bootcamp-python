from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

fl = FileLoader()

filename = "athlete_events.csv"
df = fl.load(filename)

mpl = MyPlotLib()

mpl.histogram(df, features=['Height', 'Weight'])
mpl.density(df, features=['Weight', 'Height'])
mpl.pair_plot(df, features=['Weight', 'Height'])
mpl.box_plot(df, features=['Weight', 'Height'])
