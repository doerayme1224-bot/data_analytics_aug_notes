# Lesson 8: Stastistical inference
**Probability**
[[General Data Analytics]]
Measure of *how likely* an event is to happen
- scale from *0 - 1*
0 means event is *impossible* 
1 means event *will happen*
Formula for Probability:
Probability = Number of favorable outcomes/ Total number of possible outcomes
The sum of all probablities outcomes are always equal to 1
ex: coin toss, dice roll

**Probability distributions**

Help us understand the chance of different outcomes in a dataset

*Normal Distribution*
Shows the *spread of Data around an average value (mean)*
Has a *bell shaped curve*, which is common in the collection of data due to natural process. Called the *central limit *theroem*. its important because it *helps us assume* when a dataset has *normal distribution*

![alt text](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2F3a5391f0-5201-4baa-b4cc-d3a37243338d%2FUntitled.png?table=block&id=b2139f4c-e602-4f87-8b4b-9fc3392026f2&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=2000&userId=&cache=v2)

*Hypothesis testing*

Statistical procedure to determine if there is enough evidence for a claim 
Used in research settings to determine differences and relationships between variables

step 1 - define the question
Helps make your testing more guided
Step 2 - Formulate hypothesis( question ) 
Null hypothesis (H0) - Default assumption, Indicates no effect, no differnce, no realationship
Alternative hypothesis (Ha) - Opposite of null hypothesis
Step 3 - Collect data 
Make sure the data you collect addresses the research 
step 4 - perform statistical test 
Conduct specific Statistical calculation
Step 5 - Finding p value and making a decision
Finding p value: p-value represents the probability that the observed results occured by chance
A lower p value implies stronger evidence against the null hypothesis, meaning the results are unlikely to be random
The P-Value derives from the outcome of the statistical test that you chose to preform
Comparison and significance level
Significance level (a) Represents threshhold of when we start to reject the null hypothesis.  It indicates the probability of incorrectly rejecting the null hypothesis when it is actually true 
Typical significance level is 0.05
p <= 0.05 reject Null hypothesis
p > 0.05 fail to reject Null Hypothesis
