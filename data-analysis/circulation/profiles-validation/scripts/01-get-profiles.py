import numpy as np
import pandas as pd
import pprint as pp
from sklearn.datasets import load_iris

iris = load_iris()

iris_DF = pd.DataFrame(
    data = np.c_[iris['data'], iris['target']],
    columns= iris['feature_names'] + ['target']
    )

