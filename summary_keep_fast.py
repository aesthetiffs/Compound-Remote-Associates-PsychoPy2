# Creates both individual and combined summary files from the raw PsychoPy data
# This script does NOT remove fast recognitions
# By Tiffani Ng/Beeman Lab

# Please note that this version of the CRA summary script is written for Python 2.7

import os
import glob
import pandas as pd
import datetime
import random
from collections import OrderedDict

# Checks whether there is a data directory
# If no data directory exists, throw an error
if os.path.isdir('./data') == False:
    raise Exception('Error: data directory was not found. Please put all of your data files into a folder with the name data ')
else:
    print 'data folder found'

data_dir = "data"
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir_path = os.path.join(current_dir, data_dir)

# Checks whether "clean_data" exists
# If not create a folder where the "clean" individual files will be held
if os.path.isdir('./data/clean_data') == True:
    print 'clean_data directory exists, skipped directory creation'
else:
    os.makedirs('./data/clean_data')
    print 'created clean_data directory'

# Checks whether "individual_summary" exists
# If not create a folder where the individual summary files will be held
if os.path.isdir('./data/individual_summary') == True:
    print 'individual_summary directory exists, skipped directory creation'
else:
    os.makedirs('./data/individual_summary')
    print 'created individual_summary directory'

# Checks whether "combined_summary" exists
# If not create a folder where the combined summary file will be held
if os.path.isdir('./data/combined_summary') == True:
    print 'combined_summary directory exists, skipped directory creation'
else:
    os.makedirs('./data/combined_summary')
    print 'created combined_summary directory'

# Initialize a dataframe for the combined summary files
combined_summary = pd.DataFrame()

# Get today's date to append to the filenames
date = datetime.date.today()

# Reads in the individual data files, then does some magic on them
for filename in glob.glob('data/*.csv'):
    # Only read in the columns needed for the clean data file
    data = pd.read_csv(filename, usecols=['cra','solution','block','cra_key','cra_rt','craCorrect','InsAnaWas','participant','expName','date', 'condition'])

    # Create some filters to be used for calculations
    real = data['block']!='practice' #real problems (excludes practice problems)
    attempts = data['cra_key'] == 'space' #attempted problems (excludes errors of omission)
    correct = data['craCorrect']==1 #correctly solved attempts
    insight = data['InsAnaWas']=='ins' #solved by insight (incorrect and correct)
    analysis = data['InsAnaWas']=='ana' #solved by analysis (incorrect and correct)

    # Also create some variables that will store some information to be spit out later
    pid = data['participant'][0] #participant id number
    condition = data['condition'][0] #condition
    total = data['cra'].count() #counts total number of CRAs

    # create a unique identifier for unique filename purposes
    unique_id = random.randrange(0, 9999)

    # to avoid accidental duplicate IDs overwriting the first CSV output with that ID,
    # add the unique identifier
    clean_filename = 'data/clean_data/%s_%s_cra_%s_%s.csv' %(pid, condition, date, unique_id)

    # if, somehow the filename (even with the unique identifier) already exists, don't write it out
    # but let the experimenter know it happened so they can doublecheck that file
    if os.path.isfile(clean_filename) == False:
        # Save the individual clean data to a new CSV, in the clean_data folder
        data.to_csv(clean_filename, index=False)
        print 'created clean data file for %s' %(pid)

    else:
        print 'duplicate filename exists'
        print '%s' %(clean_filename)

    # calculate number of attempts (excluding practice), correct/incorrect solutions, correct/incorrect insights/ correct/incorrect analysis, total fast recognitions (and that are insight/analysis)
    total_attempts = (real & attempts).sum()
    total_correct = (real & correct).sum()
    total_insight = (real & insight).sum()
    total_analysis = (real & analysis ).sum()
    correct_insight = (real & correct & insight).sum()
    correct_analysis = (real & correct & analysis).sum()

    # Create the individual summary
    # purposely creating an ordered dict so that order is maintained when constructing the df
    individual_dict = OrderedDict([('participant', pid),
                                   ('condition', condition),
                                   ('total_attempts', total_attempts),
                                   ('total_correct', total_correct),
                                   ('total_insight', total_insight),
                                   ('total_analysis', total_analysis),
                                   ('correct_insight', correct_insight),
                                    ('correct_analysis', correct_analysis),
                                    ('expName', data['expName'][0]),
                                    ('expDate', data['date'][0])
                                    ])

    individual_filename = 'data/individual_summary/%s_%s_cra_%s_%s.csv' %(pid, condition, date, unique_id)
    individual_df = pd.DataFrame(individual_dict,index=[0])

    if os.path.isfile(individual_filename) == False:
        # Save the individual clean data to a new CSV, in the clean_data folder
        individual_df.to_csv(individual_filename, index=False)
        print 'created individual summary file for %s' % (pid)

    else:
        print 'duplicate filename exists'
        print '%s' % (clean_filename)

    # Add the individual summary to the combined summary dataframe
    combined_summary = pd.concat([combined_summary, individual_df])

# Save the combined summary
# create a unique id to avoid overwriting the last one (if made on the same date)
unique_id = random.randrange(0,9999)
combined_filename = 'data/combined_summary/cra_%s_%s.csv' %(date, unique_id)
combined_summary.to_csv(combined_filename, index=False)
print 'combined summary file created'
print 'Data preprocessing complete!'