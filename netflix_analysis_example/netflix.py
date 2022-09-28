import pandas as pd
import matplotlib_inline
import matplotlib
import matplotlib.pyplot as plt

fname = pd.read_csv("ViewingActivity.csv")

fname.shape
fname = fname.drop(['Profile Name','Attributes','Supplemental Video Type','Device Type','Bookmark','Latest Bookmark', 'Country'], axis = 1)

# indexing 'Start Time', and converting it into Eastern Time (my local)
fname['Start Time'] = pd.to_datetime(fname['Start Time'], utc=True)
fname = fname.set_index('Start Time')
fname.index = fname.index.tz_convert('US/Eastern')
fname = fname.reset_index()

# indexing "duration"
fname['Duration'] = pd.to_timedelta(fname['Duration'])

# title selection and watched more than 1 minute to remove mini trailers or other non watched episodes
titleinput = input("What title are you looking for analysis?  ")
uiTitle = fname[fname['Title'].str.contains(titleinput,regex="False")]
uiTitle = uiTitle[(uiTitle['Duration'] > '0 days 00:01:00')]
timewatching = uiTitle['Duration'].sum()

#graphout weekday usage
uiTitle['weekday'] = uiTitle['Start Time'].dt.weekday
uiTitle['weekday'] = pd.Categorical(uiTitle['weekday'], categories=[0,1,2,3,4,5,6], ordered=True)
title_by_day = uiTitle['weekday'].value_counts()
title_by_day = title_by_day.sort_index()
# title_by_day.plot(kind='bar', figsize=(20,10), title='Episodes Watched by Day')
plot1 = plt.figure(1)

plt.title("Episodes Watched by Day")
plt.plot(title_by_day)

#graph hour usage
uiTitle['hour'] = uiTitle['Start Time'].dt.hour
uiTitle['hour'] = pd.Categorical(uiTitle['hour'], categories=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], ordered=True)
title_by_hour = uiTitle['hour'].value_counts()
title_by_hour = title_by_hour.sort_index()
# title_by_hour.plot(kind='bar', figsize=(20,10), title='Episodes Watched by Hour')
plot2 = plt.figure(2)

plt.title('Episodes Watched by Hour')
plt.plot(title_by_hour)
plt.show()

print("Time total time watching", titleinput, "is", timewatching )

# print(uiTitle.shape)
# print(fname.dtypes)


# print(uiTitle.head(1))

input("Press enter to close.")
