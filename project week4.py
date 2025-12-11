import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data={
    'Hours':[10,21,23,15,20,30,55],
    'Exam Score':[98,97,85,88,90,95,99]
}
df=pd.DataFrame(data)
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(df)
df['Cluster']=kmeans.labels_
plt.figure(figsize=(8,6))
plt.scatter(df['Hours'],df['Exam Score'],c=df['Cluster'],cmap='cool',s=100,label="sales")
centroids=kmeans.cluster_centers_
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=200,marker='x',label='Centroids')
plt.title('K-Means Clustering: Hours vs Exam Score')
plt.xlabel('Hours')
plt.ylabel('Exam Score')
plt.show()