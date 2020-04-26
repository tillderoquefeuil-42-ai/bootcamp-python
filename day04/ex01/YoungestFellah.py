
# Write a function youngestFellah which takes two arguments:
# * a pandas.DataFrame which contains the dataset
# * an Olympic year The function returns a dictionary containing the age of the youngest woman and man
# who took part in the Olympics on that year. 
# The name of the dictionary’s keys is up to you, but it must be self-explanatory.
def youngestFellah(df, year):
    data = df[['Sex', 'Age', 'Year']]
    filteredByYear = data[data.Year.eq(year)]
    
    men = filteredByYear[filteredByYear.Sex.eq("M")]
    women = filteredByYear[filteredByYear.Sex.eq("F")]

    return {
        'f': women.min().Age,
        'm': men.min().Age
    }


