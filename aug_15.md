# Lesson 6: Measures of Position and Disperssion

**Measures of Position**:Important for knowing how *values* relate to a *dataset*
**Percentiles**                                                                   / **Quartiles**
a *Measure* which shows the *value where a certain percent of observations*       / Breaks data into four equal parts, with each part representing a key dataset 
fall *within a dataset*.                                                            **Key Quartiles**
**Calculating a Percentile**                                                        25%: 25% of data lies below
Step 1: Sort Data in *Ascending Order*:                                             50%: *Median*
                                         60, 70, 75, 80, 85, 90, 95                 75%: 75% of data lies below
Step 2: Determine *Position* Using *Formula*:                                       The steps for Calculating The percent are essentially the same, the differnce
                                position = percent ( observations + 1 )             comes not in how they solve, but in how they are broken up.
                                    p = 0.4 ( 7 + 1 )  =  3.2
                                    *Falls Between 3rd and 4th data set*                    60, 70, 75, 80, 85, 90, 95
Step 3: Identify *Percintile*:                                                              0.25 ( 7 + 1 ) = 2
                                Interpolation Formula:                                      Because its a whole number, it represents the 2nd Value 
    Lower Position +( *Fractional Part* ( higher Position + Lower Postition ))              (You don't need the interpolation formula)
                                75 + ( 0.2 ( 80 - 75 )) = 76
                              40 % of values fall below 76 in the dataset 
*Fractional Part* refers to the *Decimal Place* from the *Position Formula*                                                                      



**Meausures of Dispersion**
Help us get a complete picture of *how the data spreads*:

**Range**
*Differnce* betwwen the *highest and lowest Values* in a data spread
if our spread is (3,7,9,5,12)  
12 - 3 = 9
the range is nine

**Variance**
Disperssion by calculating the squared deviantions of eaach data point from the mean
complex understanding of disperssion

( 4, 5 , 5 , 5 , 6 , 6 , 7 , 9 )

Step 1: find *Mean*
( 4 + 5 + 5 + 5 + 6 + 6 + 7 + 10 ) / 8 = 6

Step 2: Calculate *squared deviations from mean*:
4
1
1
1
0
0
1
16

step 3: *Calculate Variance*

(4 + 1 + 1 + 1 + 0 + 0 + 1 + 16) / 8 = (24 / 8) = 3
Variance Means they  deviate from the mean by that amount (in this case, 3)

**Standard Deviation**
Square root of Variance
Square Root of 3 = 1.732...
This is the distance between two given datapoints in the set.


# Lesson 7: Visualizing Data Distributions

Its good to Visualize data to *see patterns and insights*.

**Frequency Distributions**
These Visualizations show how often a value or categorie will appear in a dataset

*Bar Charts*
Good for Categorical data
-each bar will represent a category and the height of the bar represents the categories frequency

*Histograms*
Shows *distribution of Numerical* data in *Ranges*
x-axis: Bins/Ranges
y-axis: amount of occurences in a bin/range

*Box Plots*Visualization of dataset distribution
Shows: -Central Tendency
       -Spread
       -Possible Outliers
the box marks Q1, Q2, and Q3
The whiskers(lines outside the box) Represents the range of values in a dataset 

whisker length: 1.5 times innerquartiles range
1.5( Q3 - Q1)
lower whisker: Q1 - whisker length 
upper whisker: Q3 + whisker length

Outliers are represented by poiints outside of the whiskers 