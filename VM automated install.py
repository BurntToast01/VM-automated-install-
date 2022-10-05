# This is still a work in progess. it'll take a few more functions to finish this off.

import time
import pyautogui
import pyautogui as wagie
import cv2 as cv
import numpy as np
from PIL import ImageGrab
main_templates=["/home/something/PycharmProjects/REDLIGHT automation/OracaleStart.png",
                "/home/something/PycharmProjects/REDLIGHT automation/Gnome okay2.png",
                ]

class automated:
    def __init__(self, ostype, RAM_amount,x):
        self.ostypes = ostypes=["windowsvista","windows7","windows8","windows8.1","windows10","windows11","fedora",
                               "manjaro","linux mint","ubuntu"]
        self.ostype=ostype
        self.RAM = RAM_amount
        self.template = x
        self.counter= 0
        self.checking_start()
    def checking_start(self,):
        checking_counter=0
        while len(self.ostype) == 0:

            print ("You forgot the OS type...")
            self.ostype=input("Please, give me the OS type!: ")
        else:
            pass
            #print(type(self.RAM))
            #pyautogui.press('f12')
            #self.checking_counter+=1
            #print(self.counter)

        for i in self.ostypes:
            if self.ostype not in self.ostypes:
                print ("sorry, I dont know what the OS is. Try putting in something else or maybe your input has a "
                       "space.""\n""try typing the os all in one word.")
                self.ostype = input ("Please, give me the OS type!: ")

        if int (self.RAM) == int (420):
            print ("WEEED!""\n""but for real you need but some more RAM")
            x=self.RAM = input ("So, how much RAM are you going to use?: ")
            if int(x)==int(420):
                self.RAM=input ("Come on, stop fucking around. How much RAM are you going to use?: ")



        if int(self.RAM)>=int(9999):
            print ("yo, that's over 10gb of RAM. That's way too much, bruh. try putting in something lower")
            self.RAM = input ("Please, give me a more reasonable amount of RAM to use!: ")
        else:
            pass

        if len(self.ostype)>0:
            if int (len (self.RAM)) < int (9999):

                print ("\n""Great, you are going to be using", self.ostype.upper (), "as your your OS and",
                               self.RAM,
                               "MB amount of RAM.",
                               "\n""Lets get started by letting Opencv start doing the rest.")


            a = input ("Press enter or any key to continue")
            if len (a) >= 0:
                # pyautogui.press ('f12')
                time.sleep (1)
                wagie.press ('winleft')
                time.sleep (1)
                wagie.typewrite ('Oracle')
                time.sleep (1)
                wagie.press ('enter')
                time.sleep (2)
                self.find_vmButton ()
            #self.find_vmButton ()


    def find_vmButton(self):
        self.counter1 = 0
        REGION = 402, 1157, 34, 33
        self.REGION_vmButton = x, y, w, h = REGION
        job_done = 0
        template = cv.imread (self.template[0])
        template_gray = np.array (cv.cvtColor (template, cv.COLOR_RGB2GRAY))
        #cv.imshow ('lookoverhere', template_gray)
        #cv.waitKey (1000)
        while True:

            # DO NOT change this screen capture 
            # Use this to start matching templates with Opencv.
            a = np.array (ImageGrab.grab (bbox=(x, y, x + w, y + h)))
            #print(self.REGION)
            b = cv.cvtColor (a, cv.COLOR_RGB2GRAY)
            # the line of code is to make sure we can see a live image from the screen
            #cv.imshow ('lookoverhere', b)
            #cv.waitKey (500)
            result = cv.matchTemplate (
                image=b,
                templ=template_gray,
                method=cv.TM_CCOEFF_NORMED, )

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc (result)
            #print (min_val, max_val)
            if max_val >= 0.99:
                pyautogui.rightClick (
                    x=max_loc[0] + x,  # screen x
                    y=max_loc[1] + y
                )  # screen y_
                self.counter1 += 1
                # print (min_val, max_val, min_loc, max_loc)
                # print (min_val, max_val, min_loc, max_loc)
            if self.counter1 == 1:
                # print (min_val, max_val, min_loc, max_loc)
                # print (x, y, w, h)
                end = time.time ()
                #print (end - start)

                print("find_vmButton was successful")
                break

            if max_val <= 0.90:
                # this part is only to catch if and when the image moves from the original REGION location
                # if the image/window has not been moved this section of the code will NOT execute
                ##TODO: maybe force the script to get the window you're looking for, then use ImageGrab.grab (bbox=) instead of pyautogui
                ## maybe pass it the dimensions of the enterie screen or a known location for the general are? dont sweat it too much
                ## it find the image really quickly, though, we're not sure how well this wouldd work with moving images
                while 1:
                    locations = pyautogui.locateOnScreen (
                        "/home/something/PycharmProjects/REDLIGHT automation/OracaleStart.png", confidence=0.8,
                        grayscale=True)
                    if locations is not None:
                        self.REGION_vmButton =x, y, w, h= locations
                        #print(x, y, w, h)

                        print("Button was not in its place. Had to look for it.")
                        break
                    else:
                        locations = pyautogui.locateOnScreen (
                            "/home/something/PycharmProjects/REDLIGHT automation/OracaleStart.png", confidence=0.8,
                            grayscale=True)




    def Phase2(self):
        print("looking for button")
        start = time.time ()
        REGION = 402, 1163, 34, 33
        x, y, w, h = REGION
        job_done = 0
        template = cv.imread ("/home/something/PycharmProjects/REDLIGHT automation/OracaleStart.png")
        template_gray = np.array (cv.cvtColor (template, cv.COLOR_RGB2GRAY))
        # cv.imshow ('a', template_gray)
        # cv.waitKey (250)
        # The code below does not seem to be needed for this to work.
        # template_gray.astype(np.uint8)

        while True:
            # DO NOT change this screen capture you dumb fuck
            # Use this to start matching templates with Opencv.
            a = np.array (ImageGrab.grab (bbox=(x, y, x + w, y + h)))
            b = cv.cvtColor (a, cv.COLOR_RGB2GRAY)
            # the line of code is to make sure we can see a live image from the screen
            # cv.imshow ('lookoverhere', b)
            cv.waitKey (1)
            result = cv.matchTemplate (
                image=b,
                templ=template_gray,
                method=cv.TM_CCOEFF_NORMED, )

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc (result)
            print (min_val, max_val)
            if max_val >= 0.99:
                pyautogui.rightClick (
                    x=max_loc[0] + x,  # screen x
                    y=max_loc[1] + y
                )  # screen y_
                job_done += 1
                # print (min_val, max_val, min_loc, max_loc)
                # print (min_val, max_val, min_loc, max_loc)
            if job_done == 1:
                # print (min_val, max_val, min_loc, max_loc)
                # print (x, y, w, h)
                end = time.time ()
                print (end - start)
                break

            if max_val <= 0.90:
                # this part is only to catch if and when the image moves from the original REGION location
                # if the image/window has not been moved this section of the code will NOT execute
                ##TODO: maybe force the script to get the window you're looking for, then use ImageGrab.grab (bbox=) instead of pyautogui
                ## maybe pass it the dimensions of the enterie screen or a known location for the general are? dont sweat it too much
                ## it find the image really quickly, though, we're not sure how well this wouldd work with moving images
                while 1:
                    locations = pyautogui.locateOnScreen (
                        "/home/something/PycharmProjects/REDLIGHT automation/OracaleStart.png", confidence=0.9,
                        grayscale=True)
                    if locations is not None:
                        x, y, w, h = locations
                        print (x, y, w, h)
                        break
                    else:
                        locations = pyautogui.locateOnScreen (
                            "/home/something/PycharmProjects/REDLIGHT automation/OracaleStart.png", confidence=0.9,
                            grayscale=True)





a = automated (input("What OS would you like to use?: " ), input("How much Mb's of RAM?: "),main_templates)
a

