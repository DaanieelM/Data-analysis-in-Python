import numpy as pd
import pandas as pd
import matplotlib.pyplot as plt # visualizing data
%matplotlib inline
import seaborn as sns

# Read data
df = pd.read_csv(r"C:\Users\Daniel\Desktop\Python\Project1\Spotify Most Streamed Songs.csv")

df.head()

df.shape

# Remove duplicates
df = df.drop_duplicates()

# Drop column 'cover_url'
df = df.drop(columns = 'cover_url')

df.head()

# Rename column artist(s)_name to artist
df = df.rename(columns={'artist(s)_name':'artist'})

df.describe()

# Check types of columns
df.dtypes

df['streams'].dtypes

# Remove NaN values
df.dropna(inplace=True)

print(df['streams'].max())

# Change text to NaN
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# Remove NaN values
df = df.dropna(subset=['streams'])

df.shape

# Change data type
df['streams'] = df['streams'].astype('streams')

df['streams'].dtypes

df.groupby('streams').sum()


# Total number of streams of top 10 artists
artists_number = df.groupby(['artist'], as_index=False)['streams'].sum().sort_values(by='streams', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=artists_number, x='artist', y='streams')

# Total number of streams of top 10 track name
streams_number = df.groupby(['track_name'], as_index=False)['streams'].sum().sort_values(by='streams', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=streams_number, x='track_name', y='streams')

# The top 5 tracks with the heighest streams in 2022
df2 = df[df['released_year'] == 2022]
streams2022 = df2.groupby(['track_name'], as_index=False)['streams'].sum().sort_values(by='streams', ascending=False).head(5)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=streams2022, x='track_name', y='streams')

# The top 10 artists with the heighest streams in 2022
artists2022 = df2.groupby(['artist'], as_index=False)['streams'].sum().sort_values(by='streams', ascending=False).head(5)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=artists2022, x='artist', y='streams')

# The best 10 tracks created by Bad Bunny
BadBunny = df[df['artist'] == 'Bad Bunny']
BadBunny.sort_values(by=['streams'], ascending = False).head(10)
tracks_Bunny = BadBunny.groupby(['track_name'], as_index=False ['streams'].sum().sort_values(by='streams', ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=tracks_Bunny, x='track_name', y='streams')
