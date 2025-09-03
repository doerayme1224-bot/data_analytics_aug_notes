# Lesson 6: Measures of Position and Disperssion
[[General Data Analytics]]
**Measures of Position**:Important for knowing how *values* relate to a *dataset*
**Percentiles**                                                                  
a *Measure* which shows the *value where a certain percent of observations* fall *within a dataset*.                                                           

**Calculating a Percentile**                                                        
Step 1: Sort Data in *Ascending Order*:                                             
                                         60, 70, 75, 80, 85, 90, 95                 
Step 2: Determine *Position* Using *Formula*:                                       
                                position = percent ( observations + 1 )             
                                    p = 0.4 ( 7 + 1 )  =  3.2
                                    *Falls Between 3rd and 4th data set*                    
Step 3: Identify *Percintile*:                                                              
                                Interpolation Formula:                                       
    Lower Position +( *Fractional Part* ( higher Position + Lower Postition ))              
                                75 + ( 0.2 ( 80 - 75 )) = 76
                              40 % of values fall below 76 in the dataset 
*Fractional Part* refers to the *Decimal Place* from the *Position Formula*                                                                      

**Quartiles**
Breaks data into four equal parts, with each part representing a key dataset
fall *within a dataset*.                                                           
 **Key Quartiles**
25%: 25% of data lies below
50%: Median
75%: 75% of data lies below
Steps for calculating percent are essentially the same, the difference comes not in how you solve, nut in how they are broken up
                                        60, 70, 75, 80, 85, 90, 95
                                        0.25 ( 7 + 1 ) = 2
                                        Because its a whole number, it represents the second value (you don't need to use the interpolation formula) 


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