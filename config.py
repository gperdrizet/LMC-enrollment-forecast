import os
'''Configuration file for hardcoding python variables.
Used to store things like file paths, model hyperparameters etc.'''

PROJECT_NAME = 'LMC-enrollment-forecast'

# Get path to this config file so that we can define 
# other paths relative to it
PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Data related files & paths
DATA_PATH = f'{PROJECT_ROOT_PATH}/data/'
ENROLLMENT_BY_DEPARTMENT_DATAFILE = 'enrollment_by_department.csv'
ENROLLMENT_BY_SEMESTER_DATAFILE = 'enrollment_by_semester.csv'
CLEANED_DATAFILE = 'enrollment_by_semester_cleaned.csv'
FORMATTED_DATAFILE = 'enrollment_by_semester_formatted.csv'
CENSUS_ENROLLMENT_BY_DATE = 'census_enrollment_by_date.pkl'

# Modeling meta-parameters
RESULTS_PATH = f'{PROJECT_ROOT_PATH}/results/'
TARGET_VARIABLE = 'Next Semester Census Enrollment'
TRAIN_TEST_SPLIT = 0.8
N_MODELS = 100

# Simple linear regression
SIMPLE_LINEAR_MODEL_RESULTS_FILE = 'simple_linear_regression_results.pkl'

# Multiple linear regression
MULTIPLE_LINEAR_MODEL_RESULTS_FILE = 'multiple_linear_regression_results.pkl'

# Neural network
NEURAL_NETWORK_RESULTS_FILE = 'neural_network_results_file.pkl'
NEURAL_NETWORK_MODEL_ENSEMBLE_PATH = f'{RESULTS_PATH}/DNN_models/'
TRAINING_EPOCHS = 100
UNITS = 128
LEARNING_RATE = 0.02