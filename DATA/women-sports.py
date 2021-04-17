import matplotlib.pyplot as plt 

#This graph will show the amount of medals per sport from women

values = [144, 36, 75, 305, 43, 506, 580]
labels = ["Biathlon", "Bobsleigh", "Curling", "Ice Hockey", "Luge", "Skating", "Skiing"]
colors = ["purple", "cyan", "orange", "green", "pink", "gray", "olive"]


plt.pie (values, labels = labels)

plt.show () 

