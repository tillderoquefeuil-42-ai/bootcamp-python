
# Write a function proportionBySport which takes four arguments: - a pandas.DataFrame of the dataset
# - an olympic year
# - a sport
# - a gender
# The function returns a float corresponding to the proportion (percentage) of participants 
# who played the given sport among the participants of the given gender.
# Hint: here and further, if needed, drop duplicated sportspeople to count only unique ones. 
# Beware to call the dropping function at the right moment and with the right parameters, in order not to omit any individuals

def proportionBySport(df, year, sport, gender):
    data = df[['Name', 'Sex', 'Sport', 'Year']]
    filtered = data[data.Year.eq(year) & data.Sex.eq(gender)]
    filtered = filtered.drop_duplicates(subset="Name")     
    total = filtered.shape[0]

    filteredBySport = filtered[filtered.Sport.eq(sport)]
    sportProp = filteredBySport.shape[0]

    return sportProp / total
