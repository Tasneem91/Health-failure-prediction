# Import the required libraries
import numpy as np
from scipy import stats

file_name = 'heart_failure_clinical_records_dataset.csv'

# i). Exploratory Data Analysis
# 1- Read the data
def read_heart_failure_data(file_name):
    try:
        raw_data = open(file_name, 'rb')
        heart_failure_data = np.loadtxt(raw_data, skiprows=1, delimiter=',')
        print(heart_failure_data.dtype)
        np.set_printoptions(suppress=True)
        print(heart_failure_data)
        return heart_failure_data
    except Exception as e:
        print(f"Error Message {e}")

# This function to find the age location measures
def discover_age_location_measures(data):
    print("Discover Age Location and Spread Measures in Heart Failure Clinical Records Dataset\n")
    minimum_age = int(data[:, 0].min())
    print("Minimum Age = ", minimum_age)
    maximum_age = int(data[:, 0].max())
    print("Maximum Age = ", maximum_age)
    ages_average = int(data[:, 0].mean())
    print("Ages Average = ", ages_average)
    ages_standard_deviation = data[:, 0].std()
    print("Age Standard Deviation = ", ages_standard_deviation)
    age_variance = data[:, 0].var()
    print("Age Variance = ", age_variance)
    print("--------------------------------------\n")

def test_function(array1):
    count = 0
    if array1[0] == 1:
        if array1[1] == 1:
            count += 1


    return count

def discover_patients_info(data):
    smokers = np.count_nonzero(data[:, 10] == 1)
    print(f"The number of smokers is  {smokers} out of {data.shape[0]}", )
    print("Average of the smokers = ", round(data[:, 10].mean(), 2), "")
    print(f"The patients are varies between {np.count_nonzero(data[:, 9] == 1)} men, and {np.count_nonzero(data[:, 9] == 0)} women")
    sex_smoking = data[:, 9:11]
    #print(sex_smoking.shape)
    count = np.apply_along_axis(test_function, axis=1, arr=sex_smoking)
    men_smokers = np.count_nonzero(count == 1)
    print(f"The number of smokers men is {men_smokers}")


def check_categorical_and_numerical_features(file_name):
    # Load the dataset
    data = np.loadtxt(file_name, delimiter=',', skiprows=1)

    # Get the column names
    column_names = np.genfromtxt(file_name, delimiter=',', max_rows=1, dtype=str)

    # Loop over the columns
    for i in range(data.shape[1]):
        column = data[:, i]
        if np.all(np.logical_or(column == 0, column == 1)):
            print(f'Column {i} ({column_names[i]}) is a categorical column with only 0 or 1 values.')


# 3- Explore dataset statistical information: mean, median, std, var, skew, kurtosis
def explore_continous_var_statistical_info(file_name):
    # Load the dataset
    data = np.loadtxt(file_name, delimiter=',', skiprows=1)

    # Get the column names
    column_names = np.genfromtxt(file_name, delimiter=',', max_rows=1, dtype=str)

    # Loop over the columns
    for i in range(data.shape[1]):
        column = data[:, i]
        if np.all(np.logical_or(column == 0, column == 1)):
            continue

        else:
            print(f"\n mean, median, std, var, skew, kurtosis for Column {i} ({column_names[i]}) are:\n")
            print("mean :", round(np.mean(column), 2))
            print("median :", round(np.median(column), 2))
            print("std :", round(np.std(column), 2))
            print("var :", round(np.var(column), 2))
            print("min :", np.min(column))
            print("max :", np.max(column))
            print("skewness :", round(stats.skew(column), 2))
            print("kurtosis :", round(stats.kurtosis(column), 2))



print("EDA module has been loaded")







