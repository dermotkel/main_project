import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
sns.set_style("darkgrid")
from pandas.plotting import andrews_curves
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from pandas.plotting import lag_plot
from pandas.plotting import radviz
from pandas.plotting import parallel_coordinates


# get the iris data set directly from the below url. It includes headers
iris_url='https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
# pandas read csv from URL: http://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/
df = pd.read_csv(iris_url)
#divide the dataset into three new dataframes - https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

setosa=df[df['Name']=='Iris-setosa']
versicolor =df[df['Name']=='Iris-versicolor']
virginica =df[df['Name']=='Iris-virginica']

#Multivariate distribution

#parallel_coordinates(df, "Name")
#plt.title('Iris Species Parallel Coordinates')
#plt.ylabel('Centimetres')

#plt.show()

# Gives a good general look at the distribution of the data

#Univariate Distribution

#print(stats.shapiro(setosa.SepalLength)) # Shapiro-wilks test for normality https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
#qqplot also shows that the data is normally distributed http://www.statsmodels.org/dev/generated/statsmodels.graphics.gofplots.ProbPlot.html

#Setosa Petal Length distribution

#sns.distplot(setosa.PetalLength, hist=True, rug=True, kde=False)

#plt.title('Setosa Petal Length Histogram')
#plt.xlabel('Petal Length in cm')
#plt.ylabel('Frequency')

#sm.qqplot(setosa.PetalLength, line="s")
#plt.title('Setosa Petal Length Normal QQ Plot')

#print(stats.shapiro(setosa.PetalLength))
# Shapiro test is greater than .05 so it is normally distributed

#Virginica Petal Length distribution

#sns.distplot(virginica.PetalLength, hist=True, rug=True, kde=False)

#plt.title('Virginica Petal Length Histogram')
#plt.xlabel('Petal Length in cm')
#plt.ylabel('Frequency')

#sm.qqplot(virginica.PetalLength, line="s")
#plt.title('Virginica Petal Length Normal QQ Plot')
#print(stats.shapiro(virginica.PetalLength))
# Shapiro-wilks is greater than .05, so  normally distributed

#Versicolor Petal Length distribution

#sns.distplot(versicolor.PetalLength, hist=True, rug=True, kde=False)

#plt.title('Versicolor Petal Length Histogram')
#plt.xlabel('Petal Length in cm')
#plt.ylabel('Frequency')

#sm.qqplot(versicolor.PetalLength, line="s")
#plt.title('Versicolor Petal Length Normal QQ Plot')
#print(stats.shapiro(versicolor.PetalLength))
# Shapiro test is greater than .o5 so normally distributed

# All normally distributed, but Levine test
##print(stats.levene(setosa.PetalLength, virginica.PetalLength, versicolor.PetalLength))
#shows it does not meet variance assumption, however groups are of equal size, so we can use Anova
#http://www.statisticssolutions.com/the-assumption-of-homogeneity-of-variance/

#Setosa Petal Width distribution

#sns.distplot(setosa.PetalWidth, hist=True, rug=True, kde=False, bins=4)

#plt.title('Setosa Petal Width Histogram')
#plt.xlabel('Petal Width in cm')
#plt.ylabel('Frequency')

#sm.qqplot(setosa.PetalWidth, line="s")
#plt.title('Setosa Petal Width Normal QQ Plot')

#print(stats.shapiro(setosa.PetalWidth))

# Shapiro test is less than .05 so it is not normally distributed

#Virginica Petal Width distribution

#sns.distplot(virginica.PetalWidth, hist=True, rug=True, kde=False, bins=4)

#plt.title('Virginica Petal Width Histogram')
#plt.xlabel('Petal Width in cm')
#plt.ylabel('Frequency')

#sm.qqplot(virginica.PetalWidth, line="s")
#plt.title('Virginica Petal Width Normal QQ Plot')

#print(stats.shapiro(virginica.PetalWidth))

# Shapiro test is greater than .05 so it is normally distributed

#Versicolor Petal Width distribution

#sns.distplot(versicolor.PetalWidth, hist=True, rug=True, kde=False, bins=4)

#plt.title('Versicolor Petal Width Histogram')
#plt.xlabel('Petal Width in cm')
#plt.ylabel('Frequency')

#sm.qqplot(versicolor.PetalWidth, line="s")
#plt.title('Versicolor Petal Width Normal QQ Plot')

#print(stats.shapiro(versicolor.PetalWidth))

# Shapiro test is less than .05 so it is not normally distributed
# Not all groups are normall distrivuted, so we use Kruskal wallis

#print(stats.kruskal(setosa.PetalWidth, virginica.PetalWidth, versicolor.PetalWidth))

#Setosa Sepal Length distribution

#sns.distplot(setosa.SepalLength, hist=True, rug=True, kde=False)

#plt.title('Setosa Sepal Length Histogram')
#plt.xlabel('Sepal Length in cm')
#plt.ylabel('Frequency')

#sm.qqplot(setosa.SepalLength, line="s")
#plt.title('Setosa Sepal Length Normal QQ Plot')

#print(stats.shapiro(setosa.SepalLength))
# Shapiro test is greater than .05 so it is normally distributed

#Virginica Sepal Length distribution

#sns.distplot(virginica.SepalLength, hist=True, rug=True, kde=False)

#plt.title('Virginica Sepal Length Histogram')
#plt.xlabel('Sepal Length in cm')
#plt.ylabel('Frequency')

#sm.qqplot(virginica.SepalLength, line="s")
#plt.title('Virginica Sepal Length Normal QQ Plot')

#print(stats.shapiro(virginica.SepalLength))
# Shapiro test is greater than .05 so it is normally distributed

#Versicolor Sepal Length distribution

#sns.distplot(versicolor.SepalLength, hist=True, rug=True, kde=False)

#plt.title('Versicolor Sepal Length Histogram')
#plt.xlabel('Sepal Length in cm')
#plt.ylabel('Frequency')

#sm.qqplot(versicolor.SepalLength, line="s")
#plt.title('Virginica Sepal Length Normal QQ Plot')

#print(stats.shapiro(versicolor.SepalLength))
# Shapiro test is greater than .05 so it is normally distributed

# All normally distributed, but Levine test
#print(stats.levene(setosa.SepalLength, virginica.SepalLength, versicolor.SepalLength))
#shows it does not meet variance assumption as pvalue is less than .05, however groups are of equal size, so we can use Anova
#http://www.statisticssolutions.com/the-assumption-of-homogeneity-of-variance/
#print(stats.levene(setosa.PetalWidth, virginica.PetalWidth, versicolor.PetalWidth))
#print(stats.kruskal(setosa.PetalLength, virginica.PetalLength, versicolor.PetalLength))

#Setosa Sepal Width distribution

#sns.distplot(setosa.SepalWidth, hist=True, rug=True, kde=False)

#plt.title('Setosa Sepal Width Histogram')
#plt.xlabel('Sepal Width in cm')
#plt.ylabel('Frequency')

#sm.qqplot(setosa.SepalWidth, line="s")
#plt.title('Setosa Sepal Width Normal QQ Plot')

#print(stats.shapiro(setosa.SepalWidth))
# Shapiro test is greater than .05 so it is normally distributed

#Virginica Sepal Width distribution

#sns.distplot(virginica.SepalWidth, hist=True, rug=True, kde=False)

#plt.title('Virginica Sepal Width Histogram')
#plt.xlabel('Sepal Width in cm')
#plt.ylabel('Frequency')

#sm.qqplot(virginica.SepalWidth, line="s")
#plt.title('Virginica Sepal Width Normal QQ Plot')

#print(stats.shapiro(virginica.SepalWidth))
# Shapiro test is greater than .05 so it is normally distributed

#Versicolor Sepal Width distribution

#sns.distplot(versicolor.SepalWidth, hist=True, rug=True, kde=False)

#plt.title('Versicolor Sepal Width Histogram')
#plt.xlabel('Sepal Width in cm')
#plt.ylabel('Frequency')

#sm.qqplot(versicolor.SepalWidth, line="s")
#plt.title('Versicolor Sepal Width Normal QQ Plot')

#print(stats.shapiro(versicolor.SepalWidth))
# Shapiro test is greater than .05 so it is normally distributed

# All normally distributed and Levine test
#print(stats.levene(setosa.SepalWidth, virginica.SepalWidth, versicolor.SepalWidth))
#shows it does meet variance assumption as pvalue is greater than .05,  so we can use Anova
#http://www.statisticssolutions.com/the-assumption-of-homogeneity-of-variance/




#Bivariate distribution
#sns.jointplot(x="SepalWidth", y="SepalLength", data=setosa, kind="reg") # Youcan change the statistics and shos the correlation using Pearson as it is normally distrubuted ~ https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot
#sns.jointplot(x="SepalWidth", y="SepalLength", data=setosa, kind="kde")
#sns.jointplot(x="SepalWidth", y="SepalLength", data=virginica, kind="reg")
#sns.jointplot(x="SepalWidth", y="SepalLength", data=virginica, kind="kde")
#sns.jointplot(x="SepalWidth", y="SepalLength", data=versicolor, kind="reg")
#sns.jointplot(x="SepalWidth", y="SepalLength", data=versicolor, kind="kde")
#sns.jointplot(x="PetalWidth", y="PetalLength", data=setosa, kind="reg")
#sns.jointplot(x="PetalWidth", y="PetalLength", data=setosa, kind="kde")
#print(stats.shapiro(setosa.PetalWidth))
#print(stats.shapiro(setosa.PetalWidth))


#Catrgorical data - scatterplot



#print(df.describe()) 


#sns.swarmplot(x="Name", y="SepalWidth", data=df, palette="bright") # a Swarmplot - https://seaborn.pydata.org/tutorial/categorical.html

#Distribution of observations within categories 

#sns.boxplot(x="Name", y="SepalLength", data=df)
#sns.swarmplot(x="Name", y="SepalLength", data=df, color="white")


#sns.barplot(y="Name", x="SepalLength", data=df) # https://seaborn.pydata.org/generated/seaborn.barplot.html


#andrews_curves(df, 'Name')
#plt.show()

#mod = ols('SepalLength ~ Name', data=df).fit() #https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
                
#aov_table = sm.stats.anova_lm(mod, typ=2)
#print (aov_table)

#tukey = pairwise_tukeyhsd(endog=df.SepalLength, groups=df.Name, alpha=0.05) #http://www.statsmodels.org/dev/generated/statsmodels.sandbox.stats.multicomp.TukeyHSDResults.plot_simultaneous.html         
#print(tukey.summary())                                                      # http://hamelg.blogspot.ie/2015/11/python-for-data-analysis-part-16_23.html
#tukey.plot_simultaneous()

#plt.show()


#mod = ols('PetalLength ~ Name', data=df).fit() #https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/ - type 1,2,3 Anova - https://www.r-bloggers.com/anova-%E2%80%93-type-iiiiii-ss-explained/
                
#aov_table = sm.stats.anova_lm(mod, typ=2)
#print (aov_table)

#tukey = pairwise_tukeyhsd(endog=df.PetalLength, groups=df.Name, alpha=0.05) #http://www.statsmodels.org/dev/generated/statsmodels.sandbox.stats.multicomp.TukeyHSDResults.plot_simultaneous.html         
#print(tukey.summary())                                                      # http://hamelg.blogspot.ie/2015/11/python-for-data-analysis-part-16_23.html
#tukey.plot_simultaneous()

#corr = df.corr()
#print(corr)

#corr = df.corr()
#sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap="plasma")
#plt.show() # https://seaborn.pydata.org/generated/seaborn.heatmap.html -
#andrews_curves(df, 'Name')

#lag_plot(df.PetalLength) # https://pandas.pydata.org/pandas-docs/stable/visualization.html
