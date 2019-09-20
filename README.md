# Compound Remote Associates task - PsychoPy2 1.90.3 version
Code to run a CRA task for your own creativity (insight) studies!

This Compound Remote Associates (CRA) task was developed in the Beeman Lab and is run on PsychoPy, an open-source experiment application. Currently, this code is only guaranteed to work on Windows.  Unfortunately, I don't have a Mac to test the code for compatibility!.

With this code, you can present any number of CRA problems for a given time period (e.g., 15 seconds). Participants can make either a verbal response (which requires an experimenter to score the responses) or input their responses directly in PsychoPy. Participants will also be asked how they solved the problem: whether by insight or by analysis. For an example of a typical CRA trial, see the gif below!

__*Note*: This repo does NOT contain a full set of CRA problems. This is to prevent potential participants from having complete access to CRA solutions (for MTurk studies, etc). If you require a list of CRA problems, you can contact me directly via [email](https://mailhide.io/e/etceE) or submit a request here.__

## Citing This Code & License Information
If you use this code in your experiments, please cite my Github Repository in your publications!

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

## Modifications
Under the GNU license, you are free to modify this code for your personal/research use. You can refer to the sections below (or the comments included in the python code) to help you understand the structure of this code.

### Modifying Task Instructions
Instructions for the CRA task are CSV files, which means you can edit them in whatever program you typically use to edit CSV files (e.g., Excel, Notepad). 
