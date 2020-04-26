
# Write a class called SpatioTemporalData which takes a dataset (pandas DataFrame) as argument in its
# constructor and implements the following methods:
# • when(location) : This method takes a location as an argument and returns a list containing the years where games were held in the given location.
# • where(date) : This method takes a date as an argument and returns the location where the Olympics took place in the given year.
class SpatioTemporalData():
    def __init__(self, df):
        self.df = df

    def when(self, location):
        data = self.df[['Year', 'City']]
        filtered = data[data.City.eq(location)]
        filtered = filtered.drop_duplicates(subset="Year")
        result = filtered.Year.values.tolist()
        return result


    def where(self, date):
        data = self.df[['Year', 'City']]
        filtered = data[data.Year.eq(date)]
        filtered = filtered.drop_duplicates(subset="City")
        result = filtered.City.values.tolist()

        return result
