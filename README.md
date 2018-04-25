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

![setosapetalhist](https://user-images.githubusercontent.com/35706109/39267290-4b9029c2-48c4-11e8-95d9-30ad9b286770.png)


