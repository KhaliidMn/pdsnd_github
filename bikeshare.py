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
    while True:
        city = input('Enter a city from: chicago, new york city, washington: ')
        city = city.lower()
        cities = ['chicago','new york city','washington']
        if city in cities:
            break;
        else:
            print('Enter a valid city: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month f all, january, february, ... , june: ')
        month=month.title().strip()
        months = ['All','January','February','March','April','May','June','July','Augest','September','October','November','December']
        if month in months:
            break;
        else:
            print('Enter a valid month: ')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day all, monday, tuesday, ... sunday: ')
        day=day.strip().title()
        days = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        if day in days:
            break;
        else:
            print('Enter a valid day: ')

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
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['Hour']=df['Start Time'].dt.hour
    df['Day']=df['Start Time'].dt.day_name()
    df['Month']=df['Start Time'].dt.month_name()
    
    if month != 'All':
        df=df[df['Month']==month]
    if day != 'All':
        df=df[df['Day']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common starting month is: '+df['Month'].mode()[0]) 


    # TO DO: display the most common day of week
    print('The most common starting day is: '+df['Day'].mode()[0]) 


    # TO DO: display the most common start hour
    print('The most common starting hour is: '+str(df['Hour'].mode()[0]))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common starting start station is:'+df['Start Station'].mode()[0]) 

    # TO DO: display most commonly used end station
    print('The most common end station is:'+df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End']='starts from '+df['Start Station']+' to '+df['End Station']
    combination=df['Start End'].mode()[0]
    print('The most common combination starting station '+combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=str(df['Trip Duration'].sum())
    print('The total travel time is:'+total_travel_time+'minutes')
    
    # TO DO: display mean travel time
    print('The mean of travel time is:'+str(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    try:
        user_counter=str(df['User Type'].value_counts())
        print('the number of user typs is: '+user_counter)
   
    # TO DO: Display counts of gender
        gender_counter=str(df['Gender'].value_counts())
        print('the number of gender is: '+gender_counter)

    # TO DO: Display earliest, most recent, and most common year of birth
        common=str(df['Birth Year'].mode()[0])
        earliest=str(df['Birth Year'].min())
        latest=str(df['Birth Year'].max())
        print('earliest birth in: '+earliest+' the most recent is in: '+latest+' and the most common is in: '+common)
    
    except:
        print('the city you chose does not have these values you are looking for')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
