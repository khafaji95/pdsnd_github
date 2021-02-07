import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# Global Variables used to check and validate the user's input.
city_input = ["chicago", "new york city", "washington"]
month_input = ["all", "january", "february", "march", "april", "may", "june"]
day_input = ["all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]


def check_filter(question, category):
    """
    This Function takes on the question asked to the user with a category
    to check and validate the input it recieves.

    ARGS:
        1) (STR) Question that the proram is currently asking the user.
        2) (STR) The category of the question.

    RETURNS:
        1) (STR) city - name of the city the user is interested in viewing.
        2) (STR) month - month chosen by the user to filter and view data.
        3) (STR) day - the day the user want to view it's data.
    """

    # A variable that acts as a switch for the While Loop.
    x = True
    while x:
        user_input = input(question).lower()

        if (user_input in city_input) and (category == "Enter City"):
            x = False
        elif (user_input in month_input) and (category == "Enter Month"):
            x = False
        elif (user_input in day_input) and (category == "Enter Day"):
            x = False
        else:
            print("Ops! The input you entered is not correct please try again and choose from the list shown below.\n\n")

    return user_input


def get_filters():
    """
    Declares filter variables and passes their relevant question and category to check_filter().

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    city = check_filter("\n\nWelcome to this program! Kindly choose a city you wish to analyze from the list below:\n\n1) Washington \n2) Chicago\n3) New York City\n\n", "Enter City")
    month = check_filter("\n\nGeat!! Now do choose a month you wish to filter the data by from the list below:\n\n0) All \n1) January \n2) February \n3) March \n4) April \n5) May \n6) June\n\n", "Enter Month")
    day = check_filter(f"\n\nGreat!! so far you want to see the data of {city.title()} on {month.title()}. Now pick a day to filter the data even more from the list below:\n\n0) All \n1) Sunday \n2) Monday \n3) Tuesday \n4) Wednesday \n5) Thursday \n6) Friday \n7) Saturday\n\n", "Enter Day")

    print('-' * 40)
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
    # Create a dataframe

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
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
    print('\nThe Most Common Month: \n')
    popular_month = df['month'].mode()[0]
    print(month_input[popular_month].title())
    # TO DO: display the most common day of week
    print('\nThe Most Common day of the week: \n')
    popular_day = df['day_of_week'].mode()[0]
    print(popular_day)

    # TO DO: display the most common start hour
    print('\nThe Most Common start hour: \n')
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe Most Common Used Start Station: \n')
    start_station = df['Start Station'].mode()[0]
    print(start_station)
    # TO DO: display most commonly used end station
    print('\nThe Most Common End Station: \n')
    end_station = df['End Station'].mode()[0]
    print(end_station)
    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe Most Frequent Combination of Start and End Stations: \n')
    df['Frequent Combination'] = "Start Station: "+ df['Start Station'] + "||" + " End Station: " + df['End Station']
    combination_station = df['Frequent Combination'].mode()[0]
    print(combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Travel Time: \n')
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    # TO DO: display mean travel time
    print('\nAvarage Travel Time: \n')
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    ARGS:
    1) DF - DataFrame.
    2) city - city chosen by the user.
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe Count of User Types: \n')
    user_types = df['User Type'].value_counts()
    print(user_types)

    if (city == "new york city") or (city == "chicago"):

        # TO DO: Display counts of gender
        print('\nGender Head Count: \n')
        gender_count = df['Gender'].value_counts()
        print(gender_count)

        # TO DO: Display most common year of birth
        print('\nThe Most Common Birth Year: \n')
        common_birth_year = df['Birth Year'].mode()[0]
        print(common_birth_year)

        # TO DO: Display most recent year of birth
        print('\n The Most Recent Year of Birth: \n')
        max_birth_year = df['Birth Year'].max()
        print(max_birth_year)

        # TO DO: Display earliest year of birth
        print('\nThe Earliest Year of Birth: \n')
        min_birth_year = df['Birth Year'].min()
        print(min_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def raw_data(df):
    x = True
    index = 0
    while x:
        print("\nDisplaying five rows of your data: \n")
        pd.set_option("display.max.columns", None)
        print(df.iloc[index:index+5])
        index+=5
        answer = input("\nDo you wish to view more rows? Yes or No\n").lower()
        if answer == "no":
            x = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_raw_data = input("\nDo you wish to view the raw data? Yes or No\n").lower()
        if view_raw_data == "yes":
            raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
