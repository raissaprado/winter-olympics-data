import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#This graph will show the TOP 5 Countries with more Women medalists


objects = ('USA', 'CAN', 'GER', 'FIN', 'RUS')
y_pos = np.arange(len(objects))
performance = [252, 239, 230, 106, 106]


plt.bar(y_pos, performance, align='center', alpha=0.5, color=['red', 'firebrick', 'purple', 'green', 'olive'])
plt.xticks(y_pos, objects)
plt.ylabel('Medals')
plt.title('Women - TOP 5 Countries')

plt.show()
