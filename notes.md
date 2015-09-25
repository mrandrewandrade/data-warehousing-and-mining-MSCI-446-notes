# Part 1: Review
data on cloud
using data to change world
data analytics for sustanability
eduational data mining

datamining
exam project

1/ design questions
proxy for a feature


implicit and hidden informatoin from data
finding patterns

What do manager's do?
They make desisions and make big bucks

## Discrete vs continous variables

1/ discrete (categorical variables)
2/ continous (numberical variables)
1b/ boolean or binary variable

Numeric -> categorical conversion
Normalization -> putting variable between 0 and 1

## Data mining

### Predictive analytics (supervised learning)
Use variables to predict others

#### Classification -> discrete prediction
*Objective*: predict values of the class variable for new data
*How?* Build a model for the class variable as a function of the feature variables

- has a specific class variable/ attribute/ label
- features or inputs to the system
- training dataset

#### Regression -> numeric prediction

Think Scatter plot
Msci 466 grade vs hours of study

Table: 
|hours of study| grade|
|data1|data1|
|...|...|
|endofdata|endofdata|

Supervised

y = mx +b
y = m1 X1 + m2 x2 + m3 x3 ... mk xk + b

feature engineering -> determing inputs to system

### Descriptive analytics (unsupervised learning)
Describing an existing event

#### Association -> see which variables are associated with each other
store keeps tracked of which products are bought togeather
2 examples:

1/ data set x1 ... xk
Note: no class variable

Rows are binary

meaning of x1: things people bought in a store
item set, 1 has specific things bought

Association: shows what goes togeather
x1 x6 -> x8

Algorithm -> determines probability

Can use association for missing value imputation

#### Clustering 

Grouping based on variables

Msci 446 grade vs hours of study

Output of clustering of algorithm: column at the end of dataset which labels each data set

Get the center of each cluster -> present that

#### Outlier detection

Points that stand out

Dedicated algorithms to outlier detection

By-product of other data mining tasks

Clustering -> far from the center of cluster

Iterpret:
1. real world has measurement errors
2. people behave diffrently

Story: from Database
Setting zip code as null

garbage in garbage out problem

Use outlier detectionto fix data (might or might not be correct)

### Summary of the course in 10 minutes

#### Issues in Data mining
1. computational complexity

Can't evaluate all models 

2. validation or evaluation
How to pick the best algorithm?   
Test of a small set of data

3. data skew
Data can be misleading:

- downsampling
keep all no's and sa

- upsampling
keep all the yeses and you sample with replacement to get you more no's

sampling with replacement 
draw from dataset, draw another put it back in

sampling without replacement
draw from dataset put it aside, draw another from dataset put it aside

4. Intepretation

Human in the loop is necessary to understand
Made from subset of population

Datamining does stereotyping by default

eg. banking
take credit score and stereo on it

5. Ethics/Data Privacy


# Part 2: Exploratory Data Analysis

Before you start data mining:

- numeric: mean, median, standard deviation, percentiles, min value, max value
- histogram: 
heavy tailed distribution
bimodal distribution

discrete variables:
- list possible values and their frequencies
- count distinct
- identify and frequency of most and least frequent values

Text:
- word clouds

# Part 3: Data Mining

## Predictive

### Regression

#### Least squares linear regression (LSLR)

Input:
|id | x | y | ŷ | y-ŷ|
|p1 | 1 | 2 | 1 | 1|
|p2 | 1 |1 | 1 | 0 |
....

make plot



y- ŷ <- called residual = observed - predicted   

Supose we obtain in the following linear model:       
y = x    

Sum of the squares residuals =  \sum (y- \hat{y} )^{2}           

[img]http://www.sciweavers.org/tex2img.php?eq=%20%5Csum%20%28y-%20%5Chat%7By%7D%20%29%5E%7B2%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0[/img]


L.S.L.R. optimizes this metric   

mean squared error (MSE) = SSQ / num of data points   
root mean squared error (RMSE) = sqrt (MSE)    

in example:   
SSQ = 1^2 + 0^2 + (-1)^2 + 0^2 + 0^2 = 2   
MSE = 2/5   
RMSE = sqrt (2/5)   

Residual plot y - ŷ vs x   

put plot

Distribution of residuals   

frequency vs y - ŷ   

put histogram

If x and y are indeed linearly related, the distribution of residuals should be normal and centered around zero
Also the residual plot should not have any patterns (under/over estimation)

Suppose y is EXPONENTIALLY related to X

put plot

put residual plot

### Log transform:

y = b e^x

ln y = ln (b e^x)
      = ln b + ln e^x
      = ln b + x














