import os
import numpy as np
import pandas as pd
import pprint as pp
from sklearn.datasets import load_iris

project_dir = os.getcwd() + '/data-analysis/circulation/profiles-validation'

iris = load_iris()

iris_DF = pd.DataFrame(iris.data, columns=iris.feature_names)

iris_DF.to_csv(project_dir + "/data/source/iris.csv", index=False)