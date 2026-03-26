1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

Noticing that the target zone is for 30 year old participants are between 95 - 162bpm, it shows that the heart data is not accurate. Seeing some of the data is less than 95 bpm and not even close to 162 bpm will cause a lot of outliers making misleading conclusions.

2) Which file had the **poorest** data quality? How do you know?

The file "phase1.txt" is missing data, has some high values in order to even use the data you to get rid of some strings, none values and outliers.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
hr_data = [68, 70, 71, 72, 72, 73, 74, 75, 180]
hr_data.remove(180)
new_hr_data = [68, 70, 71, 72, 72, 73, 74, 75]
range = 75 - 68
print(range)

b) Explain how the extreme value affects the range.
A very extreme outlier can expand the range significantly, causing the range to misinterpret the true variability of the data.


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
To help understand the spread of data with extreme values, I would Interquartile Range because it focuses on the middle 50% of the data which considers all data points.

