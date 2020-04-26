
# Write a function howManyMedalsByCountry which takes two arguments:
# * a pandas.DataFrame which contains the dataset
# * a country name
# The function returns a dictionary of dictionaries giving the number and type of medal for each competition where the country team earned medals. 
# The keys of the main dictionary are the Olympic games’ years. In each year’s dictionary, the key are ‘G’, ‘S’, ‘B’ corresponding to the type of medals won.
# Duplicated medals per team games should be handled and not counted twice.

def howManyMedalsByCountry(df, team):
    data = df[['Team', 'Year', 'Medal', 'Event']]

    filtered = data[data.Team.eq(team)]
    filtered = filtered.dropna()

    years = filtered.drop_duplicates(subset="Year")[['Year']]
    years = years.Year.values.tolist()

    result = {}
    for x in years:
        year = filtered[filtered.Year.eq(x)]

        value = {
            'G' : year[year.Medal.eq("Gold")].drop_duplicates(subset="Event").shape[0],
            'S' : year[year.Medal.eq("Silver")].drop_duplicates(subset="Event").shape[0],
            'B' : year[year.Medal.eq("Bronze")].drop_duplicates(subset="Event").shape[0]
        }
        result[x] = value

    return result


