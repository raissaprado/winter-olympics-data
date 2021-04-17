import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#This graph will show the TOP 5 Countries with more Men medalists


objects = ('USA', 'CAN', 'GER', 'NOR', 'FIN')
y_pos = np.arange(len(objects))
performance = [422, 386, 386, 359, 328]

plt.bar(y_pos, performance, align='center', alpha=0.5, color=['red', 'firebrick', 'purple', 'green', 'olive'])
plt.xticks(y_pos, objects)
plt.ylabel('Medals')
plt.title('Men - TOP 5 Countries')

plt.show()
