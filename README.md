# Main Project 2018: Programming and Scripting - Dermot Kelleher

# Table of Contents

- [1. Introduction](https://github.com/dermotkel/main_project/blob/master/README.md#introduction)
  - [1.1 The Iris Dataset](https://github.com/dermotkel/main_project/blob/master/README.md#iris-data-set)
  - [1.2 Variables](https://github.com/dermotkel/main_project/blob/master/README.md#12-variables)
  - [1.3 Research Questions and Hypotheses](https://github.com/dermotkel/main_project/blob/master/README.md#13-research-questions-and-hypotheses)
- [2. Distribution of the Data](https://github.com/dermotkel/main_project/blob/master/README.md#2-distribution-of-the-data)
  - [2.1 Petal Length Distribution](https://github.com/dermotkel/main_project/blob/master/README.md#21-petal-length-distribution)
   - [2.1.1 Setosa Petal Length](https://github.com/dermotkel/main_project/blob/master/README.md#211-setosa-petal-length)
   - [2.1.2 Virginica Petal Length](https://github.com/dermotkel/main_project/blob/master/README.md#212-virginica-petal-length)
   - [2.1.3 Versicolor Petal Length](https://github.com/dermotkel/main_project/blob/master/README.md#213-versicolor-petal-length)
- [2.2 Petal Width Distribution](https://github.com/dermotkel/main_project/blob/master/README.md#22-petal-width-distribution)
   - [2.2.1 Setosa Petal Width](https://github.com/dermotkel/main_project/blob/master/README.md#221-setosa-petal-width)
   - [2.2.2 Virginica Petal Width](https://github.com/dermotkel/main_project/blob/master/README.md#222-virginica-petal-width)
   - [2.2.3 Versicolor Petal Width](https://github.com/dermotkel/main_project/blob/master/README.md#223-versicolor-petal-width)
- [2.3 Sepal Length Distribution](https://github.com/dermotkel/main_project/blob/master/README.md#23-sepal-length-distribution)
   - [2.3.1 Setosa Sepal Length](https://github.com/dermotkel/main_project/blob/master/README.md#231-setosa-sepal-length)
   - [2.3.2 Virginica Sepal Length](https://github.com/dermotkel/main_project/blob/master/README.md#232-virginica-sepal-length)
   - [2.3.3 Versicolor Sepal Length](https://github.com/dermotkel/main_project/blob/master/README.md#233-versicolor-sepal-length)
- [2.4 Sepal Width Distribution](https://github.com/dermotkel/main_project/blob/master/README.md#24-sepal-width-distribution)
   - [2.4.1 Setosa Sepal Width](https://github.com/dermotkel/main_project/blob/master/README.md#241-setosa-sepal-width)
   - [2.4.2 Virginica Sepal Width](https://github.com/dermotkel/main_project/blob/master/README.md#242-virginica-sepal-width)
   - [2.4.3 Versicolor Sepal Width](https://github.com/dermotkel/main_project/blob/master/README.md#243-versicolor-sepal-width)
- [2.5 Multivariate Distribution](https://github.com/dermotkel/main_project/blob/master/README.md#25-multivariate-distribution)
- [3 Differences between species](https://github.com/dermotkel/main_project/blob/master/README.md#3-differences-between-species)
   - [3.1 Petal Length](https://github.com/dermotkel/main_project/blob/master/README.md#31-petal-length)
   - [3.2 Petal Width](https://github.com/dermotkel/main_project/blob/master/README.md#32-petal-width)
   - [3.3 Sepal Length](https://github.com/dermotkel/main_project/blob/master/README.md#33-sepal-length)
   - [3.4 Sepal Width](https://github.com/dermotkel/main_project/blob/master/README.md#34-sepal-width)
- [5 Results](https://github.com/dermotkel/main_project/blob/master/README.md#5-results)
- [6 Bibliography](https://github.com/dermotkel/main_project/blob/master/README.md#6-bibliography)
  

## 1. Introduction

A new data analysis team is being created in our company and my manager has tasked me with training the new team members. The purpose of this study is to introduce my colleagues to the core concepts of data analysis with Python by performing an analysis of the famous Iris Dataset using key python libraries, such as Pandas, Seaborn and Scipy. This study will demonstrate how to perform statistical analysis and data visualisation. We will analyse the Iris Dataset by investigating the following: The distribution of data, differences between the independent variables and correlation between variables. 

### 1.1 Iris Dataset

There are 150 data points in the Iris dataset: 50 for each species of Iris. It contains 5 variables. 'Name' is a categorical variable which denotes the different species of Iris. It has three levels: Setosa, Virginica and Versicolor. There are four ratio variables (all measured in centimetres): Petal height, petal width, sepal height and sepal width (Dua, D. and Karra Taniskidou, n.d.).

### 1.2 Variables

The independent variable is the Name categorical variable with its four levels: Setosa, Virginica and Setosa. This is also called a Predictor variable. We want to observe how the other variables in the study are affected by the independent variables. 

The four ratio variables outlined above are the depedent variables in this study (also called outcome variables). These are the variables that we expect may be affected or changed by the indepdent variables (Laerd statistics, n.d.). 

### 1.3 Research Questions and Hypotheses

In this section we will lay out some research questions. These will be the focus of the srudy. We will answer each one in the Results chapter of this study. 

1. Are the three species normally distributed across all dependent variables?

2. Is there a significant difference between the three species in terms of petal length, petal width, sepal length and sepal width ?

3. Is there a postive correlation between sepal length and petal length?

We shall also make some hypotheses about the Iris Dataset. A hypothesis is simply an 'educated quess' we make at the beginning of a study on what we expect to find (Statistics How To, n.d.).

A effective way of making a hypothesis is by visually inspecting the data and making predictions. Firstly, it is important to find out the differences between a sepal and a petal. The sepal is on the outside and the petal is on the inside, closer to the centre of the flower. The below sideview of an Iris shows the difference clearly. 

![SepalPetal](https://raw.githubusercontent.com/ritchieng/machine-learning-dataschool/master/images/03_iris.png "Sepal and Petal")

![irisflowers](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png "Iris Flowers")

The above picture is not perfect, of course, as they are not all taken from the same distance/postion. It is therefore, difficult to judge differences in size. However, we can make the following observations: The petals on the Setosa appear to be significantly smaller than the other species. The sepals appear to be of a similar length for each of the species. 

The hypotheses are as follows: 

4. The petal width and petal length of the Setosa are significantly smaller than the other species. 

5. The sepal length of all species is similar.

In the next chapter, we will examine the distribution of each flower species across each of the four dependent variables. In chapter three we will examine differences between the Iris Species. In chapter four, we will look for correlation in the Iris dataset. Finally, in chapter five, we will present our results. 

The Python code used in this study is available in the project.py file in this repository. Start at the beginning of the file. The relevant code is grouped under the corresponding chapter heading. 


## 2. Distribution of the Data

The normal distribution is an important concept in data analysis. A histogram representing a normal distribution will have a similar mean and median. It will also be symmetrical. A normal distribution should look like a bell-curve: 

![Bellcurve](https://ds055uzetaobb.cloudfront.net/image_optimizer/1dbcc5a80e3fb541aa4678fcff58bb26ca717902.png "Bell Curve")

If a variable has a normal distribution, we may be able to use parametric statistical tests. If it is not normally distributed, we can only use non-parametric tests.

We will now examine the distribution of all dependent variables across all species. Histograms and QQ Plots will be created to visually inspect the data. A histogram divides the continuous variable into bins at equal intervals. The height of each bin indicates the count of datapoints in it. Intervals with more datapoints are then higher. 

A QQ Plot plots each datapoint along a line. If the variables are tightly clustered around the line, the variable is normally distributed. The QQ Plot is created using the Statsmodels library and the Histogram is created using the Seaborn library. We will also use the Scipy library to perform a Shapiro-Wilk test for normality. 

### 2.1 Petal Length Distribution

#### 2.1.1 Setosa Petal Length

![setosapetalhist](https://user-images.githubusercontent.com/35706109/39267290-4b9029c2-48c4-11e8-95d9-30ad9b286770.png)


![setpetalqq](https://user-images.githubusercontent.com/35706109/39267890-2050f8c0-48c6-11e8-82a2-48fb5d8b1397.png)

The histogram appears to be normally distributed, though is slightly left-skewed. From the statsmodel library we can also create a normal QQ plot, another usual visual tool to check if data is normally distributed. If the data is in a straight line, then the data is normally distributed.

As we can see in the above QQ Plot, the Setosa petal length data follows a straight line though it does deviate at the very top and bottom.

While the histogram and QQ plot suggest that it is normally distributed. Using the stats module from the Scipy library in Python, we can perform a Shapiro-Wilk test to test for normality. The null hypothesis is that the data is normally distributed. In other words, if the p-value is greater than our chosen alpha value .05, then we accept the null hypotheses and the data is normally distributed. 

A Shapiro-Wilk test of Setosa petal length suggests that the data is normally distributed, *w = .955, p= .055.*

#### 2.1.2 Virginica Petal Length

![virginica_hist](https://user-images.githubusercontent.com/35706109/39269731-8a2ee68a-48cb-11e8-9d07-968a57984201.png)

![virgqq](https://user-images.githubusercontent.com/35706109/39269790-bc060fee-48cb-11e8-94ac-0d851c50c31f.png)

The histogram is slightly right-skewed and uniform in the middle. The middle bars are of a similar height. The QQ plot suggests that it is normally distributed, though with some small deviations. 

A Shapiro-Wilk test of Virginica petal length suggests that the data is normally distributed, *w = .962, p= .110.*

#### 2.1.3 Versicolor Petal Length

![verpetlen](https://user-images.githubusercontent.com/35706109/39270216-47843dc4-48cd-11e8-8998-8615a323a5f7.png)

![verpetlenq](https://user-images.githubusercontent.com/35706109/39270218-4a779ae4-48cd-11e8-8324-2165f844e865.png)

The histogram shows a strong left-skew or tail in this variable. However, the QQ Plot does follow a straight line. This demonstrates why it is important to use more than one plot to examine the distribution of data. 

A Shapiro-Wilk test of Versicolor petal length suggests that the data is normally distributed, *w = .966, p= .158.*

As can be seen above, the petal length of all three species of Iris are normally distributed. 

### 2.2 Petal Width Distribution

#### 2.2.1 Setosa Petal Width

![setpetwidthhist](https://user-images.githubusercontent.com/35706109/39271696-a56221fa-48d1-11e8-94dd-ca8f4e12d056.png)

![setpetwidthq](https://user-images.githubusercontent.com/35706109/39271707-abc25498-48d1-11e8-93ec-c3b53bf10473.png)

The histogram demonstrates that the Setosa petal width is strongly right-skewed and may not be normally distributed. The QQ Plot is not useful as so many variables are clustered in one area of the plot. 

A Shapiro-Wilk test of Setosa petal width suggests that the data is **not** normally distributed, *w = .814, p= < .000.*

#### 2.2.2 Virginica Petal Width

![virpetwh](https://user-images.githubusercontent.com/35706109/39274364-a357a7ba-48d9-11e8-914c-4f47f2084013.png)

![virpetwq](https://user-images.githubusercontent.com/35706109/39274369-a59e5730-48d9-11e8-866f-61e9f9782fce.png)

The histogram is skewed right, but the QQ plot looks relatively straight.

A Shapiro-Wilk test of Virginica petal width suggests that the data is normally distributed, *w = .960, p= .087.*

#### 2.2.3 Versicolor Petal Width

![verpetwh](https://user-images.githubusercontent.com/35706109/39274585-5fbe37fc-48da-11e8-8079-d8644137b9cd.png)

![verpetwq](https://user-images.githubusercontent.com/35706109/39274588-6215df1e-48da-11e8-9394-a914335c0662.png)

The histogram shows that the variable is bimodal (has two distinct peaks) and may not be normally distributed.

A Shapiro-Wilk test of Versicolor petal width suggests that the data is *not* normally distributed, *w = .948, p= .027.*

Setosa and Versicolor petal widths are not normally distributed, while Virginica is normally distributed. 

### 2.3 Sepal Length Distribution

#### 2.3.1 Setosa Sepal Length

![setpeth](https://user-images.githubusercontent.com/35706109/39275055-ce7ba4ee-48db-11e8-9518-f9c3f04fac96.png)

![setpetq](https://user-images.githubusercontent.com/35706109/39275060-d1d57ec6-48db-11e8-8915-d5393c587fbb.png)

The plots and the Shapiro-Wilk test of Setosa sepal length suggests that the data is normally distributed, *w = .978, p= .460.*

#### 2.3.2 Virginica Sepal Length

![virpetlh](https://user-images.githubusercontent.com/35706109/39275249-92c3f6da-48dc-11e8-8e24-64f56c695bb9.png)

![virpetlq](https://user-images.githubusercontent.com/35706109/39275255-94f87e12-48dc-11e8-8673-6f5d871739dd.png)

The histogram is right-skewed but the Shapiro-Wilk test of Virginica sepal length suggests that the data is normally distributed, *w = .971, p= .258.*

#### 2.3.3 Versicolor Sepal Length

![verhist](https://user-images.githubusercontent.com/35706109/39275472-4bb7d9d6-48dd-11e8-9d4f-f45bf6cacfaa.png)

![verq](https://user-images.githubusercontent.com/35706109/39275480-4f8450e4-48dd-11e8-80bd-d2d3d4a2ad72.png)

The histogram looks normal and the Shapiro-Wilk test of Versicolor sepal length suggests that the data is normally distributed, *w = .978, p= .465.*

The Sepal length of all species is normally distributed. 

### 2.4 Sepal Width Distribution

#### 2.4.1 Setosa Sepal Width
![setsep](https://user-images.githubusercontent.com/35706109/39275679-0b92a790-48de-11e8-9d46-9cddd7b2f07a.png)

![setsepq](https://user-images.githubusercontent.com/35706109/39275683-0ddedb7c-48de-11e8-89d4-daa96cd3aa2c.png)

The plots look normal and the Shapiro-Wilk test of Setosa sepal width suggests that the data is normally distributed, *w = .969, p= .205.*

#### 2.4.2 Virginica Sepal Width
![virh](https://user-images.githubusercontent.com/35706109/39275834-a84a8fbc-48de-11e8-8ecc-9dfff915f5ce.png)

![virq](https://user-images.githubusercontent.com/35706109/39275838-aa632598-48de-11e8-8911-db278046c006.png)

The histogram is left-skewed but the Shapiro-Wilk test of Virginica sepal width suggests that the data is normally distributed, *w = .967, p= .180.*

#### 2.4.3 Versicolor Sepal Width

![verh](https://user-images.githubusercontent.com/35706109/39276004-5b19f9ca-48df-11e8-8c0d-a393d865eb74.png)

![verq](https://user-images.githubusercontent.com/35706109/39276009-5e18127e-48df-11e8-83a4-27a7deb78c18.png)

he histogram is left-skewed but the Shapiro-Wilk test of Versicolor sepal width suggests that the data is normally distributed, *w = .974, p= .338.*

The sepal width of all species are normally distributed. 

The below tables shows if the variable is normally distributed (YES) or not normally distributed (NO).


|   | **Petal Length** | **Petal Width**  | **Sepal Length** | **Sepal Width** |
|---|---|---|---|---|
| **Setosa**  | Yes  | No  | Yes  | Yes  |
| **Virginica**   | Yes  | Yes  |Yes   | Yes  |
| **Versicolor**  | Yes  | No  | Yes  | Yes  |

### 2.5 Multivariate Distribution

Above, we looked at the distribution of a single variable at a time, called univariate distribution. The plot below is a Parallel Coordinates plot using Pandas visualation library. 

Each datapoint is represented on the plot as a single line across all the dependent variables. 

![pc](https://user-images.githubusercontent.com/35706109/39276283-550bf8f2-48e0-11e8-9203-66c60485de09.png)

Starting from the left of the plot, we can see that all three species appear to have relatively similar sepal lengths and widths. Differences begin to appear, however, when it comes to the petal variables. Setosa petal length and width is distinctly less than the others. 

In the next chapter, we examine this in more detail by using plots and statistics to look at the differences between the three species in more detail. 

## 3 Differences between species

We will now now look at each variable: Petal length, petal width, sepal length and sepal width and see if there are differences between the species. We will use plots and statistical analysis. 

### 3.1 Petal Length

![swarmpw](https://user-images.githubusercontent.com/35706109/39328966-e6242026-4994-11e8-88d3-06b8b8e14cc2.png)

The above swarmplot created using Seaborn compares the petal length of each species by placing each datapoint on the plot. Datapoints with a similar value are placeed beside each other making the cluster appear wider. 

The Setosa is much wider and shorter, while Virginica and Versicolor are more disperse. Setosa is clearly smaller with no overlap with the others. Virginica and Versicolor have only a slight overlap. 

The pandas dataframe.describe() functions shows us the means of petal length for Setosa (1.46cm), Versicolor (4.26cm) and Virginica (5.55cm). This is demonstrated in the barplot made using Seaborn below:

![barplot](https://user-images.githubusercontent.com/35706109/39329947-d823d1e4-4997-11e8-9ad4-c3c05de12249.png)

The Setosa petal length seems significantly smaller than the other two species. 

![figure_1](https://user-images.githubusercontent.com/35706109/39333466-e6052938-49a2-11e8-911b-39a1b85a7221.png)

The boxplot created using Seaborn above shows the differences between the species more clearly. The black diamonds are outliers. The whiskers show the range of the data. The middle line is the medium and the box is the interquartile range (it contains the middle 50% of the data). 

We will now perform a one-way ANOVA test to see if these differences we can observe are statistically significant (Marsja, 2016). The one-way has several assumptions (Laerd Statistics, nd.). Our data is continuos. As we saw in the last chapter, the petal length is normally distributed. Finally, there should be a homogeneity of variances which we can test by performing a Levene's test using Scipy (Statistics Solutions, 2018). The null hypothesis is that there is a homogenity of variances. So we reject the null hypothesis if the p-value is less than our alpha-value of .05.

A Levene's test shows that petal length does not meet the homogenity of variances assumption, *f = 19.72, p= <.000.*

However, Anova is robust if this assumption is not met if the size of the groups are equal (Statistics Solutions, nd.). All of our groups have 50 datapoints. We will, therefore, use ANOVA with the above caveat and primarily to show how it works in Python. 

A one-way Anova performed using Scipy shows that there is a significant difference in the petal length between at least two two flower-types, *f = 1179, p= <.000.*

An ANOVA tells us that at least one variable is different from another. A Tukey *post hoc* test using StatsModels will show which species are actually significantly different (Hamelg, 2015). The null hypothesis is that all species are equal. I include a screenshot from the output below:

![tukey](https://user-images.githubusercontent.com/35706109/39333292-42766d2c-49a2-11e8-8163-9caad8b49284.PNG)

We reject the null hypothesis in all instances. So, the petal length is difference across all species. 

### 3.2 Petal Width

![petalwidthswarm](https://user-images.githubusercontent.com/35706109/39334087-28b71d98-49a5-11e8-9fd8-526f60b9e0ea.png)

![petalwidthbar](https://user-images.githubusercontent.com/35706109/39334090-2da7e68e-49a5-11e8-97f5-a27bfc76e289.png)

![petalwithbox](https://user-images.githubusercontent.com/35706109/39334095-3087fd30-49a5-11e8-9e1e-e4e5e9216c95.png)

The above three plots show, again, that the Setosa seems significantly different to the other species. The others overlap to a small degree. 

As seen in the previous chapter, two of the three petal width variables are not normally distributed. Therefore, we have to use the non-parametric alternative to the ANOVA, called the Kruskal-Wallis Test using Scipy. The test finds that at least one of the species is significantly different to another *χ2 = 131, p = <.000*. 

At this stage, we would normally use a *post hoc* Dunn's test to check which of the species are different. Similar to how we used the Tukey test with ANOVA. This is not easily implemented in Python at present. 

### 3.3 Sepal Length

![seplswarm](https://user-images.githubusercontent.com/35706109/39335263-36d1511e-49aa-11e8-833b-401aea163aeb.png)

![seplenbar](https://user-images.githubusercontent.com/35706109/39335270-3c7f0926-49aa-11e8-8322-2564a2083b93.png)

![seplbox](https://user-images.githubusercontent.com/35706109/39335275-3f991732-49aa-11e8-8132-ee6d7c39344b.png)

A one-way Anova performed using Scipy shows that there is a significant difference in the sepal length between at least two two species, *f = 119, p= <.000.*

A screenshot from the Tukey *post hoc test* carried out with StatsModels is below:

![tukey](https://user-images.githubusercontent.com/35706109/39335709-144f9450-49ac-11e8-8c15-fc7fab068ecb.PNG)

We reject the null hypothesis in all instances. So, the sepal length is different across all species. 

### 3.4 Sepal Width


![sepwswarm](https://user-images.githubusercontent.com/35706109/39335995-44465d14-49ad-11e8-8eeb-747383833214.png)

![sepwbar](https://user-images.githubusercontent.com/35706109/39335999-4682fa10-49ad-11e8-8aca-205cda12849f.png)

![sepwbox](https://user-images.githubusercontent.com/35706109/39336002-489ce680-49ad-11e8-87e6-fe36bd70def7.png)

It is interesting to note that Setosa has the widest Sepals of the three species. In all other variables, it appears to be smaller. 

A one-way Anova performed using Scipy shows that there is a significant difference in the sepal width between at least two species, *f = 47.3, p= <.000.*

A screenshot from the Tukey *post hoc* test carried out with StatsModels is below:

![tukey](https://user-images.githubusercontent.com/35706109/39336006-4b99d082-49ad-11e8-93c1-e63e665e9e1a.PNG)

We reject the null hypothesis in all instances. So, the sepal width is different across all species 

## 4 Correlation

Finally, we will look at correlation between variables within the dataset. Correlation looks at the relationship between two variables. It is measured on a scale from -1 to 1. A correlation of - 1 means that the two variables have a perfect negative linear relationship. In other words, if one variable increases, the other will always decrease. If they have a correlation of 1, they have a perfect positive linear relationship. They move in the same direction. A correlation of 0 means that there is no relationship. 

The pandas .corr() function gives the Pearson Correlation coefficent of the dataset. The output is below: 

![capture](https://user-images.githubusercontent.com/35706109/39337337-53a0feac-49b4-11e8-93c3-2e7a9cee2711.PNG)

It should be noted, however, that the Pearson's r is a parametric test. It requires that the two variables are normally distributed. If the variables do not meet this requirment, we have to use a non-parametric test, such as Spearman's rho. As we are comparing the variables without differentiating them by their species, we have not checked if they are normally distributed. 

We could perform an analysis as we did in chapter 2, However, below i will show a Correlation Matrix Heatmap showing the Pearson's r and Spearman's rho correlations of the data. You will see that both results are similar, though the non-parametric shows a slightly weaker correlation.

![pearson](https://user-images.githubusercontent.com/35706109/39337334-4e8e7d90-49b4-11e8-8f13-ba418f16ce89.png)

![spearman](https://user-images.githubusercontent.com/35706109/39337346-5b2092dc-49b4-11e8-8d0f-706aa1496658.png)


It is interesting that there is a strong positive correlation between petal length and petal width. Flowers with longer petals also have wider petals. However, there appears to be no linear relationship between sepal length and sepal width. 

We can also see that there is a strong positive correlation between petal length and sepal length. This relationship is also shown clearly in the jointplot created with Seaborn below. Spearman's rho is used as the petal length histogram is bimodal and may not be normally distributed.

![jointplot](https://user-images.githubusercontent.com/35706109/39337352-63d6a614-49b4-11e8-8301-bddaf98ffc65.png)

## 5 Results

We will now answer the research questions and hypotheses posed in the introduction. 

**1. Are the three species normally distributed across all dependent variables?**

|   | **Petal Length** | **Petal Width**  | **Sepal Length** | **Sepal Width** |
|---|---|---|---|---|
| **Setosa**  | Yes  | No  | Yes  | Yes  |
| **Virginica**   | Yes  | Yes  |Yes   | Yes  |
| **Versicolor**  | Yes  | No  | Yes  | Yes  |

The chart above shows that all species are normally distributed except for Setosa petal width and Versicolor petal width.

**2. Is there a significant difference between the three species in terms of petal length, petal width, sepal length and sepal width ?**

![pc](https://user-images.githubusercontent.com/35706109/39276283-550bf8f2-48e0-11e8-9203-66c60485de09.png)

Virginica has the longest and widest petals, followed by Versicolor. Setosa has the smallest.

Virginica has the longest sepals, followed by versicolor and then Setosa, but the differences are smaller. interestingly, Setosa has the widest sepals followed closely by Virginica and finally Versicolor.

**3. Is there a postive correlation between sepal length and petal length?**

![jointplot](https://user-images.githubusercontent.com/35706109/39337352-63d6a614-49b4-11e8-8301-bddaf98ffc65.png)

There is a strong positive correlation between sepal length and petal length


**4. The petal width and petal length of the Setosa are significantly smaller than the other species.**

![scatter](https://user-images.githubusercontent.com/35706109/39338697-59a5f70a-49bc-11e8-9980-001cc93533f7.png)

Using swarmplots, barplots and boxplots, as well as ANOVA and Kruskal-Wallis tests, we saw that Setosa petals are significantly smaller than the other species.The above scatterplot created using Pandas clearly shows this difference. 


**5. The sepal length of all flowers is similar.**

![seplenbar](https://user-images.githubusercontent.com/35706109/39335270-3c7f0926-49aa-11e8-8322-2564a2083b93.png)

The barplot above shows that there is a slight difference in the average sepal length across all species and an ANOVA confirmed these differences as significant. 

## 6 Bibliography

Dua, D. and Karra Taniskidou, E. (n.d.). UCI Machine Learning Repository. Retrieved April 18, 2018, from http://archive.ics.uci.edu/ml

Hamelg. (2015). Python for Data Analysis Part 26: Analysis of Variance (ANOVA). Retrieved April 20, 2018, from http://hamelg.blogspot.ie/2015/11/python-for-data-analysis-part-16_23.html

Laerd Statistics. (n.d.). Types of Variable. Retrieved April 20, 2018, from https://statistics.laerd.com/statistical-guides/types-of-variable.php

Marsja, E. (2016). Four ways to conduct one-way ANOVAs with Python. Retrieved April 10, 2018, from https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/

Statistics Solutions. (2018). The Assumption of Homogeneity of Variance. Retrieved April 20, 2018, from http://www.statisticssolutions.com/the-assumption-of-homogeneity-of-variance/

Statistics How To. (n.d.). Hypothesis Testing. Retrieved April 20, 2018, from http://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/


