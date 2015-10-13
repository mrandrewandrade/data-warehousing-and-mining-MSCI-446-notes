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

![](http://www.sciweavers.org/tex2img.php?eq=%20%5Csum%20%28y-%20%5Chat%7By%7D%20%29%5E%7B2%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)


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


## More on least squares

- least-squares linear regression optimizes SSQ/RSS

- goodness of fit
y = m1x1 + m2x2 + .... + mxkx + b

Residual Plot
- one for each Xi

Residual Distribution
- on for each model

### Another example of log transform

TODO: typset the equations


What is the point?

It linearizes the model so linear regression can be used on non-linear relationships

### Piecewise Linear Regeression


- called segmented regression in R

#### Example: electricity in households

Corelate electricity consumption vs outdoor temperature

cooling gradient -> proxy for insulation and efficiency 

### Variable Selection / Feature engineering

Example: movie revenue and other factors   
What factors do you use?    

Three techniques:

1. Forward Selection
Try each variable one by one and find the one the lowest sum of squares error
- not used in practice

2. Backward Selection
Try with all the variables and remove the worse one (greedy algorithm) 
- has python implementation
3. Shrinkage
LASSO: uses matrix algebra to shrink coefficient to help with eliminating 

### Remove Outliers
- can remove good data if it doesn't fit the model
- linear regression is a model of convenient fiction
"Linearize the model simplifes the model based on the data you have"

# Part 4 

## Classification
### Baysian Classification

Baye's Theorem

P (A|B) = P(B|A) = P(B|A) P(A) / P(B)

#### Dishonest Casino Problem

- A dishonest casino has a 99% fair dice and 1% loaded dice, where:

fair: (1) = P (2) = P (3) = P (4) = P(5) = P(6) = 1/6    

loaded: P (1) = 0.1, P(2) = 0.1, P(3) = 0.1, P(4) = 0.1, P(5) = 0.1, P(6) = 1/2

Compute P(loaded | rolled 3 consecutive times)

P(A|B) = P(B | A) P(A) / P(B)

= P(0.5*0.5*0.5) * P(0.01) / (1/6^3* 0.99 + 1/2^2*0.01)

prior probability

posterior probability

What is the value of a class variable C given the values of the feature variables x through xk?

P( pay off load = yes | credit = .. and marital status = .. and years with current employer = .. )
 = P(features | class ) P (class) / P(features)

Major assumption: features are independant

Naive bayes -> this approach in tutorial

Friday: simple example

Tuesday: complicated
 Read example on course website

P(A|B)  = P(A) P(B|A) / P(B)



### Bayesian Classification

Discrete variable.

num | refund | maritial status | cheat?|

Use Naive Bayes to predict the value of cheat given that refund = no and M.S. = single (S)

P(A|B) <- posterior probability
P(A) <- prior
P(b|A) <- likely hood

P(cheat=yes|refund=no and M.S. = S)= P(cheat=yes)P(refund=no and MS=S| cheat = yes) / P(refund = no and M.S. = S)
 = P(cheat = yes) P(refund=no and MS=S | cheat = yes) / P(refund = no and MS = S | cheat = yes)P(cheat=yes) + p(refund = no and MS = S|cheat=no)P(cheat=no)

Advantage:
incorporates all the variables 
useful in practice (simple to use)


Disadvantage:
assumes independance
not human interpretable

### Naive bayes with numeric features

Look at example .pdf

Play golf based on termperature

There is no prior prability for a specific temperature (because it is continous)

What were the examples on non-normal distribution?


### Decision tree

Used to do classification of discrete variable.

First use entropy to probability districution

Eg. Roll a 6 sided die
1/6th of each side (unless dishonest casino)
Is there chaos in distribution?
Yes -> you don't konw what is going to happen.

What if 1 or 0 where one is 95% probablitily
-> more certainty

How do we formalize this?  

### Enthropy!

Say X is a random variable, with the following probability distribution:

X = x1 with probability p1

X = x2 with pr. p2

x = xn with pr. pn

The entropy of X denoted H(x) = -p1 log2 (p1) - p2 log2(p2) - ... - pn log2 pn

Observations:

1. Complete certainty => H(X) = 0
X = x1 with pr 1, P(X=x) = 1
H(x) = -1 log2 1 - 0 log2 (0) - 0 log2 (0) - ...
     = -1.0 -0 -0 = 0
2. P (X=x1) = P1 = 1/2, P(X = x2) = p2 = 1/2
H(x) = -1/2 log2 1/2 - 1/2 log2 1/2
     = -1/2 * -1 - 1/2 * -1 = 1/2 + 1/2 = 1
3. P1 = 1/4, P2 = 1/4, P3 = 1/4, P4 = 1/4
H(x) = -1/4 (-2) * 4 = 2

|Refund|marital status|cheat|


2 choices for the root of the tree

refund
/ \
y  n 

When yes:
3 cheat = no
0 cheat = yes
p1 = 3/3
p2 = 0/3

H(x) = -1 log2 1 - 0 log 0 = 0

4 cheat = no
3 cheat = yes
p1 = 4/7 
p2 = 3/7 

H(x) = -4/7 log2 4/7 - 3/7 log2 3/7 = 0.98

Marital status
/     |     \
single maried divorced

single
2 cheat = no
2 cheat = yes
p1 = 1/2
p2 = 1/2

H(x) = 1


married
4 cheat = no
0 cheat = yes
p1 = 4/4
p2 = 0/4

H(x) = 0


divorced
1 cheat = no
1 cheat = yes
p1 = 1/2
p2 = 1/2
H(x) = 1

At bottom of tree which want low entropy (as close to 0 as possible)

1. Now we need to calculate entropy for each
2. Calculate weighted average entropy of refund

Weighted average entrpy of REFUND:
3/10 * 0 + 7/10 * 0.98 = 0.69

Weight average entropy of marital status
4/10 * 1 + 4/10*0 + 2/10 * 1 = 0.6

Maritial status has lowest entropy, therefore at the top

        MS
    /   |   \
Single Married Divorces
  /      |          \   
refund  cheat = no  refund
/   \    |


cheat = no     refund

Midterm: up to and including topic number 7.

Half of midterm: similar to practice questions
Other half: thinking questions

# 1R / One-R algorithm 

Data from class
Collect gender, device, glasses, front?

For gender:  
if gender M then FRONT = NO
2m Front = yes
20M front = no

if gender = F then FRONT = Yes
12 f front = yes
4f front = no

For device:
If device = yes then front  = no
3 front = yes
11 front = no

if decide = no then front = no
11 front = yes
13 front = no


























