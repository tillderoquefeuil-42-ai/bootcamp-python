import pandas as pd
import os

class FileLoader():

    # The argument of this method is the file path of the dataset to load. 
    # It must display a message specifying the dimensions of the dataset (e.g. 340 x 500). 
    # The method returns the dataset loaded as a pandas.DataFrame.
    def load(self, path):
        if not os.path.exists(path) or not os.path.isfile(path):
            return None
        df = pd.read_csv(path)

        print("Loading dataset of dimensions {size[0]} x {size[1]}".format(size=df.shape))
        return df

    # Takes a pandas.DataFrame and an integer as arguments. 
    # This method displays the first n rows of the dataset if n is positive, or the last n rows if n is negative.
    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(abs(n)))
