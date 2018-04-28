import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import seaborn as sns
from scipy import stats
from scipy.stats import spearmanr
import statsmodels.api as sm
sns.set_style("darkgrid")
from pandas.plotting import andrews_curves
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from pandas.plotting import parallel_coordinates


# get the iris data set directly from the below url. It includes headers.
iris_url='https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv'
# pandas read csv from URL. Cite: http://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/
df = pd.read_csv(iris_url)

# divide the dataset into three new dataframes by their species. Yhis makes comparisons easier. Cite: https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

setosa=df[df['Name']=='Iris-setosa']
versicolor =df[df['Name']=='Iris-versicolor']
virginica =df[df['Name']=='Iris-virginica']


# 2.1.1 Setosa Petal Length 

# Shoes how to make outlines on the bins. Cite: https://stackoverflow.com/questions/43080259/no-outlines-on-bins-of-matplotlib-histograms-or-seaborn-distplots
sns.distplot(setosa.PetalLength, hist=True, kde=False, hist_kws=dict(edgecolor="darkred", linewidth=.5)) 
plt.title('Fig. 1. Setosa Petal Length Histogram')
plt.xlabel('Petal Length in cm')
plt.ylabel('Frequency')
plt.show()

# QQ Plot created using Statsmodels. Cite: http://www.statsmodels.org/dev/generated/statsmodels.graphics.gofplots.qqplot.html
sm.qqplot(setosa.PetalLength, line="s")
plt.title('Fig 2. Setosa Petal Length Normal QQ Plot')
plt.show()

# A Shapiro-Wilk test for normality using Scipy. Cite: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
print(stats.shapiro(setosa.PetalLength))


# 2.1.2 Virginica Petal Length 

sns.distplot(virginica.PetalLength, hist=True, kde=False, hist_kws=dict(edgecolor="darkred", linewidth=.5))
plt.title('Fig. 3. Virginica Petal Length Histogram')
plt.xlabel('Petal Length in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(virginica.PetalLength, line="s")
plt.title('Fig. 4. Virginica Petal Length Normal QQ Plot')
print(stats.shapiro(virginica.PetalLength))


# 2.1.3 Versicolor Petal Length 

sns.distplot(versicolor.PetalLength, hist=True, kde=False, hist_kws=dict(edgecolor="darkred", linewidth=.5))
plt.title('Fig. 5. Versicolor Petal Length Histogram')
plt.xlabel('Petal Length in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(versicolor.PetalLength, line="s")
plt.title('Fig. 6. Versicolor Petal Length Normal QQ Plot')
plt.show()

print(stats.shapiro(versicolor.PetalLength))

# 2.2.1 Setosa Petal Width 

sns.distplot(setosa.PetalWidth, hist=True, hist_kws=dict(edgecolor="darkgreen", linewidth=.5), color="green", kde=False, bins=4)
plt.title('Fig. 7. Setosa Petal Width Histogram')
plt.xlabel('Petal Width in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(setosa.PetalWidth, line="s")
plt.title('Fig. 8. Setosa Petal Width Normal QQ Plot')
plt.show()

print(stats.shapiro(setosa.PetalWidth))

# 2.2.2 Virginica Petal Width 

sns.distplot(virginica.PetalWidth, hist=True, kde=False, bins=6, hist_kws=dict(edgecolor="darkgreen", linewidth=.5), color="green")
plt.title('Fig. 9. Virginica Petal Width Histogram')
plt.xlabel('Petal Width in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(virginica.PetalWidth, line="s")
plt.title('Fig. 10. Virginica Petal Width Normal QQ Plot')
plt.show()

print(stats.shapiro(virginica.PetalWidth))

# 2.2.3 Versicolor Petal Width 

sns.distplot(versicolor.PetalWidth, hist=True, kde=False, bins=6, hist_kws=dict(edgecolor="darkgreen", linewidth=.5), color="green")
plt.title('Fig. 11. Versicolor Petal Width Histogram')
plt.xlabel('Petal Width in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(versicolor.PetalWidth, line="s")
plt.title('Fig. 12. Versicolor Petal Width Normal QQ Plot')
plt.show()

print(stats.shapiro(versicolor.PetalWidth))

# 2.3.1 Setosa Sepal Length 

sns.distplot(setosa.SepalLength, hist=True, kde=False, hist_kws=dict(edgecolor="darkblue", linewidth=.5), color="blue")
plt.title('Fig. 13. Setosa Sepal Length Histogram')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(setosa.SepalLength, line="s")
plt.title('Fig. 14. Setosa Sepal Length Normal QQ Plot')
plt.show()

print(stats.shapiro(setosa.SepalLength))

# 2.3.2 Virginica Sepal Length 

sns.distplot(virginica.SepalLength, hist=True, kde=False, hist_kws=dict(edgecolor="darkblue", linewidth=.5), color="blue")
plt.title('Fig. 15. Virginica Sepal Length Histogram')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(virginica.SepalLength, line="s")
plt.title('Fig, 16, Virginica Sepal Length Normal QQ Plot')
plt.show()

print(stats.shapiro(virginica.SepalLength))

# 2.3.3 Versicolor Sepal Length

sns.distplot(versicolor.SepalLength, hist=True, kde=False, hist_kws=dict(edgecolor="darkblue", linewidth=.5), color="blue")
plt.title('Fig. 17. Versicolor Sepal Length Histogram')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(versicolor.SepalLength, line="s")
plt.title('Fig. 18. Versicolor Sepal Length Normal QQ Plot')
plt.show()

print(stats.shapiro(versicolor.SepalLength))


# 2.4.1 Setosa Sepal Width 

sns.distplot(setosa.SepalWidth, hist=True, kde=False, hist_kws=dict(edgecolor="darkorange", linewidth=.5), color="orange")
plt.title('Fig. 19. Setosa Sepal Width Histogram')
plt.xlabel('Sepal Width in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(setosa.SepalWidth, line="s")
plt.title('Fig. 20. Setosa Sepal Width Normal QQ Plot')
plt.show()

print(stats.shapiro(setosa.SepalWidth))

# 2.4.2 Virginica Sepal Width 

sns.distplot(virginica.SepalWidth, hist=True, kde=False, hist_kws=dict(edgecolor="darkorange", linewidth=.5), color="orange")
plt.title('Fig. 21. Virginica Sepal Width Histogram')
plt.xlabel('Sepal Width in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(virginica.SepalWidth, line="s")
plt.title('Fig. 22. Virginica Sepal Width Normal QQ Plot')
plt.show()

print(stats.shapiro(virginica.SepalWidth))

# 2.4.3 Versicolor Sepal Width 

sns.distplot(versicolor.SepalWidth, hist=True, kde=False, hist_kws=dict(edgecolor="darkorange", linewidth=.5), color="orange")
plt.title('Fig. 23. Versicolor Sepal Width Histogram')
plt.xlabel('Sepal Width in cm')
plt.ylabel('Frequency')
plt.show()

sm.qqplot(versicolor.SepalWidth, line="s")
plt.title('Fig. 24. Versicolor Sepal Width Normal QQ Plot')
plt.show()

print(stats.shapiro(versicolor.SepalWidth))


# 2.5 Multivariate distribution

# Plot shos a multivariate distribution and is created using Pandas. Cite: https://pandas.pydata.org/pandas-docs/stable/visualization.html#parallel-coordinates

parallel_coordinates(df, "Name")
plt.title('Iris Species Parallel Coordinates')
plt.ylabel('Centimetres')
plt.show()





## Petal Length

#sns.swarmplot(x="Name", y="PetalLength", data=df, palette="bright") # a Swarmplot - https://seaborn.pydata.org/tutorial/categorical.html
#plt.title('Fig. 25. Petal Length Swarmplot')
#plt.ylabel('Petal Length in cm')
#plt.show()

#print(setosa["PetalLength"].describe()) 
#print(virginica["PetalLength"].describe()) 
#print(versicolor["PetalLength"].describe()) 



#sns.barplot(x="Name", y="PetalLength", data=df, ci=None)
#plt.ylabel('Average Petal Length in cm')
#plt.title('Fig. 26. Petal Length Barplot')



#sns.boxplot(x="Name", y="PetalLength", data=df)
#plt.title('Fig. 27. Petal Length Boxplot')


#plt.show()

#print(stats.levene(setosa.PetalLength, virginica.PetalLength, versicolor.PetalLength))
#shows it does not meet variance assumption as pvalue is less than .05, however groups are of equal size, so we can use Anova
#http://www.statisticssolutions.com/the-assumption-of-homogeneity-of-variance/


#mod = ols('PetalLength ~ Name', data=df).fit() #https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
                
#aov_table = sm.stats.anova_lm(mod, typ=2)
#print (aov_table)

#tukey = pairwise_tukeyhsd(endog=df.PetalLength, groups=df.Name, alpha=0.05) #http://www.statsmodels.org/dev/generated/statsmodels.sandbox.stats.multicomp.TukeyHSDResults.plot_simultaneous.html         
#print(tukey.summary())                                                      # http://hamelg.blogspot.ie/2015/11/python-for-data-analysis-part-16_23.html
#tukey.plot_simultaneous()
#plt.ylabel('Average Petal Length in cm')


#plt.show()

## Petal Width

#sns.swarmplot(x="Name", y="PetalWidth", data=df, palette="bright") # a Swarmplot - https://seaborn.pydata.org/tutorial/categorical.html
#plt.title('Fig. 28. Petal Width Swarmplot')
#plt.ylabel('Petal Width in cm')
#plt.show()

#print(setosa["PetalWidth"].describe()) 
#print(virginica["PetalWidth"].describe()) 
#print(versicolor["PetalWidth"].describe()) 



#sns.barplot(x="Name", y="PetalWidth", data=df, ci=None)
#plt.ylabel('Average Petal Width in cm')
#plt.title('Fig. 29. Petal Width Barplot')



#sns.boxplot(x="Name", y="PetalLength", data=df)
#plt.title('Fig. 30. Petal Length Boxplot')


#plt.show()

#print(stats.kruskal(setosa.PetalWidth, virginica.PetalWidth, versicolor.PetalWidth))

#Sepal Length



#sns.swarmplot(x="Name", y="SepalLength", data=df, palette="bright") # a Swarmplot - https://seaborn.pydata.org/tutorial/categorical.html
#plt.title('Fig. 31. Sepal Length Swarmplot')
#plt.ylabel('Sepal Length in cm')
#plt.show()






#sns.barplot(x="Name", y="SepalLength", data=df, ci=None)
#plt.ylabel('Average Sepal Length in cm')
#plt.title('Fig. 32. Sepal Length Barplot')
#plt.show()



#sns.boxplot(x="Name", y="SepalLength", data=df)
#plt.title('Fig. 33. Sepal Length Boxplot')


#plt.show()



#mod = ols('SepalLength ~ Name', data=df).fit() #https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
                
#aov_table = sm.stats.anova_lm(mod, typ=2)
#print (aov_table)

#tukey = pairwise_tukeyhsd(endog=df.SepalLength, groups=df.Name, alpha=0.05) #http://www.statsmodels.org/dev/generated/statsmodels.sandbox.stats.multicomp.TukeyHSDResults.plot_simultaneous.html         
#print(tukey.summary())                                                      # http://hamelg.blogspot.ie/2015/11/python-for-data-analysis-part-16_23.html
#tukey.plot_simultaneous()
#plt.ylabel('Average Petal Length in cm')


#plt.show()

# Sepal Width

#sns.swarmplot(x="Name", y="SepalWidth", data=df, palette="bright") # a Swarmplot - https://seaborn.pydata.org/tutorial/categorical.html
#plt.title('Fig. 34. Sepal Width Swarmplot')
#plt.ylabel('Sepal Width in cm')
#plt.show()




#sns.barplot(x="Name", y="SepalWidth", data=df, ci=None)
#plt.ylabel('Average Sepal Width in cm')
#plt.title('Fig. 35. Sepal Width Barplot')
#plt.show()



#sns.boxplot(x="Name", y="SepalWidth", data=df)
#plt.title('Fig. 36. Sepal Width Boxplot')


#plt.show()



#mod = ols('SepalWidth ~ Name', data=df).fit() #https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
                
#aov_table = sm.stats.anova_lm(mod, typ=2)
#print (aov_table)

#tukey = pairwise_tukeyhsd(endog=df.SepalWidth, groups=df.Name, alpha=0.05) #http://www.statsmodels.org/dev/generated/statsmodels.sandbox.stats.multicomp.TukeyHSDResults.plot_simultaneous.html         
#print(tukey.summary())                                                      # http://hamelg.blogspot.ie/2015/11/python-for-data-analysis-part-16_23.html
#tukey.plot_simultaneous()
#plt.ylabel('Average Petal Length in cm')

#plt.show()

# Correlation



#corr = df.corr()
#print(corr)


#corr = df.corr()
#sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap="plasma")
#plt.title("Pearson Correlation Matrix")
#plt.show() # https://seaborn.pydata.org/generated/seaborn.heatmap.html -

#corr = df.corr(method="spearman")
#sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True, cmap="plasma")
#plt.title("Spearman Correlation Matrix")
#plt.show() # https://seaborn.pydata.org/generated/seaborn.heatmap.html -

#sns.jointplot(x="PetalLength", y="SepalLength", data=df, kind="reg", stat_func=spearmanr) # Youcan change the statistics and shos the correlation using Pearson as it is normally distrubuted ~ https://seaborn.pydata.org/generated/seaborn.jointplot.html#seaborn.jointplot

#plt.show()

# Results

ax = setosa.plot.scatter(x="PetalLength", y="PetalWidth", color="blue", label="Setosa")
virginica.plot.scatter(x="PetalLength", y="PetalWidth", color="red", label="Virginica", ax=ax)
versicolor.plot.scatter(x="PetalLength", y="PetalWidth", color="green", label="Versicolor", ax=ax)
plt.title("Petal Length and Width Scatterplot")
plt.show()
