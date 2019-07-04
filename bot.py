# Automate android device with adb
# https://pythonbasics.org
import os

def android_tap(x,y):
    os.system("adb shell input tap " + x + " " + y)

def android_type(text):
    os.system('adb shell input text "' + text + '"')

android_type("great")
