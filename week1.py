import pandas as md
import matplotlib.pyplot as plt
city=md.read_csv("Bangalore_1990_2022_BangaloreCity.csv")
print(city.isnull().sum())
city['tavg']=city['tavg'].fillna(city['tavg'].mean())
city['tmax']=city['tmax'].fillna(city['tmax'].mean())
city['tmin']=city['tmin'].fillna(city['tmin'].mean())
city['prcp']=city['prcp'].fillna(city['prcp'].mean())
print(city.isnull().sum())
city['time']=md.to_datetime(city['time'], format="%d-%m-%Y")
city['year']=city['time'].dt.year
city['month']=city['time'].dt.month
city['day']=city['time'].dt.day
yearly=city.groupby('year')['tavg'].mean(). reset_index()
print(yearly)
plt.figure(figsize=(10, 5))
plt.plot(yearly['year'], yearly['tavg'], marker='o')
plt.plot(yearly['year'], yearly['tavg'], marker='o', color='orange')
plt.title('Yearly Average Temperature in Bangalore (1990-2022)')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.show()