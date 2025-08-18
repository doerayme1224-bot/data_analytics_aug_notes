# Lesson 8: Stastistical inference
**Probability**

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



# Lesson 9: Realationships Between Variables
**Correlation** (often denouted as "r")
Statistical concept which measures how much two numbered variables will change together
Helps us evaluate trends
Correlation is represented on a scale from -1 to +1
+1: Perfect Positive Correlation (as one variable increases, the other variable also increases) 
-1: Perfect Negative Correlation (as one variable increase, the other variable decreases)
0: No Correlation (no linear realationship between the two variables)

*Correlation Doesn't Mean Causation*
Two variables can have the same correlation, but that doesn't mean thart one variable is responsible for the other

![alt text](https://codingtemple.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F833abfe9-9ed0-4d7c-9473-f1ece2104e38%2Fd99af45e-b7ed-4fbc-af4e-d174292bfc9d%2Fexample.svg?table=block&id=adf23fb6-9f4e-4591-baaa-19c5b25d32ad&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&userId=&cache=v2)

**Correlation Coefficeints**
if correlation (c) (0 < c <= +1) this means Positive Correlation
if correlation (c) (0 > c >= -1) this means Negative Correlation
if correlation (c) ( c = 0 ) This means no Correlation. The variable is not affected by changes from the other variable

![alt text](https://codingtemple.notion.site/image/https%3A%2F%2Fwww.simplypsychology.org%2Fwp-content%2Fuploads%2Fcorrelation.jpg?table=block&id=bb7f2dcc-fc60-49fa-942f-ea964c79ffa9&spaceId=833abfe9-9ed0-4d7c-9473-f1ece2104e38&width=2000&userId=&cache=v2)

**Strength of Correlation**
*Common Threshhold for Interpreting Correlation Strength*
0.8 <= c <= 1 : Strong Correlation (Substantial realationship between Variables)
0.6 <= c < 0.8 : Moderate Correlation (Noticeahble realationship between Variables)
0.2 <= c < 0.6 : Mild Correlation (Weak realationship between Variables)
c < 0.2 : No Correlation 

![alt text](https://booksite.elsevier.com/9780128017128/content/Student_Resources_Figures/Figure%201.5.1.jpg)

**Simple Linear Regression**

Statiscal Tool which models the relationship between two continous variables with a linear equation to observed data
It Identifies a Linear relationship between two variables, Which allows us to predict a Variable based on the Value of the other (line of best fit)
ther "line of best Fit" allows us to make predictions
Regression Equation (y = mx + b)
allows you to make predictions of a variable given the value of the other variable

*Limitations of Lineaer Regression*
Assumption of linearity
Assumes all relationships between variables is (doesn't hold true for all datasets)
Outliers
Can heavily skew or distort the results of analysis, Which leads to innacurate data 

![alt text](https://justinsighting.com/wp-content/uploads/2016/05/housing-price-and-square-feet-predicted-768x549.jpg)

# Lesson 10: Logic Tree
Systematic Strategic way of dealing with Problems (Structured Thinking)
1 : define Key Problem (be specific on details)
![Image on logic tree](https://cdn.disco.co/media/Screenshot_2025-07-04_080427_9a46d9e6-9eec-40a6-8281-34ab64470b05.png)
Your logic tree level means the branch step:
![the levels of logic tree](https://cdn.disco.co/media/Picture1_97028079-b804-469a-92ed-6318026e7080.gif)
2: Break Key Problem Into smaller Issues (possible causes) 
-Use opposing approaches to cover all bases
![picture for step 2](https://cdn.disco.co/media/Screenshot_2025-07-04_080438_3b358251-6136-4b00-b7f7-02fe20f1f8ea.png)
3: break those key problems Into even smaller Issues
-Sub issues should lead you to thinking about the main problem if you work through them in reverse
![picture for step 3](https://cdn.disco.co/media/Screenshot_2025-07-04_080745_92d969ad-32e1-4799-8710-cf2613c150b3.png)
4:Keep branching issues ou tuntil they are in their "Simplest Form"
![Last image for today](https://cdn.disco.co/media/Issue-Tree-Example-3-1-1024x556_27aa2f90-7fda-4910-9533-fe5b21e95c76.png)