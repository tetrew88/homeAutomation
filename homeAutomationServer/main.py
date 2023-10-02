#!/usr/bin/python3

from classes.homeAutomationServer import *
import os


homeAutomationServer = HomeAutomationServer(os.path.dirname(os.path.abspath(__file__)))
if homeAutomationServer.start():
    homeAutomationServer.run()