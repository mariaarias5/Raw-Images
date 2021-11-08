#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on November 05, 2021, at 13:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'trial'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Master\\4th Semester\\Master thesis\\Psy\\Raw Images\\RE_experiment_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
Key_welcome_response = keyboard.Keyboard()
Welcome_text = visual.TextStim(win=win, name='Welcome_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "CrossFix"
CrossFixClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)

# Initialize components for Routine "Video_Trials"
Video_TrialsClock = core.Clock()

# Initialize components for Routine "Image_no_background"
Image_no_backgroundClock = core.Clock()
No_background_image = visual.ImageStim(
    win=win,
    name='No_background_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=[0.8,0.45],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Trial_response = event.Mouse(win=win)
x, y = [None, None]
Trial_response.mouseClock = core.Clock()

# Initialize components for Routine "GoodBye"
GoodByeClock = core.Clock()
goodbye = visual.TextStim(win=win, name='goodbye',
    text='Thank you for participating!\n\nPress SPACEBAR to end the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
Key_welcome_response.keys = []
Key_welcome_response.rt = []
_Key_welcome_response_allKeys = []
Welcome_text.setText('Welcome!\n\nIn this experiment, you will be presented with some videos.\n\nPlease use the mouse and click on the screen, to indicate where it was the last time that the object appear. \n\nIf you have any questions consult the experimenter.\n\nOnce you have understood this, press SPACEBAR to begin.')
# keep track of which components have finished
WelcomeScreenComponents = [Key_welcome_response, Welcome_text]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Key_welcome_response* updates
    waitOnFlip = False
    if Key_welcome_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Key_welcome_response.frameNStart = frameN  # exact frame index
        Key_welcome_response.tStart = t  # local t and not account for scr refresh
        Key_welcome_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Key_welcome_response, 'tStartRefresh')  # time at next scr refresh
        Key_welcome_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Key_welcome_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Key_welcome_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Key_welcome_response.status == STARTED and not waitOnFlip:
        theseKeys = Key_welcome_response.getKeys(keyList=['space'], waitRelease=False)
        _Key_welcome_response_allKeys.extend(theseKeys)
        if len(_Key_welcome_response_allKeys):
            Key_welcome_response.keys = _Key_welcome_response_allKeys[-1].name  # just the last key pressed
            Key_welcome_response.rt = _Key_welcome_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Welcome_text* updates
    if Welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_text.frameNStart = frameN  # exact frame index
        Welcome_text.tStart = t  # local t and not account for scr refresh
        Welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_text, 'tStartRefresh')  # time at next scr refresh
        Welcome_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Key_welcome_response.keys in ['', [], None]:  # No response was made
    Key_welcome_response.keys = None
thisExp.addData('Key_welcome_response.keys',Key_welcome_response.keys)
if Key_welcome_response.keys != None:  # we had a response
    thisExp.addData('Key_welcome_response.rt', Key_welcome_response.rt)
thisExp.addData('Key_welcome_response.started', Key_welcome_response.tStartRefresh)
thisExp.addData('Key_welcome_response.stopped', Key_welcome_response.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Welcome_text.started', Welcome_text.tStartRefresh)
thisExp.addData('Welcome_text.stopped', Welcome_text.tStopRefresh)
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "CrossFix"-------
continueRoutine = True
routineTimer.add(0.250000)
# update component parameters for each repeat
# keep track of which components have finished
CrossFixComponents = [polygon]
for thisComponent in CrossFixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CrossFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "CrossFix"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = CrossFixClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CrossFixClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 0.25-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CrossFixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CrossFix"-------
for thisComponent in CrossFixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Loop1 = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('VideoStimuli.xlsx'),
    seed=None, name='Loop1')
thisExp.addLoop(Loop1)  # add the loop to the experiment
thisLoop1 = Loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in Loop1:
    currentLoop = Loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Video_Trials"-------
    continueRoutine = True
    # update component parameters for each repeat
    Trial_videos = visual.MovieStim3(
        win=win, name='Trial_videos',
        noAudio = True,
        filename=videos,
        ori=0.0, pos=(0, 0), opacity=None,
        loop=False,
        size=[840,460],
        depth=0.0,
        )
    print(videos)
    # keep track of which components have finished
    Video_TrialsComponents = [Trial_videos]
    for thisComponent in Video_TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Video_TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Video_Trials"-------
    while continueRoutine:
        # get current time
        t = Video_TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Video_TrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_videos* updates
        if Trial_videos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_videos.frameNStart = frameN  # exact frame index
            Trial_videos.tStart = t  # local t and not account for scr refresh
            Trial_videos.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_videos, 'tStartRefresh')  # time at next scr refresh
            Trial_videos.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Video_TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Video_Trials"-------
    for thisComponent in Video_TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial_videos.stop()
    # the Routine "Video_Trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ImageStimuli.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Image_no_background"-------
        continueRoutine = True
        # update component parameters for each repeat
        No_background_image.setImage(filename_image)
        # setup some python lists for storing info about the Trial_response
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        Image_no_backgroundComponents = [No_background_image, Trial_response]
        for thisComponent in Image_no_backgroundComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Image_no_backgroundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Image_no_background"-------
        while continueRoutine:
            # get current time
            t = Image_no_backgroundClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Image_no_backgroundClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *No_background_image* updates
            if No_background_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                No_background_image.frameNStart = frameN  # exact frame index
                No_background_image.tStart = t  # local t and not account for scr refresh
                No_background_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(No_background_image, 'tStartRefresh')  # time at next scr refresh
                No_background_image.setAutoDraw(True)
            # *Trial_response* updates
            if Trial_response.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Trial_response.frameNStart = frameN  # exact frame index
                Trial_response.tStart = t  # local t and not account for scr refresh
                Trial_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Trial_response, 'tStartRefresh')  # time at next scr refresh
                Trial_response.status = STARTED
                Trial_response.mouseClock.reset()
                prevButtonState = Trial_response.getPressed()  # if button is down already this ISN'T a new click
            if Trial_response.status == STARTED:  # only update if started and not finished!
                buttons = Trial_response.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Image_no_backgroundComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Image_no_background"-------
        for thisComponent in Image_no_backgroundComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('No_background_image.started', No_background_image.tStartRefresh)
        trials.addData('No_background_image.stopped', No_background_image.tStopRefresh)
        # store data for trials (TrialHandler)
        x, y = Trial_response.getPos()
        buttons = Trial_response.getPressed()
        trials.addData('Trial_response.x', x)
        trials.addData('Trial_response.y', y)
        trials.addData('Trial_response.leftButton', buttons[0])
        trials.addData('Trial_response.midButton', buttons[1])
        trials.addData('Trial_response.rightButton', buttons[2])
        trials.addData('Trial_response.started', Trial_response.tStart)
        trials.addData('Trial_response.stopped', Trial_response.tStop)
        # the Routine "Image_no_background" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 2.0 repeats of 'trials'
    
# completed 2.0 repeats of 'Loop1'


# ------Prepare to start Routine "GoodBye"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
GoodByeComponents = [goodbye, key_resp_2]
for thisComponent in GoodByeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodByeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GoodBye"-------
while continueRoutine:
    # get current time
    t = GoodByeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodByeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye* updates
    if goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye.frameNStart = frameN  # exact frame index
        goodbye.tStart = t  # local t and not account for scr refresh
        goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye, 'tStartRefresh')  # time at next scr refresh
        goodbye.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodByeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GoodBye"-------
for thisComponent in GoodByeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('goodbye.started', goodbye.tStartRefresh)
thisExp.addData('goodbye.stopped', goodbye.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "GoodBye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
