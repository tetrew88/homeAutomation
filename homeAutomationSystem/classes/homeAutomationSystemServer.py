import eventlet
eventlet.monkey_patch(os=True,select=True,socket=True,thread=True,time=True)

import threading
import socketio

import sys
import os

import json

import time

sys.path.append("..")
from homeAutomationSystem.homeAutomationSystem.classes.homeAutomationSystem import *


homeAutomationSystemSocket = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(homeAutomationSystemSocket, object)

homeAutomationServerSocket = socketio.Client(logger=True, engineio_logger=True)


class HomeAutomationSystemServer(socketio.Namespace):

    homeAutomationSystem = False

    def __init__(self, scriptPath):
        self.scriptPath = scriptPath
        self.configFilePath = scriptPath + '/configs/homeAutomationSystemConfig.json'
        
        self.running = False

        socketio.Namespace.__init__(self, '/HomeAutomationSystem')


    @staticmethod
    def set_home_automation_sytem(self):
        succes = False
        homeAutomationSystemScriptPath = self.scriptPath + '/homeAutomationSystem'
        try:
            HomeAutomationSystemServer.homeAutomationSystem = HomeAutomationSystem(homeAutomationSystemScriptPath, homeAutomationServerSocket)
            succes = True
        except Exception as e:
            print(e)
            succes = False

        return succes



    @property
    def homeAutomationServerIp(self):
        homeAutomationServerIp = data = False
        try:
            with open(self.configFilePath) as configFile:
                data = json.load(configFile)
        except:
            data = False
            
        if data != False:
            homeAutomationServerIp = data["homeAutomationServerIp"]
        else:
            homeAutomationServerIp = False

        return homeAutomationServerIp



    ###BASE METHODS###
    def start(self):
        succes = False

        if self.set_home_automation_sytem(self):
            print("111111")
            if self.connect_to_home_automation_server():
                print("2222222222222")
                """
                if self.homeAutomationSystem.start():
                    print('3333333333333')
                    self.running = True
                    succes = True
                else:
                    succes = False
                """
                succes = True
                self.running = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def stop(self):
        succes = False
        if self.homeAutomationSystem.stop():
            self.running = False
            succes = True
        else:
            succes = False

        return succes


    def restart(self):
        succes = True

        if self.stop():
            if self.start():
                succes = True
            else:
                succes = False
        else:
            succes = False

        return succes


    def listen_clients(self):
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)


    def listen_home_automation_server(self):
        homeAutomationServerSocket.wait()


    def connect_to_home_automation_server(self):
        succes = False

        homeAutomationServerAdress = "http://{}:5000".format(self.homeAutomationServerIp)

        try:
            homeAutomationServerSocket.connect(homeAutomationServerAdress, transports = ['websocket', 'polling', 'flashsocket'] , namespaces=['/HomeAutomationServer'])
            succes = True
        except Exception as e:
            succes = False

        return succes


    def run(self):
        listenHomeAutomationServer = threading.Thread(target=self.listen_home_automation_server)
        listenHomeAutomationServer.start()

        #listenClient = threading.Thread(target=self.listen_clients)
        #listenClient.start()

        while self.running:
            time.sleep(0.1)

        listenHomeAutomationServer.join()
        #listenClient.join()

    
    ###SYSTEM METHODS###
    def check_home_automation_server_connection(self):
        succes = False

        try:
            homeAutomationServerSocket.send('test')
            succes = True
        except:
            succes = False


    ###CLIENTS REQUEST###
    """CONNECTION EVENT"""
    @homeAutomationServerSocket.event(namespace='/HomeAutomationServer')
    def connect():
        print('connecté au serveur ')


    @homeAutomationServerSocket.event(namespace='/HomeAutomationServer')
    def light_controller_color_updated(data):
        print("yesssssssssssssssssss")