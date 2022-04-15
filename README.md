# :surfer: surfs_up
Module 9 - SQLite &amp; SQLAlchemy &amp; Flask</br>
</br>
Describe the key differences in weather between June and December for the island of Oahu and make two recommendations for further analysis.

## :one: Overview
The goal of this analysis is to investigate temperature variations on the Hawaiian island of Oahu in order to determine the viability of a business that combines the sale of surfing products with the sale of milkshakes and ice cream. Surf 'n Shake will be the name of the store. The data will be used to persuade local investors to join forces in the creation of this business.

Mr. W. Avy, the lead investor, provided us with a flat database in sqlite format containing temperature data recorded by several weather observation stations located at various points throughout the Hawaiian Islands from 2010 to 2017. Following a meeting with Mr. W. Avy, it was decided to limit the analysis to the months of June and December and to the island of Oahu as the starting point for a potential Surf 'n Shake business chain.

Mr. W. Avy wants to know if the temperature will be high enough during those two months to keep the flow of tourists strong and the business profitable.  In theory, if the temperature makes Oahu attractive for tourists during the hottest month (June) and the coldest month (December), there should be enough customers to make the business profitable throughout the year.

## :two: Results
The SQLite database recieved from W. Avy contains two tables: `measurement` and `station`.  The `measurement` table has `19550 records`, which were filtered using code to focus only on the records from the months of June and December of each year.  The table `station` contains only `9 records`, corresponding to the data of the weather stations located in the Hawaiian archipielago.

Code for extracting the temperatures for the month of June.

```
# 1. Import the sqlalchemy extract function.
from sqlalchemy import extract

# 2. Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
june_results = session.query(Measurement.date, Measurement.tobs).\
    filter(extract('month', Measurement.date)==6)
print(june_results)
```

Similarly, below is the code used for filtering the information for the month of December.

```
# 6. Write a query that filters the Measurement table to retrieve the temperatures for the month of December.
december_results = session.query(Measurement.date, Measurement.tobs).\
    filter(extract('month', Measurement.date)==12)
print(december_results)
```

### Image 1: Screenshot of the `measurement` table without any filters
![Image1](https://github.com/Peteresis/surfs_up/blob/c32152ab66cde0777dfb59be65ecb207b0d494c4/Images/measurementtable.png)

### Image 2: Screenshot of the `station` table
![Image2](https://github.com/Peteresis/surfs_up/blob/c32152ab66cde0777dfb59be65ecb207b0d494c4/Images/satationtable.png)

Once the temperature information for the months of June and December was filtered, the Pandas function `describe()` was used to calculate the main statistical parameters of the June and December data.

## 💠 Deliverable #1 The statistical description for June is shown below.  

The data for June has 1700 entries or lines.  The mean temperature for June in Oahu is `74.9 F`, but it can go as low as `64 F` and as high as `85 F`, so there is a 20 degree range variation in the historical data.

### Image 3: Statistical description of the DataFrame with the temperatures for the month of June
![Image3](https://github.com/Peteresis/surfs_up/blob/de270105093c5f8a8c2fb4b435956b02abf0a4af/Images/june_describe_df.png)

## 💠 Deliverable #2 The statistical description for December is shown below.  

Using the same procedure described above, the data for December has 1517 data points.  The mean temperature for December in Oahu is `71.04 F`.  The minimum temmperature registred durung the period is `56 F` and the maximum is `83 F`.  In this case the difference between the two extremes is 27.

### Image 4: Statistical description of the DataFrame with the temperatures for the month of December
![Image4](https://github.com/Peteresis/surfs_up/blob/de270105093c5f8a8c2fb4b435956b02abf0a4af/Images/december_describe_df.png)


### Image 5: Comparison of the statistical description of the DataFrame with the temperatures for the months of June and December
![Image5](https://github.com/Peteresis/surfs_up/blob/de270105093c5f8a8c2fb4b435956b02abf0a4af/Images/december_describe_df.png)


## :three: Summary



## References
Module 9: Exploring Weather Data, https://courses.bootcampspot.com/courses/1145/pages/9-dot-0-1-exploring-weather-data, :copyright: 2020-2021 Trilogy Education Services, Web 15 Apr 2022.

Boxplot (or Box-and-Whisker Plot) - Missouri State University, http://people.missouristate.edu/songfengzheng/Teaching/MTH545/Notes03.pdf

Save a Pandas dataFrame As An Image, https://predictivehacks.com/?all-tips=save-a-pandas-dataframe-as-an-image

Display df.describe() Output In A Dataframe, https://support.sisense.com/kb/en/article/display-dfdescribe-output-in-a-dataframe

Understanding Boxplots, https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
