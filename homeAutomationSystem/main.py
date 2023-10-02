#!/usr/bin/python3

from classes.homeAutomationSystemServer import *
import os


homeAutomationSystemServer = HomeAutomationSystemServer(os.path.dirname(os.path.abspath(__file__)))
if homeAutomationSystemServer.start():
    homeAutomationSystemServer.run()