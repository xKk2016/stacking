import numpy as np
import pandas as pd

txt = np.loadtxt('chenfei.txt',delimiter=",")
txtDF = pd.DataFrame(txt)
txtDF.to_csv('chenfei.csv', index=False)
txt = np.loadtxt('datapipeline.txt',delimiter=",")
txtDF = pd.DataFrame(txt)
txtDF.to_csv('xuguokai.csv', index=False)

