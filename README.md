# Part 1: Review

* Data in the cloud (warehousing)
* Using data to change world
* Data analytics for sustainability
* Educational data mining

Data Mining course evaluations: exam (no python), project

1/ design questions  
proxy for a feature

Implicit and hidden information from data  
Finding patterns

What do managers do?  
They make decisions and make big bucks

## Discrete vs. Continuous variables

1. Discrete (categorical variables)  
  1b. boolean or binary variable (special case)
2. Continuous (numberical variables)

Numeric -> Categorical conversion  
Normalization -> making range between 0 and 1

## Data Mining


### Predictive analytics (supervised learning)
Use variables to predict others

#### Classification -> Discrete Prediction
*Objective*: predict values of the class variable for new data  
*How?* Build a model for the class variable as a function of the feature variables

- has a specific class variable/ attribute/ label
- features or inputs to the system
- input must be training dataset

E.g. Decision Tree for predicting loan application:  
````
Income < 50k --> Loan = No  
Income >= 50k -->
            Gender = F --> Loan = Yes  
            Gender = M -->
                  Credit < 700 --> Loan = no  
                  Credit >= 700 --> Loan = Yes
````

#### Regression -> Numeric Prediction

Think Scatter plot.
Eg: MSci 446 grade vs. hours of study

Table:

|Hours of study | Grade|
|:-------------:|:----:|
|data1          | data1|
|...            |   ...|

y = mx +b
y = m1 X1 + m2 x2 + m3 x3 ... mk xk + b

* Supervised
* Feature engineering -> determining inputs to system  

Eg: Movie revenue prediction project in prev years, determining appropriate m1, m2, and adding **m3 x is_franchise** bool to help with predictions.

### Descriptive analytics (unsupervised learning)
Describing an existing data set

#### Association
* see which variables are associated with each other
* no class variables

Eg:
Store keeps track of which products are purchased together.
2 examples:

1/ data set x1 ... xk of binary rows
meaning of x1: things people bought in a store
Single row is an itemset of a single --> very sparse table

Association: shows what goes together  
Eg: if x1 and x6 -> x8  
Algorithm -> determines probability
Can use Association for missing value imputation

Eg: MillionSongDataSet had a lot of words of profanity came associated.

**Why should business care?**
- if bread and butter go together, then maybe promote butter to sell more bread
- make predictions on butter based on bread demand
- or predict impact of discontinuing butter on bread

You can take Classification data and run Association on it. Association is more general than classification.  
Eg: Which Eng. program quiz? Find associations, predict missing values.

#### Clustering
- grouping based on variables
- splits your data into meaningful sets
- eg. how many different kinds of customers
- tightly connected groups with similar characteristics

Eg. Msci 446 grade vs hours of study

Output of clustering of algorithm: column at the end of dataset which determines *Cluster Membership*

*Cluster centre* - a good representative from the middle of the cluster.

#### Outlier/Anomaly Detection

Data that stand out

Dedicated algorithms to outlier detection

By-product of other data mining tasks (i.e Clustering, regression)

Clustering -> far from the center of cluster

Interpret:
1. Measurement errors/ bad data
2. Real people behave differently/ not everyone fits the model

Garbage in/Garbage out: -->  
Story: Police Dept. set Homeless people's ZipCodes as dept's address, then data mining found police dept. as a crime hive.

Use outlier detection fix data (might or might not be correct)

### Summary of the course in 10 minutes

#### Issues in Data mining
1. Computational complexity
  - Can't evaluate all models
2. Validation or evaluation
  - How to pick the best algorithm?   
    - Test with smaller set of data
3. Data skew.
Data can be misleading, to mitigate:
  - downsampling:
keep all no's and reduce your yes's
  - upsampling:
keep all the yes's and you sample with replacement to get you more no's
  - Sampling with replacement -->
draw from dataset, draw another put it back in
  - Sampling without replacement -->
draw from dataset put it aside, draw another from dataset put it aside
4. Interpretation
  - Human in the loop (domain expertise) is necessary to understand
  - Made from subset of population
  - Data Mining does stereotyping by default
  - Eg. banking --> take credit score and steretype on it
5. Ethics/Data Privacy


# Part 2: Exploratory Data Analysis

Before you start data mining:

- numeric: µean, median, standard deviation, percentiles, min value, max value
- histograms: watch for -->
  - heavy tailed distribution
  - bimodal distribution
  - left skew/right skew

Discrete variables:
- list possible values and their frequencies
- count distinct
- identify and find the frequency of most and least frequent values --> check for data quality/spot outliers

Text:
- word clouds
- make sure data is suitable for data mining

# Part 3: Data Mining

## Predictive

### Regression

#### Least squares linear regression (LSLR)

Input:

|id | x | y | ŷ | y-ŷ|
|--:|--:|--:|--:|:--:|
|p1 | 1 | 2 | 1 | 1  |
|p2 | 1 | 1 | 1 | 0  |
|p3 | 3 | 2 | 3 |-1  |

Make plot

y - ŷ <- called residual = observed - predicted   

Suppose we obtain in the following linear model:       
y = x    

Sum of the squares residuals =  \sum (y- \hat{y} )^{2}
![](http://www.sciweavers.org/tex2img.php?eq=%20%5Csum%20%28y-%20%5Chat%7By%7D%20%29%5E%7B2%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

SSQ --> L.S.L.R. optimizes this metric   

Mean Squared Error (MSE) = SSQ / num of data points   
Root Mean Squared Error (RMSE) = sqrt (MSE)    

In example:   
SSQ = 1^2 + 0^2 + (-1)^2 + 0^2 + 0^2 = 2   
MSE = 2/5   
RMSE = sqrt (2/5)   

Residual plot y - ŷ vs x   

put plot

Distribution of Residuals   

Frequency vs y - ŷ   

put histogram

- If x and y are indeed linearly related, the distribution of residuals should be normal and centered around zero
- Residual plot should not have any patterns (under/over estimation bias)

Suppose y is EXPONENTIALLY related to X

put plot

put residual plot

### Log transform:
````
y = b e^x
ln y = ln (b e^x)
     = ln b + ln e^x
     = ln b + x
````

## More on least squares

- least-squares linear regression optimizes SSQ/RSS (name in python) _<-- hinted at inclusion in Exam_

- goodness of fit
y = m1x1 + m2x2 + .... + mxkx + b

Residual Plot
- one for each Xi

Residual Distribution
- on for each model

If the fit is no good --> Log Transform

### Another example of log transform

TODO: typset the equations


What is the point?

It linearizes the model so linear regression can be used on non-linear relationships

### Piecewise Linear Regression

- called segmented regression in R

#### Example: electricity use in households

Correlate electricity consumption vs. outdoor temperature

Cooling gradient -> proxy for insulation and efficiency of AC
Heating gradient -> proxy for insulation and efficency of furnace

### Variable Selection / Feature engineering

Example: movie revenue and other factors   
What factors do you use?    

Three techniques:

1. Forward Selection
Try each variable one by one and find the one the lowest sum of squares error
  - not used in practice
2. Backward Selection (more practical than FS)
Try with all the variables and remove the worse one (greedy algorithm) (bad variable = highest impact on SSQ)
  - has python implementation
3. Shrinkage
  - LASSO: uses matrix algebra to shrink coefficient to help with eliminating variables

Why not use all the variables/features? --> Risk of overfitting

Linear regression is very sensitive to outliers.
OK to remove outliers for building models

#### Risks of removing Outliers
- can remove good data if it doesn't fit the model
- linear regression is a model of convenient fiction
"Linearize the model simplifies the model based on the data you have"

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
