# Fordgo Bike Rides Exploration
## By Youssef Lasheen

## Dataset


The data consists of information regarding 183,412 fordgo bikes trips covering the greater San Francisco Bay area in Febuary 2019, including trip start_date, trip duration, and other user realted attributes. The dataset can be found [here](https://video.udacity-data.com/topher/2020/October/5f91cf38_201902-fordgobike-tripdata/201902-fordgobike-tripdata.csv), with feature documentation available [here](https://docs.google.com/document/d/e/2PACX-1vQmkX4iOT6Rcrin42vslquX2_wQCjIa_hbwD0xmxrERPSOJYDtpNc_3wwK_p9_KpOsfA6QVyEHdxxq7/pub).

## Summary of Findings
- There are a lot more subscriber usage than customers

Trip Duration is so dependendable on the age of the member:
    - When the age between 20 to 45, the trip duration is higher than the older ages. 
    - There's a leap at an older age (around 60 years) to got 3000 trip duration. 
    - Subscribers the trip duration is higher for older age.

Bike Ride Durations for Different Age Group Across DayofWeek:
    - There are more younger bikers across 7 days .
    - Bikers on Saturday and Sunday bike longer compared to weekdays.

- Most riders were male subscribers who had less mean trip duration than females and other.



## Key Insights for Presentation

For the presentation, I focus on just the influence of the attributes of users on the duration of the trip. I start by comparing the duartion with the user_type then I compared it with Gender, Age.
I used countplots, violinpolts, histograms, and barh plots.

Afterwards, I introduced the start week variable to compare the duration of the user's trips mean with the week day. To start, I used the COUNT plots of duration and Weekday.