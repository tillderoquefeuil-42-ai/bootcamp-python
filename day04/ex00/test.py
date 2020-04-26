from FileLoader import FileLoader

fl = FileLoader()

filename = "good.csv"
df = fl.load(filename)
# print(df)

fl.display(df, 5)
fl.display(df, -5)