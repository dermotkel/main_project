import pandas as pd
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


# get the iris data set directly from the below url. It includes headers
iris_url='https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
# pandas read csv from URL: http://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/
df = pd.read_csv(iris_url)
#divide the dataset into three new dataframes - https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

setosa=df[df['Name']=='Iris-setosa']
versicolor =df[df['Name']=='Iris-versicolor']
virginica =df[df['Name']=='Iris-virginica']

#Univariate Distribution

#print(df.head())
#sns.distplot(setosa.PetalLength, norm_hist=False)
#sns.distplot(setosa.PetalWidth, norm_hist=False)
#sns.distplot(versicolor.SepalLength, norm_hist=False)
#sns.distplot(virginica.SepalLength, norm_hist=False)


#qqplot also shows that the data is normally distributed http://www.statsmodels.org/dev/generated/statsmodels.graphics.gofplots.ProbPlot.html
#sm.qqplot(versicolor.PetalWidth, line="s")
#sm.qqplot(setosa.PetalWidth, line="s")
#sm.qqplot(setosa.PetalLength, line="s")
#plt.show()

#print(stats.shapiro(setosa.SepalLength)) # Shapiro-wilks test for normality https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
#print(stats.normaltest(setosa.SepalLength))

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





import pandas as pd
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


# get the iris data set directly from the below url. It includes headers
iris_url='https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
# pandas read csv from URL: http://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/
df = pd.read_csv(iris_url)
#divide the dataset into three new dataframes - https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

setosa=df[df['Name']=='Iris-setosa']
versicolor =df[df['Name']=='Iris-versicolor']
virginica =df[df['Name']=='Iris-virginica']

# Univariate Distribution

#print(df.head())
#sns.distplot(setosa.PetalLength, norm_hist=False)
#sns.distplot(setosa.PetalWidth, norm_hist=False)
#sns.distplot(versicolor.SepalLength, norm_hist=False)
#sns.distplot(virginica.SepalLength, norm_hist=False)
#plt.show()

#qqplot also shows that the data is normally distributed http://www.statsmodels.org/dev/generated/statsmodels.graphics.gofplots.ProbPlot.html
#sm.qqplot(versicolor.PetalWidth, line="s")
#sm.qqplot(setosa.PetalWidth, line="s")
#sm.qqplot(setosa.PetalLength, line="s")

#print(stats.shapiro(setosa.SepalLength)) # Shapiro-wilks test for normality https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
#print(stats.normaltest(setosa.SepalLength))

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

plt.show()

corr = df.corr()
print(corr)

corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap="plasma")
plt.show()