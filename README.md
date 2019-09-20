# Compound Remote Associates task - PsychoPy2 1.90.3 version
Code to run a CRA task for your own creativity (insight) studies!

This Compound Remote Associates (CRA) task was developed in the Beeman Lab and is run on PsychoPy, an open-source experiment application. Currently, this code is only guaranteed to work on Windows.  Unfortunately, I don't have a Mac to test the code for compatibility.

With this code, you can present any number of CRA problems for a given time period (e.g., 15 seconds). Participants can make either a verbal response (which requires an experimenter to score the responses) or input their responses directly in PsychoPy. Participants will also be asked how they solved the problem: whether by insight or by analysis. For an example of a typical CRA trial, see the gif below!

__*Note*: This repo does NOT contain a full set of CRA problems. This is to prevent potential participants from having complete access to CRA solutions (for MTurk studies, etc). If you require a list of CRA problems, you can contact me directly via [email](https://mailhide.io/e/etceE).__

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

## Modifications
Under the GNU license, you are free to modify this code for your personal/research use. You can refer to the sections below (or the comments included in the python code) to help you understand the structure of this code.

### Modifying Task Instructions
Instructions for the CRA task are CSV files, which means you can edit them in whatever program you typically use to edit CSV files (e.g., Excel, Notepad). 

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
