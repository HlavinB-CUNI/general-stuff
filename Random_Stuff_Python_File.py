import seaborn as sns
import matplotlib.pyplot as mp
import pandas as pd
import zipfile
import numpy as np
import datetime

idx = pd.IndexSlice
plotconfig = {
    'style':'.',
    'grid':True,
    'markersize':5,
    'figsize':(10,4)
}

#sample 5 rows randomly
#df.sample(5).style

with zipfile.ZipFile("data/covid.zip") as z:
    with z.open("Covid data/CovidDeaths.csv") as f:
        covid = pd.read_csv(f, index_col=["iso_code", "date"], parse_dates=["date"], date_parser=lambda d: pd.to_datetime(d, format="%d-%m-%y"))
        # covid = pd.read_csv(f, index_col=["iso_code", "date"], parse_dates=["date"], date_format="%d-%m-%y")

        country_columns = ["continent", "location", "population"]
        countries = covid.groupby("iso_code").apply(
            lambda g: g.iloc[0][country_columns]
        )

        countries = countries[countries.apply(lambda row: len(row.name) == 3, axis=1)]
        countries.continent = countries.continent.astype("category")

        keep_covid_columns = [
            "new_cases",
            "new_deaths",
            "icu_patients",
            "hosp_patients",
        ]
        
        #LENGTH OF CSV
        print(len(list(covid)))
            
            

        covid = covid[keep_covid_columns]
        covid = covid[covid.apply(lambda row: len(row.name[0]) == 3, axis=1)]

        covid = covid.sort_index()

        covid = covid.reset_index()

countries = countries
czech_cases = covid.loc[covid['iso_code'] == 'CZE'].set_index('date')
slovak_cases = covid.loc[covid['iso_code'] == 'SVK'].set_index('date')

# ax is the axis object, which is used to plot multiple lines on the same plot
ax = czech_cases.plot(color="lightgrey", label="other values", legend=True, **plotconfig)

czech_cases.loc[
    (czech_cases["new_cases"] >= 5000) & (czech_cases["new_cases"] < 15000), "new_cases"
].plot(ax=ax, label="Values between 500 and 750", legend=True, **plotconfig)

czech_cases.loc[
    czech_cases.index.weekday == 6, "new_cases"
].plot(ax=ax, label="Sunday", legend=True, **plotconfig)

czech_cases.loc[czech_cases.index.weekday == 5, "new_cases"].plot(ax=ax, label="Saturday", legend=True, **plotconfig)