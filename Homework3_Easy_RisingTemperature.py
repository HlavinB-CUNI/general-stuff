import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    finalDF = pd.DataFrame(columns=['id', 'temperature', 'recordDate']) # data frame for return data 

    # SORT BY recordDate first, and then proceed with this logic
    weather = weather.sort_values(by=['recordDate'])

    # if the temperature in the next cell down the data frame column for temperature, then add the next cell down to the final list
    if weather.shape[0] > 0:
        for i in range((weather.shape[0])-1):
            difference = abs(weather.iloc[i,1] - weather.iloc[i+1,1])
            if difference.days == 1:
                if weather.iloc[i,2] < weather.iloc[i+1,2]:
                    finalDF = finalDF._append(weather.iloc[i+1], ignore_index=True)
                else:
                    continue
            else:
                continue
        finalDF = finalDF.drop('temperature', axis=1) # getting rid of unnecessary column
        finalDF = finalDF.drop('recordDate', axis=1) # getting rid of unnecessary column
    else: 
        finalDF = finalDF.drop('temperature', axis=1) # getting rid of unnecessary column w/o doing anything else
        finalDF = finalDF.drop('recordDate', axis=1) # getting rid of unnecessary column w/o doing anything else

    return finalDF