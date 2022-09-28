# Surfs Up Analysis

## Overview
In order to secure an investment to open up a surf and ice cream shop on the Hawaiian island of Oahu, W. Avy asks that I completed weather analysis of the island. I collected temperature and precipitation data from the nine stations located on the island. Using the data from all the stations, I am able to show W. Avy the summary statistics and well as a daily precipation graph. Lastly, using Flask I created routes that W. Avy can use to see the full precipitation data, the different stations, and the temperatures.

### Resources
- Data Source: hawaii.sqlite
- Software: SQLlite, Python, Jupyter Notebook, Flask

## Results
Three key differences between June and December:
1. The difference in mean temperature between June and December is 4 degrees (75-71=4). Although this may not seem like a lot, June's mean temperature is one standard deviation below December's which potentially could cause a decrease in tourism. 
2. June's minimum temperature is 64 degrees, whereas December's is 56 degrees. The strong possibility that the temperature will drop below 60 degrees in December will surely impact how often island-goers, and locals alike, will be in the mood for ice cream. 
3. Obviously December will have cooler temperatures but the variability is larger as well. The range for June temperatures is 21 degrees (85-64=21) and the range for December is 27 degrees (83-56=27). With a larger variability comes less predictability of the weather.

Graphing the June and December temperatures side-by-side in a boxplot allows you to quickly see the similarities and differences between the two months. 

![June_December_Temp_Boxplot](https://user-images.githubusercontent.com/109091887/192883876-dedd094f-2728-4bf3-aefc-264846314b7a.png)

Histograms will also show us the frequency of the temperatures within each month. 

![June_Temp_Histogram](https://user-images.githubusercontent.com/109091887/192888661-5fbb5a51-d6c8-4b1d-8408-82611c420c0a.png)
![Dec_Temp_Histogram](https://user-images.githubusercontent.com/109091887/192888686-7ebceaeb-5f6f-4edc-afcc-8ab6e849125c.png)


## Summary
Overall, I feel confident that the surf and ice cream shop will be success given the previous years data. By looking at the summary statistics, we have observed that the temperature varies throughout the year but I don't believe the drop from June to December will significantly effect ice cream sales. Additionally, if you have an excellent product then the weather will not deter customers from frequenting your business. 
Two additional queries that could be beneficial to the analysis are:
1. Pulling and analyzing the summary statistics for precipitation in the two months. Although there is only a minor difference in temperature between the two months, a large difference in precipation could play a role in profits.
2. It's possible that certain parts of Oahu have slightly different weather patterns so a breakdown of the temperature (and precipitation) for each station would help determine the best location on the island to open the shop. 
