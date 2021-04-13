import os
'''Configuration file for hardcoding python variables.
Used to store things like file paths, model hyperparameters etc.'''

PROJECT_NAME = 'LMC-enrollment-forecast'

# Get path to this config file so that we can define 
# other paths relative to it
PROJECT_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# Data files
DATA_PATH = f'{PROJECT_ROOT_PATH}/data/'

ENROLLMENT_BY_DEPARTMENT_DATAFILE = 'enrollment_by_department.csv'
ENROLLMENT_BY_SEMESTER_DATAFILE = 'enrollment_by_semester.csv'

FORMATTED_DATAFILE = 'enrollment_by_semester_formatted.csv'

# Modeling meta-parameters
TARGET_VARIABLE = 'Next Semester Census Enrollment'
TRAIN_TEST_SPLIT = 0.7
N_MODELS = 10

# Neural network hyperparameters
TRAINING_EPOCHS = 200
UNITS = 64
LEARNING_RATE = 0.02