#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Coded by Tiffani/Beeman Lab in PsychoPy

#-------------------------------- Python Imports --------------------------------------
# Don't remove anything from this section, but feel free to add if you are importing other packages
from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import pandas as pd
import numpy as np
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# ------------------------------- Experiment Information ----------------------------------
# This section includes experiment session information that gets put into your CSV (output)
# Includes an option to skip to a particular section, in case your program crashes and you don't want to completely start over ('which_part')
expName = 'CRA'  #name of your experiment
# The information that gets put into the pop-up upon hitting run/study start
expInfo = {'participant':'', 'condition':'','which_part':'0'} 
# Creates the dialog box that pops up upon hitting run/study start
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName


# -------------------------------- Filename Creation --------------------------------------
# Filename (that gets spit out at the end of the experiment) will include participant ID number, condition name, experiment name, and date + time
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['participant'], expInfo['condition'], expName, expInfo['date'])


# ------------------------------- Experiment Handler -------------------------------------
# Avoid changing the information below. We need this so our loops work later.
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
endExpNow = False  # flag for 'escape' or other condition => quit the exp


#--------------------------- Experimental Conditions Set-Up ------------------------------
# If you have multiple conditions, put the condition name below.
# You will probably want to keep it short. 
# I have currently put in some dummy conditions (ex1, ex2) to show you how it should look like.
# This is optional, but it helps to avoid accidental incorrect condition IDs in the data. 
# If you don't need it, you can comment it out.
condition_list = ['1','2']

# This creates a dialog box if the conditions are incorrect.
# You can comment this out if you're not using it/don't have multiple conditions.
errorDlg = gui.Dlg(title="Error", pos=(200,400))
if not (expInfo['condition'] in condition_list):
    errorDlg.addText('Invalid condition ID. Please enter a valid condition code.')
    errorDlg.show()
    raise Exception('Bad condition ID')


#------------------------------- Window and Monitor Set Up ---------------------------------	
# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=False)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

#-------------------------------- Components Creation --------------------------------------
# This section is where the components of the CRA trials are created (but not yet displayed). 
# Feel free to change the appearance of any of the components.
# (Refer to the PsychoPy documentation for more details.)

# This is the component for the instruction text that appears at the beginning of the experiment. 
# Please do not put anything inside the text='' part.
# The code relies on adding text dynamically (each loop) to this section, so if you put text here, it will be included in each of your instruction text.
# If you need to change the instructions for any part of the experiment, please see the following CSV files:

instructions = visual.TextStim(win=win, ori=0, name='instructions',
                                   text='', font='Arial', pos=[0, 0], height=0.06, wrapWidth=1.25,
                                   color='black', colorSpace='rgb', opacity=1, depth=0.0)


# This is the component for the CRA problems. Please do not put anything inside the
cra = visual.TextStim(win=win, ori=0, name='cra',
                                   text='', font='Arial', pos=[0, 0], height=0.1, wrapWidth=1.25,
                                   color='black', colorSpace='rgb', opacity=1, depth=0.0)


# This is the text that comes up when the participant has pressed the spacebar, indicating that they have solved the problem.
solution = visual.TextStim(win=win, ori=0, name='solution',
                                   text='Please give the solution aloud.', font='Arial', pos=[0, 0], height=0.06, wrapWidth=1.25,
                                   color='black', colorSpace='rgb', opacity=1, depth=0.0)


# This creates the text asking how participants solved the problem (with insight or with analysis).
# Feel free to change the keys they use, as long as you also change it in the code 
# (Line or search:)
ins_ana = visual.TextStim(win=win, ori=0, name='ins_ana',
                                   text='Did you solve the problem with...\n\nINSIGHT (F/left key)? Or ANALYSIS (J/right key)?',
                          font='Arial', pos=[0, 0], height=0.06, wrapWidth=1.25,
                          color='black', colorSpace='rgb', opacity=1, depth=0.0)

# ------------------ Fixation Cross Component -------------------
# This is the fixation cross. 
# You can change it to any text symbol, size, color, etc you'd like. 
fixation = visual.TextStim(win=win, ori=0, name='fixation',
                                   text='+', font='Arial', pos=[0, 0], height=0.10, wrapWidth=1.25,
                                   color='black', colorSpace='rgb', opacity=1, depth=0.0)

# ------------------ Fixation Cross (Image Version) Component -------------------
# If you would like to change the fixation cross to an image instead, you would need to change this to an ImageStim (uncomment the code below, change the image path).
# fixation = visual.SimpleImageStim(win=win, image='PATH TO IMAGE HERE')								   

# ------------------ Participant Spacebar Advance Component -------------------
# This component is what participants will see when they need to start the next trial
space_advance = visual.TextStim(win=win, ori=0, name='space_advance',
                                   text='Ready for the next problem? (Press spacebar)', font='Arial', pos=[0, 0], height=0.05, wrapWidth=1.25,
                                   color='black', colorSpace='rgb', opacity=1, depth=0.0)

# Uncomment the two lines of code below if you would like to use a sound cue (i.e., a pure tone), such as to signal the start of a trial
# You will also need to uncomment line (or search for:)
# The first line creates the sound and determines how long it will play (800 ms)
# The second line sets the maximum volume that it will play at (you can also adjust the volume on your computer)
# ------------------ Ready Sound Component -------------------
# ready = sound.Sound('A', octave=4, sampleRate=44100, secs=0.8)
# ready.setVolume(0.8)


# ------------------ Clock Components -------------------
# The clocks are needed to keep track of timing in the experiment, such as the 15 second solution window and solution time.
stopwatch = core.Clock()
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine


#-------------------------------- Functions Creation --------------------------------------
# Changes to these functions will change them for EVERY use of the function.

# ------------------ Shutdown Function -------------------
# Makes a copy of the data in case of a crash (some PsychoPy versions were not auto-saving data after crashes; this is a fail-safe so that you do not lose your data in case the program crashes). 
# Also closes the PsychoPy window and quits. 
# Neater to keep it in a function since the two lines are used so often.
def shutdown():
    # thisExp.saveAsWideText(thisExp.dataFileName + '.csv', delim=',')
    win.close()
    core.quit()


# ------------------ Instructions Function -------------------	
# Malleable instructions function. 
# Changes to the INSTRUCTION TEXT are NOT made here. Those are made directly in the CSV file.
# Requires CSV file where instructions are located as the input (the parentheses after calling the function).
def instruction(instr_text):
# takes in the file or instruction text as an argument
# also takes in the keypress needed for that trial (tied to the instruction dictionary)
    global this_instructions
    global currentLoop
    instructions_handler = data.TrialHandler(nReps=1, method='sequential',
                                                 extraInfo=expInfo, originPath=None,
                                                 trialList=data.importConditions(instr_text),
                                                 seed=None, name='instructions_handler')
    thisExp.addLoop(instructions_handler)  # add the loop to the experiment
    this_instructions = instructions_handler.trialList[0]
    for this_instructions in instructions_handler:
        event.clearEvents(eventType='keyboard')
        currentLoop = instructions_handler

        # This is where the instruction text is set, but not yet drawn.
        # Additionally, it replaces double quotes (") as a line break.
        # Feel free to change that if you need to use double quotes, but you will also need to make the changes to all of the instruction CSV files.
        instructions_text = this_instructions['instructions']
        break_text = instructions_text.replace('"','\n')
        instructions.setText(break_text)
        instr_key = this_instructions['key']

        # This is where the instruction text that you set previously are drawn to the screen.
        continueRoutine = True
        while continueRoutine:
            instructions.draw()
            win.flip()

        # Ends this presentation when the appropriate key as defined in the CSV is pressed.
            if event.getKeys(keyList=[instr_key]):  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                shutdown()
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            shutdown()


# ------------------ CRA Function -------------------				
# Define which set by providing the path to the CRA CSV (cra_trials).
# Define what kind of block is it - practice or actual trials.
# The practice one is the most important to define here, as it differs slightly for practice trials.
def cra_block(cra_trials, blockType):
    global currentLoop
    global this_cra
    cra_handler = data.TrialHandler(nReps=1, method='sequential',
                                                 extraInfo=expInfo, originPath=None,
                                                 trialList=data.importConditions(cra_trials),
                                                 seed=None, name='cra_handler')
    thisExp.addLoop(cra_handler)  # add the loop to the experiment
    this_cra = cra_handler.trialList[0]

    # Also read in other required details from CSV:
    # Insight/analysis/solution keys
    # Length of Fixation and Solution Window
    required_keys = pd.read_csv('files/required/keys.csv')
    # get values of the solution/insight/analysis keys
    solution_key = required_keys.loc[required_keys['type']=='solution','key'].values[0]
    ins_key = required_keys.loc[required_keys['type']=='insight','key'].values[0]
    ana_key = required_keys.loc[required_keys['type']=='analysis','key'].values[0]
    correct_key = required_keys.loc[required_keys['type'] == 'correct', 'key'].values[0]
    incorrect_key = required_keys.loc[required_keys['type'] == 'incorrect', 'key'].values[0]

    cra_timing = pd.read_csv('files/required/timing.csv')
    # get values of the timing info for fixation cross and solution window
    fixation_time = cra_timing.loc[cra_timing['type'] == 'fixation', 'time'].values[0]
    cra_time = cra_timing.loc[cra_timing['type'] == 'cra', 'time'].values[0]

    # Loop for the CRA trials begin here
    for this_cra in cra_handler:
        event.clearEvents(eventType='keyboard')
        currentLoop = cra_handler

        # Sets the CRA text to be displayed later
        currentCRA = this_cra['cra']
        cra_break = currentCRA.replace(' ', '\n')
        cra.setText(cra_break)

        # which trial type/block is this?
        cra_handler.addData('block', blockType)

        # Asks participants if they are ready to start the next trial. Ends when they hit the spacebar (or whatever button you choose).
        space_advance.draw()
        win.flip()
        event.waitKeys(keyList=['space'])

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            shutdown()

        # play the ready sound with fixation cross
        # ready.play()

        # Draw the fixation cross for 800ms
        fixation.draw()
        win.flip()
        core.wait(fixation_time)

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            shutdown()

        # Important clocks to get RTs later and keep track of how much time remains in the trial
        event.clearEvents()
        routineTimer.reset()
        stopwatch.reset()
        # If you need to change the time for each trial, change 15 to any other second amount
        routineTimer.add(cra_time)

        # while they have time (15seconds), or until a response is made
        continueRoutine = True
        while continueRoutine==True and (routineTimer.getTime() > 0):
            cra.draw()
            win.flip()

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                shutdown()

            cra_attempted = event.getKeys(keyList=[solution_key], timeStamped=stopwatch)

            # only if there is no response, quit this loop and move onto the next trial
            if routineTimer.getTime() <= 0 and len(cra_attempted)==0:
                continueRoutine = False

            # If the participant attempted the CRA, it will keep track of the RTs here and the key they pressed (i.e., spacebar).
            # Then, it will ask participant to give their answer (input).
            if len(cra_attempted) > 0:
                cra_key, cra_rt = zip(*cra_attempted)
                cra_key = cra_key[0]
                cra_rt = cra_rt[0]
                cra_handler.addData('cra_key', cra_key)
                cra_handler.addData('cra_rt', cra_rt)
                event.clearEvents()

             # Show the solution screen
                solution.draw()
                win.flip()

                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    shutdown()

            # !!!!!!! CORRECT/INCORRECT KEYS !!!!!!!!
            # Feel free to change 'num_1' and 'num_0' to whatever keys you choose.
            # You will need to make the changes below as well.
                cra_solution = event.waitKeys(keyList=[incorrect_key, correct_key])
                # save correct or incorrect
                if len(cra_solution) > 0:
                    cra_correct = cra_solution[0]
                    if cra_correct == correct_key:
                        was_correct = '1'
                    elif cra_correct == incorrect_key:
                        was_correct = '0'

                    # Adds correct/incorrect data, to be saved later
                    cra_handler.addData('craCorrectKey', cra_solution[0])
                    cra_handler.addData('craCorrect', was_correct)
                    event.clearEvents()

                # Ask how they solved the problem, whether by insight/analysis
                ins_ana.draw()
                win.flip()

                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    shutdown()

                # !!!!!!! INSIGHT/ANALYIS KEYS !!!!!!!!
                # If you want to change the key for the INSIGHT and ANALYSIS rating
                # Change 'f' and 'j' to whatever keys you choose to use.
                cra_InsAna = event.waitKeys(keyList=[ins_key, ana_key])
                # move on once you get the rating, and don't forget to save the response
                if len(cra_InsAna) > 0:
                    if cra_InsAna[0] == ins_key:
                        InsAna = 'ins'
                    elif cra_InsAna[0] == ana_key:
                        InsAna = 'ana'
                    cra_handler.addData('InsAnaKey', cra_InsAna[0])
                    cra_handler.addData('InsAnaWas', InsAna)
                    continueRoutine=False

                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    shutdown()

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                shutdown()
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            shutdown()

        # Adds the entry to the trial handler, and lets the program know to move to the next loop
        thisExp.nextEntry()


# ------------------ Experiment Procedure -------------------				
# The experiment is broken up into 5 parts (note the 'which_part' numbers).	
# CRA instructions first
if expInfo['which_part'] == '0':
    instruction('files/instructions/cra_instr.csv')
    expInfo['which_part'] = '1'

# CRA practice problems
# If participants do not pass the first set of practice problems by solving at least 1 problem correctly, it will move onto the second set of practice problems
if expInfo['which_part'] == '1':
    # if they pass the practice, continue to the real trials + show the instruction for that
    # otherwise, do 3 more practice problems
    practice1 = cra_block('files/cra_lists/cra_practice1.csv', 'practice')
    # if they could not even solve 1 problem, make them do a few more practice problems
    instruction('files/instructions/cra_reinstr.csv')
    expInfo['which_part'] = '2'

# do the real CRA trials - block 1
# Also break text after the block ends
if expInfo['which_part'] == '2':
    cra_block('files/cra_lists/cra_1.csv', 'first')
    instruction('files/instructions/break.csv')
    expInfo['which_part'] = '3'

# CRA block 2
# Also break text after the block ends
if expInfo['which_part'] == '3':
    cra_block('files/cra_lists/cra_2.csv', 'second')
    instruction('files/instructions/break.csv')
    expInfo['which_part'] = '4'

# CRA block 3 (Final block)
# Also end text after the block ends
if expInfo['which_part'] == '4':
    cra_block('files/cra_lists/cra_3.csv','third')
    instruction('files/instructions/end.csv')
    # quit code here, clean up
    if endExpNow or event.getKeys(keyList=["escape"]):
        shutdown()