import os
import numpy as np
import pandas as pd
import pprint as pp

project_dir = os.getcwd() + '/data-analysis/circulation/profiles-validation'

iris_DF = pd.read_csv(project_dir + "/data/source/iris.csv")

# DO ANALYSIS STUFF HERE


iris_DF.to_csv(project_dir + "/data/validated/iris.csv", index=False)


