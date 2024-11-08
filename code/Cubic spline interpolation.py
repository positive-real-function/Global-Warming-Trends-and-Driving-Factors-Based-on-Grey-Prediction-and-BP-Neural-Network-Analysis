# code:utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# import data
file = pd.read_csv('data.txt', sep='\s+',
                   header=None,
                   names=['x', 'value'])

data = pd.DataFrame(file)
# array slice
x = data['x']  # get the first column of data
y = data['value']  # get the second column of data
# Cubic-Spline
tck = interpolate.splrep(x, y)
xx = np.linspace(min(x), max(x), 200)
yy = interpolate.splev(xx, tck, der=0)
print(yy)
# paint
plt.plot(x, y, 'o', xx, yy)
plt.legend(['true', 'Cubic-Spline'])
plt.xlabel('Year')
plt.ylabel('Temperature（℃）')
plt.title('Temperature fitting curve(January in Kabul)')
# save image
plt.savefig('Temperature fitting curve(January in Kabul).png', dpi=600)
plt.show()


