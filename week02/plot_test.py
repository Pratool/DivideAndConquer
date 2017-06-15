import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

style = {'text.usetex': True, 'font.family': 'serif', 'font.serif': ['cmr17'] }
sns.set(context="poster", style="whitegrid", palette="bright", font_scale=1.5,\
        rc=style)

#d = pd.io.parsers.read_table("switch-cap-test.txt",\
test_file = "test3.txt"
d = pd.io.parsers.read_table(test_file,\
        sep=' ')

n = d['input']
runtime = d['runtime']
logn = np.log(np.asarray(n))/np.log(1.45)

plt.semilogx(n, runtime, label='runtime')
plt.semilogx(n, logn, label='$\log_{1.45} n$')
plt.xlabel('Input Size')
plt.ylabel('Approximate Number of O(1) Operations')
plt.legend(loc=2)
plt.show()
