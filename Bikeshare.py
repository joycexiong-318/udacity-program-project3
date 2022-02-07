#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


# In[2]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    while True:
       city = input('Which city do you want to explore chicago, new york city or washington? \n> ').lower()
       if city in CITIES:
           break
        
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('provide the name of the month'                     'or just type \'all\' to apply no month filter. \n>').lower()
        if month in MONTHS:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('provide the name of the day of week'                    'or type \'all\' again to apply no day filter. \n> ').lower()
        if day in DAYS:
           break

    print('-'*40)
    return city, month, day


# In[3]:


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# In[4]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    most_common_month = df['Start Time'].dt.month.mode()[0]
    print('The most common month is :', most_common_month)

    # display the most common day of week
          
    most_common_day = df['Start Time'].dt.weekday_name.mode()[0]
    print('The most common day of week is:', most_common_day)
          
    # display the most common start hour
          
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[5]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', most_commonly_used_start_station)

    # display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', most_commonly_used_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_combination_trip = df[['Start Station','End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip is:{}, {}'            .format( most_frequent_combination_trip[0],  most_frequent_combination_trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[6]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The toal travel time is:', total_travel_time)
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean of the travel time is:', mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[7]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print('the counts of user types are:', counts_user_types)

    # Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print('the counts of gender are:',counts_gender)

    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    
    earliest_birth_year = df['Birth Year'].min()
    print('The earliest year of birth is:',earliest_birth_year)
    
    most_recent_birth_year = df['Birth Year'].max()
    print('The most recent year of birth is:', most_recent_birth_year)
    
    most_common_birth_year = df['Birth Year'].mode()[0]
    print('The most common year of birth is:', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[9]:


def display_data(df):
    """Displays raw bikeshare data."""
    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    start_loc = 0
    keep_asking = True
    while (keep_asking):
          print(df.iloc[start_loc:start_loc + 5])
          start_loc += 5
          view_display = input("Do you wish to continue?: ").lower()
          if view_display == "no": 
              keep_asking = False


# In[10]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

