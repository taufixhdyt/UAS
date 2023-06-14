import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()

df = pd.read_csv('stock.csv')
df

plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
sns.histplot(df['Purchase Price ($)'], kde=True, bins=10, edgecolor='k', color="r")
plt.xlabel('Purchase Price')
plt.ylabel('Frequency')
plt.title('Histogram Purchase Price')

plt.subplot(1, 3, 2)
sns.histplot(df['Current Price ($)'], kde=True, bins=10, edgecolor='b', color="y")
plt.xlabel('Current Price')
plt.ylabel('Frequency')
plt.title('Histogram Current Price')

plt.subplot(1, 3, 3)
sns.histplot(df['Gain/Loss ($)'], kde=True, bins=10, edgecolor='c', color="g")
plt.xlabel('Gain/Loss')
plt.ylabel('Frequency')
plt.title('Histogram Gain/Loss')

plt.tight_layout()
plt.show()

#Mengurutkan data dari yang terbesar
data = df.sort_values(by="Dividend/share ($)", ascending=False)

#Mengambil data
t5 = data.head(5)

# Memilih data
plt.figure(figsize=(9, 4))
sns.barplot(x="Stock Name", y="Dividend/share ($)", data=t5)
plt.title("Top 5 Stocks with Highest Dividend / Shares")

#Menampilkan data
plt.show()

#Mengurutkan data dari yang terbesar
data = df.sort_values(by="Market Value ($)", ascending=False)

#Mengambil data
t5 = data.head(5)

# Memilih data
plt.figure(figsize=(9, 4))
sns.barplot(x="Stock Name", y="Market Value ($)", data=t5)
plt.title("Top 5 Stocks with Highest Market Value ($)")

#Menampilkan data
plt.show()

#Mengurutkan data dari yang terbesar
data = df.sort_values(by="Annual Yield (%)", ascending=False)

#Mengambil data
t7 = data.head(7)

# Memilih data
plt.figure(figsize=(13, 4))
sns.barplot(x="Stock Name", y="Annual Yield (%)", data=t7)
plt.title("Top 7 Stocks with Highest Annual Yield (%)")

#Menampilkan data
plt.show()
