# Project 2018 Programming and Scripting

## Introduction

A new data analysis team is being created in our company and my manager has tasked me with training the new team members. The purpose of this study is to introduce my colleagues to the core concepts of data analysis with Python by performing an analysis of the famous Iris Data using key python libraries, such as Pandas, Seaborn and Scipy. This study will demonstrate how to perform statistical analysis and data visualisation. We will analyse the Iris Dataset by focusing on the following ststistical concepts: The distribution of data, measures of central tendency, measures of variability and correlation 

In the next sections, we will introduce the Iris Dataset, formulate our research questions and hypothesis 

### Iris Data Set

The Data set contains information on the Sepal width/length and Petal width/length of three species of the Iris flower. 

### Variables

There are 150 data points in the Iris dataset: 50 for each flower type and it contains 5 variables. 'Name' is a categorical variable which denotes the different flower types. It has three levels: Setosa, Virginica and Versicolor. There are 150 data points in the set: 50 for each flowertype. There are four ratio variables (all measured in centimetres): Petal height, petal width, sepal height and sepal width.


The independent variable is the Name categorical variable. This is also called a Predictor variable. We want to observe how the other variables in the study are affected by the indepdent variable. 

The four ratio variables outlined above are the depedent variables in this study (also called outcome variables). These are the variables that we expect may be affected or changed by the indepdent variable (the flower types) # https://statistics.laerd.com/statistical-guides/types-of-variable.php

### Research Questions and Hypotheses
1. Are the three flower types normally distributed across all depdent variables?
2. What is the difference in Sepal length between the three flower types?
3. What is the difference in Sepal width between the three flower types?
4. What is the difference in Petal width between the three flower types?
5. What is the difference in Petal height between the three flower types?

6. Is there a postive correlation between Sepal Length and Petal Height?

We shall also make some hypotheses. A hypothese is simply an 'educated quess' we make at the beginning of a study on what we expect to find. http://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/

A good way of making a hypothese is by visually inspecting the data and making predictions. Firstly, it is important to find out the differences between a Sepal and a Petal. The Sepal is on the outside and the petal is on the inside, closer to the centre of the flower. The below sideview of an Iris shows the difference clearly. 

![SepalPetal](https://raw.githubusercontent.com/ritchieng/machine-learning-dataschool/master/images/03_iris.png "Sepal and Petal")

![irisflowers](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Iris Flowers")
The above picture is not perfect, of course, as they are not all taken from the same distance/postion. It is therefore, difficult to judge differences in size. However, we can make the following observations: The petals on the Setosa appear to be significantly smaller than the other flowers. The Sepals appear to be of a similar length across all of the flower. 

The hypotheses are as follows: 

1. The petal width and petal length of the Setosa is significantly smaller that the other flowers. 

2. The sepal length of all flowers is similar.


## Distribution of the Data

### Petal Length

#### Setosa Petal Length

![setosapetalhist](https://user-images.githubusercontent.com/35706109/39267290-4b9029c2-48c4-11e8-95d9-30ad9b286770.png)


![setpetalqq](https://user-images.githubusercontent.com/35706109/39267890-2050f8c0-48c6-11e8-82a2-48fb5d8b1397.png)

The histograms appears to be normally distributed, though is slightly left-skewed. From the statsModel library we can also create a normal QQ plot, another usual visual tool to check if data is normally distributed. If the data is in a straight line, then the data is normally distributed.

As we can see in the above QQ Plot, the Setosa petal length data follows a straight line though it does deviate at the very top and bottom.

While the histogram and QQ plot suggest that it is normally distributed. Using the stats module from the Scipy library in Python, we can perform a Shapiro-Wilk test to test for normality. The null hypothese is that the data is normally distributed. In other words, if the p-value is greater than our chosen alpha value .05, then we accept the null hypotheses and the data is normally distributed. 

A Shapiro-Wilk test of Setosa Petal length suggests that the data is normally distributed, *w = .955, p= .055.*

#### Virginica Petal Length

![virginica_hist](https://user-images.githubusercontent.com/35706109/39269731-8a2ee68a-48cb-11e8-9d07-968a57984201.png)

![virgqq](https://user-images.githubusercontent.com/35706109/39269790-bc060fee-48cb-11e8-94ac-0d851c50c31f.png)

The histogram is slightly right skewed and uniform in the middle. The middle bars are of a similar height. The QQ plot suggests that it is normally distributed, though with some small deviations. 

A Shapiro-Wilk test of Virginica Petal length suggests that the data is normally distributed, *w = .962, p= .110.*

#### Versicolor Petal Length




