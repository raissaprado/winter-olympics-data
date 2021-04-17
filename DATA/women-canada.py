import matplotlib.pyplot as plt 

#This graph will show the amount of women canadian medals from Canada though the years

years = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
medals = [0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 1, 2, 0, 0, 4, 7, 10, 33, 37, 47, 44, 44]

plt.plot(years,medals, color =(162/255, 59/255, 114/255), linewidth=3.0)
plt.ylabel("Medals won by canadian women")
plt.xlabel("Years with Winter Olympic games")
plt.title("Canadian women winners through the years")

plt.show () 

