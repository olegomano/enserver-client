import zmq
import time
from components.message import enginecmd_pb2 as pb 

class DebugCommander:
    def __init__(self,ip):
        print("Creating DebugCommander " + str(ip))
        self.ip = ip
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ) 
       

    def connect(self):
        print(self.socket.connect(self.ip+":5556"))
    
    def getVersion(self):
        command = pb.DebugCommand()
        command.Command = "version"       
        print("Sending Command")
        self.socket.send(command.SerializeToString())
        print("Waiing for Result")
        result = self.socket.recv()
        return result 
