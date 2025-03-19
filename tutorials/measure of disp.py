import numpy as np
table= [(0,10),(10,20),(20,30),(30,40),(40,50),(50,60),(60,70),(70,80)]
freq = [5,10,20,40,30,20,10,5]
midpoint=[(low+high)/2 for low,high in table]
mean =np.sum(freq)/len(freq)
variance= np.average(midpoint-mean)**2
std_dev = np.sqrt(variance)
cv = (std_dev/mean)*100
print("standard deviation=",std_dev)
print("cofficient of variance",cv)
