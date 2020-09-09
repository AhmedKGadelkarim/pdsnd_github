#!/usr/bin/env python
# coding: utf-8

# In[8]:

# This program is designed to analyse Us bike share data in three cities
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input(" please enter the city name: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(" Invalid city name, please enter a valid city name!").lower()

    # TO DO: get user input for month (all, january, february, ... , june)

    month = input(" Please enter the month name: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
        month = input(" Invalid month, please enter a valid month name!").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Please enter the day of the week:  ").lower()
    while day not in ['friday', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday']:
        day = input(" Invalid day, please enter a valid day name!").lower()
        
    print('-'*40)
    return city, month, day


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

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]

    print('Most Popular Month:', popular_month)
    
    # TO DO: display the most common day of week

    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', popular_day_of_week)
    
    # TO DO: display the most common start hour

    popular_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', popular_common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', popular_start_station)
    
    # TO DO: display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]

    print('Most End Station:', popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip

    df['combination'] = df['Start Station']+ " " + df['End Station']
    most_comb_stations = df['combination'].mode()[0]
    print("most frequent combination of start station and end station trip: ", most_comb_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)
    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print("counts of user types are: ", user_types)
        
    # TO DO: Display counts of gender
    if city != 'washington':    
        user_gender = df['Gender'].value_counts()
        print("counts of user types are: ", user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        print(" The earliest birth of year is: ", earliest_yob)
    
        most_recent_yob = df['Birth Year'].max()
        print(" The most recent birth of year is: ", most_recent_yob)
    
        most_common_yob = df['Birth Year'].mode().values[0]
        print(" The most common birth of year is: ", most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        # defining a raw_dat_display function so user can choose to look over the raw data 5 rows by 5 rows
        def raw_data_display():
            i = 0
            j = 5        
            display_data = input('do you want to see a sample 5 rows of raw data? yes / no \n').lower()
            while display_data not in ('yes', 'no'):
                display_data = input('invalid answer, please write (yes) / (no) only \n').lower()
            if display_data == 'yes':
                print(df.iloc[0:5].copy())
            elif display_data == 'no':
                return
            
            while True:
                display_more=input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
                while display_more not in ('yes', 'no'):
                    display_more = input('invalid answer, please write (yes) / (no) only \n').lower()
                if display_more=='yes':
                    print(df.iloc[i+5:j+5].copy())
                    i+= 5
                    j+= 5
                else:
                    break
                    
        raw_data_display()

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:




