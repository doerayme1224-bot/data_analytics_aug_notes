# Lesson 6, Data Cleaning and Ananlysis in Excel
#### Handling Missing Data
[[Excel]]
Handling data that is not complete, Handling Missing data well can help keep your analysis trustworthy
- =COUNTBLANK, counts blank cells
**Imputation with Averages**; Substitute missing values with the average of available data points
1. Identify missing Values (ISBLANK)
2. Calculate average (AVERAGEIFS)
3. Impute Missing values with averages in a new space (IF)
**Imputation With Median**
same as imputation with average, but you use a different function 
- MEDIAN(FILTER())
**Deletion of Rows**
1. Identify rows With missing values
2. Manually delete the rows
**[Video on Handling Missing Data](https://www.loom.com/share/e191f46458224d7792dfa79168019c6e?sid=df6e34a2-dd0d-4bd0-a8f1-c34a55eb317c)** 
#### Error Functions
- IFNA, replaces NA data with any value you would like
- IFERROR, Replaces an error (like division by zero in excel) with any value you would like
**[Video on Error Functions](https://www.loom.com/share/1d420b5a09b8433e98a466110617dd07?sid=0deabf66-0e07-4e82-bedd-2d76bd0f98c8)**
#### Duplicates Handling
Duplicates can produce Bias and Misrepresented findings so dealing wih them is important 
- "advanced filter", under data tab, unique records only will give you the unique values (nonduplicates)
- "remove duplicates", also under data tab, removes duplicates
**[Video on Duplicates Handling](https://www.loom.com/share/a0bfd1c33b9c40d1af9b6da824ba1865?sid=77a21178-ca21-4ae5-8fe2-c45d4ab5277a)**
####  Data Transformation
- &, operator, 
- TEXT, Function, 
**Date Format Standardization**
1. Select date column
2. go to home tab and select the number group
3. Choose desired Date 

**Numeric Format Standardization**
Same steps as the date, but you can change decimal places with the decimal place thing near general

**Text Standardization**
Lower to Uppercase, UPPER(). LOWER().
Extracting Characters from text, LEFT(), RIGHT()
Changing text for other text, SUBSTITUTE()
Text Concantenation, combines text from different cells, =E1&" word "&F1
Change the apperance/order of numbers, TEXT()
replace part of text string with another text string, REPLACE()
**[Video on Data Transformation](https://www.loom.com/share/7e8ccdb5c5ef4684965925f4e5141bf5?sid=92baccd6-d7ef-4897-97cc-b3624f5d48b7)** 