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

![verpetlen](https://user-images.githubusercontent.com/35706109/39270216-47843dc4-48cd-11e8-8998-8615a323a5f7.png)

![verpetlenq](https://user-images.githubusercontent.com/35706109/39270218-4a779ae4-48cd-11e8-8324-2165f844e865.png)

The histogram shoes a strong left-skew or tail in this variable. However, the QQ Plot does follow a straigh line. This demonstrates why it is important to use more than one plot to examine the distribution of data. 

A Shapiro-Wilk test of Versicolor Petal length suggests that the data is normally distributed, *w = .966, p= .158.*

As can be seen above, the petal length of all three species of Irish are normally distributed. 

### Petal Width

#### Setosa Petal Width

![setpetwidthhist](https://user-images.githubusercontent.com/35706109/39271696-a56221fa-48d1-11e8-94dd-ca8f4e12d056.png)

![setpetwidthq](https://user-images.githubusercontent.com/35706109/39271707-abc25498-48d1-11e8-93ec-c3b53bf10473.png)

The histogram demonstrates that the Setosa petal width is strongly right-skewed and may not be normally distributed. The QQ Plot is not useful as so many variables are clustered in one area of the plot. 

A Shapiro-Wilk test of Setosa petal width suggests that the data is **not** normally distributed, *w = .814, p= < .000.*

#### Virginica Petal Width

![virpetwh](https://user-images.githubusercontent.com/35706109/39274364-a357a7ba-48d9-11e8-914c-4f47f2084013.png)

![virpetwq](https://user-images.githubusercontent.com/35706109/39274369-a59e5730-48d9-11e8-866f-61e9f9782fce.png)

The histogram is skewed right, but the QQ plot looks relatively straight.

A Shapiro-Wilk test of Virginica petal width suggests that the data is normally distributed, *w = .960, p= .087.*

#### Versicolor Petal Width

![verpetwh](https://user-images.githubusercontent.com/35706109/39274585-5fbe37fc-48da-11e8-8079-d8644137b9cd.png)

![verpetwq](https://user-images.githubusercontent.com/35706109/39274588-6215df1e-48da-11e8-9394-a914335c0662.png)

The histogram shoes that the variable is bimodal (has two distinct peaks)

A Shapiro-Wilk test of Versicolor petal width suggests that the data is *not* normally distributed, *w = .948, p= .027.*

Setosa and Versicolor petal width are not normally distributed, while Virginica is normally distributed. 

### Sepal Length

#### Setosa Sepal Length

![setpeth](https://user-images.githubusercontent.com/35706109/39275055-ce7ba4ee-48db-11e8-9518-f9c3f04fac96.png)

![setpetq](https://user-images.githubusercontent.com/35706109/39275060-d1d57ec6-48db-11e8-8915-d5393c587fbb.png)

The plots and the Shapiro-Wilk test of Setosa sepal length suggests that the data is normally distributed, *w = .978, p= .460.*

#### Virginica Sepal Length

![virpetlh](https://user-images.githubusercontent.com/35706109/39275249-92c3f6da-48dc-11e8-8e24-64f56c695bb9.png)

![virpetlq](https://user-images.githubusercontent.com/35706109/39275255-94f87e12-48dc-11e8-8673-6f5d871739dd.png)

The histogram is right skewed but the Shapiro-Wilk test of Virginica sepal length suggests that the data is normally distributed, *w = .971, p= .258.*

#### Versicolor Sepal Length

![verhist](https://user-images.githubusercontent.com/35706109/39275472-4bb7d9d6-48dd-11e8-9d4f-f45bf6cacfaa.png)

![verq](https://user-images.githubusercontent.com/35706109/39275480-4f8450e4-48dd-11e8-80bd-d2d3d4a2ad72.png)

The histogram looks normal and the Shapiro-Wilk test of Versicolor sepal length suggests that the data is normally distributed, *w = .978, p= .465.*

The Sepal length of all flowers is normally distributed. 

### Sepal Width

#### Setosa Sepal Width
![setsep](https://user-images.githubusercontent.com/35706109/39275679-0b92a790-48de-11e8-9d46-9cddd7b2f07a.png)

![setsepq](https://user-images.githubusercontent.com/35706109/39275683-0ddedb7c-48de-11e8-89d4-daa96cd3aa2c.png)

The plots looks normal and the Shapiro-Wilk test of Setosa sepal width suggests that the data is normally distributed, *w = .969, p= .205.*

#### Virginica Sepal Width
![virh](https://user-images.githubusercontent.com/35706109/39275834-a84a8fbc-48de-11e8-8ecc-9dfff915f5ce.png)

![virq](https://user-images.githubusercontent.com/35706109/39275838-aa632598-48de-11e8-8911-db278046c006.png)

The histogram is left-skewed but the Shapiro-Wilk test of Virginica sepal width suggests that the data is normally distributed, *w = .967, p= .180.*

#### Versicolor Sepal Width

![verh](https://user-images.githubusercontent.com/35706109/39276004-5b19f9ca-48df-11e8-8c0d-a393d865eb74.png)

![verq](https://user-images.githubusercontent.com/35706109/39276009-5e18127e-48df-11e8-83a4-27a7deb78c18.png)

he histogram is left-skewed but the Shapiro-Wilk test of Versicolor sepal width suggests that the data is normally distributed, *w = .974, p= .338.*

The sepal width of all flower types are normally distributed. 

### Multivariate distribution

Above, we looked at the distribution of a single variable at a time, called univariate distribution. The plot below is a Parallel Coordinates plot using Pandas visualation library. 

Each datapoint is represented on the plot as a single line across all the dependent variables. 


![pc](https://user-images.githubusercontent.com/35706109/39276283-550bf8f2-48e0-11e8-9203-66c60485de09.png)

Starting from the left of the graph, we can see that all three species appear to have relatively similar sepal lengths and widths. Differences begin to appear, however, when it comes to the Petal variables. Setosa petal length and width is distinctly less than the others. 

In the next chapter, we examine this in more detail by using plots and statistics to look at the differences between the three flower types in more details. 


