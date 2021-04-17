import matplotlib.pyplot as plt 

#This graph will show the amount of men canadian medals from Canada though the years

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
medals = [9, 12, 20, 13, 18, 17, 18, 19, 5, 18, 0, 1, 2, 4, 2, 30, 30, 16, 38, 21, 47, 46]

plt.plot(years,medals, color =(15/255, 82/255, 87/255),linewidth=3.0)
plt.ylabel("Medals won by canadian men")
plt.xlabel("Years with Winter Olympic games")
plt.title("Canadian men winners through the years")

plt.show () 

