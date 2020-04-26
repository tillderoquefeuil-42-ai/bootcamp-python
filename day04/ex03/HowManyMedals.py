
# Write a function howManyMedals which takes two arguments: 
# * a pandas.DataFrame which contains the dataset
# * a participant name
# The function returns a dictionary of dictionaries giving the number and type of medals for each year during which the participant won medals. 
# The keys of the main dictionary are the Olympic games years. In each year’s dictionary, the keys are ‘G’, ‘S’, ‘B’ corresponding to the type of medals won (gold, silver, bronze). 
# The innermost values correspond to the number of medals of a given type won for a given year.
def howManyMedals(df, name):
    data = df[['Name', 'Year', 'Medal']]

    filtered = data[data.Name.eq(name)]
    filtered = filtered.dropna()

    years = filtered.drop_duplicates(subset="Year")[['Year']]
    years = years.Year.values.tolist()

    result = {}
    for x in years:
        # print(x)
        year = filtered[filtered.Year.eq(x)]
        value = {
            'G' : year[year.Medal.eq("Gold")].shape[0],
            'S' : year[year.Medal.eq("Silver")].shape[0],
            'B' : year[year.Medal.eq("Bronze")].shape[0]
        }
        result[x] = value

    return result


