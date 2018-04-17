
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
