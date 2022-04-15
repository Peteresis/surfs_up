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

[The complete code used for this analysis can be found here](https://github.com/Peteresis/surfs_up/blob/fc143a1f75806a3382e69c544bd214478e9deb1a/SurfsUp_Challenge.ipynb).  Below is a snippet of the code used for extracting the temperatures for the month of June.

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
![Image5](https://github.com/Peteresis/surfs_up/blob/f6b18997809eb80eac2ff29adb11110833181cf2/Images/summary_describe_df.png)


## :three: Summary

At first sight, and based on the mean temperature data, it looks like the island of Oahu is a perfect place to visit as a tourist.  The mean temperature in summer (June) is about `75 F` and during winter (December) it drops to `71 F`.  That is about the same temperature that most air conditioning units keep inside a house, so the conditions look favorable for the business.  However, before jumping into conclusions it is advisable to take a closer look at the data, so two additional queries were done:

### 1. A histogram plot to visualize if the data is skewed

Below is the histogram chart for the temperatures during the month of June.  It looks like the data is skewed to the right and for the most part the temperature during June oscillates between `71 F` and `79 F`.  From the graph, the frequency of days with extreme temperatures (either cold or hot) during June seems low, so June should not be a problem for the Surf 'n Shake business.

### Image 6: Histogram of the temperatures during June
![Image6](https://github.com/Peteresis/surfs_up/blob/647c4d44e22fe35f2af82c42da98a43557f14428/Images/JuneTemps.png)

In the same manner, the December histogram is shown below. The graph shows that the temperature in December usually ranges between `66 F` and `76 F`, but there are many days in December when the temperature stays around `72 F`. Extreme temperature days are uncommon in December when compared to the central block of the graph. The data looks slightly skewed to the right, but not nearly as much as in the June graph.

### Image 7: Histogram of the temperatures during December
![Image7](https://github.com/Peteresis/surfs_up/blob/647c4d44e22fe35f2af82c42da98a43557f14428/Images/DecemberTemps.png)

To conclude the section on histograms, we show the histograms for June and December superimposed below. This chart illustrates that the June data is significantly skewed to the right than the December data. Most of the temperatures recorded in those two months are between `66 F` and `77 F`, indicating that the temperature does not appear to be a barrier to tourists visiting Oahu.

### Image 8: Histogram of the temperatures during June and December superimposed
![Image8](https://github.com/Peteresis/surfs_up/blob/e450998192063dd2adbfba4ff0a6a4929dfa916b/Images/JuneAndDecemberTemps.png)



### 2. A boxplot to check for possible outliers

As a final check, we will present a Boxplot (Box-and-Whisker Plot) for the temperature readings in June and December.  This type of chart is useful to confirm data sekewness and capture outlier data points.</br>

The box for June once more confirms tha the data is skewed to the right.  However, the box for December seems to indicate that the data for that month is skewed to left.  This means that the month of June tends to be hotter than what the average temperature calculation suggests.  In the case of December,  there seems to be a slight prevalence of 'cold' days.

### Image 9: Box-and-Whisker Plot of the temperatures during June and December
![Image9](https://github.com/Peteresis/surfs_up/blob/e450998192063dd2adbfba4ff0a6a4929dfa916b/Images/boxplot.png)



## References
Module 9: Exploring Weather Data, https://courses.bootcampspot.com/courses/1145/pages/9-dot-0-1-exploring-weather-data, :copyright: 2020-2021 Trilogy Education Services, Web 15 Apr 2022.

Boxplot (or Box-and-Whisker Plot) - Missouri State University, http://people.missouristate.edu/songfengzheng/Teaching/MTH545/Notes03.pdf

Save a Pandas dataFrame As An Image, https://predictivehacks.com/?all-tips=save-a-pandas-dataframe-as-an-image

Display df.describe() Output In A Dataframe, https://support.sisense.com/kb/en/article/display-dfdescribe-output-in-a-dataframe

Understanding Boxplots, https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
