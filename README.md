# Compound Remote Associates task - PsychoPy2 1.90.3 version
Code to run a CRA task for your own creativity (insight) studies!

This Compound Remote Associates (CRA) task was developed in the Beeman Lab and is run on PsychoPy, an open-source experiment application. Currently, this code is only guaranteed to work on Windows.  Unfortunately, I don't have a Mac to test the code for compatibility.

With this code, you can present any number of CRA problems for a given time period (e.g., 15 seconds). Participants can make either a verbal response (which requires an experimenter to score the responses) or input their responses directly in PsychoPy. Participants will also be asked how they solved the problem: whether by insight or by analysis. For an example of a typical CRA trial, see the gif below!

![Example of a CRA trial](https://tiffaning.com/files/images/cra_preview.gif?)

__*Note*: This repo does NOT contain a full set of CRA problems. This is to prevent potential participants from having complete access to CRA solutions (for MTurk studies, etc). If you require a list of CRA problems, you can contact me directly via [email](https://mailhide.io/e/etceE).__

## Citing This Code & License Information
If you use this code in your experiments, please cite my Github Repository in your publications!
```
Tiffani Ng. (2019, September 21). Compound Remote Associates task for PsychoPy2 (Version v1.0). Zenodo. http://doi.org/10.5281/zenodo.3457283
```

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3457283.svg)](https://doi.org/10.5281/zenodo.3457283)

This code is licensed under the GNU General Public License v3.0. You may modify the code for your personal/research use; however, any modifications made for distributed must be documented and attributed to the source (this repo) under the same license. You may read more about what you can do with this licensed work [here](https://choosealicense.com/licenses/gpl-3.0/). 

## Version Information
This version of the CRA task runs on an older version of PsychoPy ([PsychoPy2, version 1.90.3](https://github.com/psychopy/psychopy/releases/tag/1.90.3)). You cannot run this task on the latest version of PsychoPy! A PsychoPy3 version will be released soon.

## Installation
1. Download and install PsychoPy2 from [here](https://github.com/psychopy/psychopy/releases/tag/1.90.3).
2. Download the files from this repo and unzip the directory into your desired location.
3. Open the Coder Window in PsychoPy2 (View > Open Coder View).
4. Drag and drop (or File > Open) the __CRA PsychoPy2.py__ file into the Coder Window. A new tab should appear with the python file opened. 
5. Hit Run to start the task!
__Note__: You can prevent any accidental keyboard input from distrupting the code by checking __"read-only"__ in PsychoPy Preferences > Coder. This is highly recommended prior to running any participants, since any mis-types made in the Coder Window will certainly cause errors and prevent your task from running.

## Procedure
1. Instructions presented to the participant.
2. Practice CRA problems.
	1. Fixation cross is presented. 
	2. 3 problem words are presented on center of the screen.
	3. Participant presses the spacebar if they reach the solution within the 15 second solution window.
		If they do not reach a solution, the program proceeds to the next problem.
	4. If they pressed spacebar, they will either be asked to give the solution aloud (__verbal input version__) or input their solution into a textbox on the screen (__participant input version__).
	5. If they solved the problem, they will be asked to indicate whether they solved with insight or analysis.
3. Test CRA problems, repeatign the steps under practice CRA problems for each CRA problem.
4. Break screen / End of task screen

## Default Settings
Below are the settings that I used by default when compiling this code. To change any of these settings, please refer to the Modifications section below.

### Keypresses
* __To advance the instructions (experimenter)__: LEFT SHIFT (lshift)
* __To quit the experiment (experimenter)__: ESC (esc)
* __To advance to next problem (participant)__: SPACEBAR (space)
* __Solution reached (participant)__: SPACEBAR (space)
* __Solution reached by insight (participant)__: F key 
* __Solution reached by analysis (participant)__: J key

### Timing
* __Fixation Presentation Time__: 0.8 seconds (800 ms)
* __CRA Presentation Time (Solution Window)__: 15 seconds

### Solution Input
There are two versions of this task:
* __Verbal input__ (cra_verbal_input.py)
	* Participant gives a verbal solution to the experimenter.
	* Experimenter inputs whether the solution was correct (__A key__) or incorrect (__Z key__).
* __Participant input__ (cra_ppt_input.py) 
	* Participant types the solution into a dialog/text box that pops up after they indicate they have reached solution (pressed spacebar).

## Modifications
Under the GNU license, you are free to modify this code for your personal/research use. You can refer to the sections below (or the comments included in the python code) to help you understand the structure of this code.

### Modifying Task Instructions
Instructions for the CRA task are CSV files, which means you can edit them in whatever program you typically use to edit CSV files (e.g., Excel, Notepad). 
* __Introductory CRA instructions__ (cra_instr.csv / cra_instr_input.csv) 
	* Contains all of the instructions for participants new to the CRA task. 
	* Explains what CRAs problems are, and how to solve them.
	* Explains insight and analysis.
	* Steps through the basic solving procedure (spacebar, solution, insight/analysis) with participants.
* __Shorter (reminder) CRA instructions__ (cra_reinstr.csv)
	* If participants are returning to the CRA task from another task, you might want to replace the Introductory CRA instructions with this briefer reminder version.
*  __Break__ (break.csv)
	* Indicates end of a block, when participants can take a break.
*  __End of task__ (end.csv)
	* Indicates the end of the task.

#### Instruction CSV file structure
There are only two columns in each instructions file: "instructions" and "key".

__instructions__
* Contains the instruction text. 
* Each row is a new "slide" in the instructions. 
* Line breaks are denoted by double quotation marks ( " ).

__key__
* The key the experimenter or participant should press to advance the script to the next "slide".
* By default, experimeter advance is LEFT SHIFT (lshift) and participant advance is SPACEBAR (space).
* If you want to change the key to a NUMERIC (e.g., '2' key), you must save the key column as TEXT. This will be easy if you are editing the CSV in a text editor (you would encapsulate the 2 with single quotations, like so: '2'). In Excel, you must select the column and change the number format to TEXT.

#### A note on saving CSV files with Excel: 
When you save the changes, you should make sure that they were saved as a CSV (Comma delimited) file. Saving as a UTF-8 CSV file will raise errors in PsychoPy2.

### Modifying Script Components
There are several components that can be modified in the script directly. You can change the text in these components directly in the code. Approximate line numbers for each component are referenced here to make finding the component easier (assuming you are modifying a clean version of the code).

#### Experimental Information
* Experiment name (default: "CRA") ~ Line 22-23 
```
expName = 'CRA'  #name of your experiment
```
* Conditions (default: "1", "2") ~ Line 55-56
```
condition_list = ['1','2']
```

#### Sound on fixation
You can add a sound that plays when the fixation cross is shown.

Uncomment the following lines:
Approximately lines 136-138
```
# ready = sound.Sound('A', octave=4, sampleRate=44100, secs=0.8)
# ready.setVolume(0.8)
```

Approximately line 257 ~ 266
```
 # ready.play()
```

#### Code does not autosave upon crashing/esc 
If, for whatever reason, PsychoPy is not automatically saving the output as a CSV file after a program crash or hitting ESC to exit, you can uncomment this line:
Approximately line 155~156
```
# thisExp.saveAsWideText(thisExp.dataFileName + '.csv', delim=',')
```

## Preprocessing CRA Output
Included with the CRA task is a python script (__summary.py__) that quickly iterates through the CSV data files generated by PsychoPy and outputs the following:
* Individual cleaned files 
	* All of the columns with irrelevant task information (e.g., loop trackers) are removed.
	* Only columns with task-relevant information (e.g., correct/solution RTs/insight/analysis) are kept.
* Individual summary files
	* Contains sums of the number of correct responses, insight solutions, analytic solutions, and fast recognition (solutions given within 2 seconds). 
	* There is a separate version of this script that does not categorize fast recognition solutions (summary_keep_fast.py), but the [literature](https://www.researchgate.net/profile/Jarrod_Moss/publication/258345147_Is_insight_always_the_same_An_fMRI_study_of_insight/links/0c96052801cac6d135000000.pdf) suggests that fast recognitions are different from insights. 
* Group summary files
	* Compiles all of the individual summary files into one large summary file. 

This script can be run in PsychoPy2, just like the task files. 
Data must be stored in the original 'data' folder, or an error will be raised, preventing the script from proceeding.

## Common Issues
#### If you are on Windows 10 ver 1903, you may encounter this error:
```
AssertionError: GetDeviceGammaRamp failed
Exception AttributeError: "'NoneType' object has no attribute 'close'" in <bound method Window.__del__ of <psychopy.visual.window.Window object at 0x1C40AC50>> ignored
```
This appears to be a common error for people using PsychoPy on ver 1903 ([example](https://discourse.psychopy.org/t/error-message-since-windows-update-to-1903/8355)), which suggests that it is an issue native to this version of Windows, and it is not an issue with this code or PsychoPy.

Possible fixes include:
1. Downgrading to a previous version of Windows until this issue is fixed by Microsoft.
2. If you are using multiple monitors, having the setting "Extend these displays" may be the cause of this issue. Simply change the setting to "Show only on 1", and the code should run. *This fixes the issue for me.*
3. Downgrade pyglet to 1.3.0. If you installed PsychoPy via Standalone, you will need to [do some extra work](https://www.psychopy.org/recipes/addCustomModules.html). *I also cannot guarantee this fixes the issue, since I have not tried it myself.*

#### Issues with full screen and participant input
Due to limitations native to PsychoPy, you cannot use fullscreen with the participant input version of the CRA task.  The dialog box (where participants input their solution) is designed (by PsychoPy) to appear behind a fullscreen, so it does not appear when fullscreen is on. Although it seems like this issue has previously been addressed by PsychoPy [here](https://discourse.psychopy.org/t/dialog-boxes-and-fullscr-windows/2373), in my experience, it does not always work. For this reason, we keep fullscreen off for this version of the CRA task.

## Other Questions/Bug Reports
Feel free to contact me via [email](https://mailhide.io/e/etceE) if you have any questions about using this code or if you encounter any strange errors/bugs (you can alternatively submit an issue on GitHub).
