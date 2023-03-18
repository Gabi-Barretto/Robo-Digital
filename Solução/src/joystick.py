import pydobot
from data.posicoes import Posicao
import serial
import serial.tools.list_ports



dobot = pydobot.Dobot(port="COM8", verbose=False).device

def coordenadas():
    
    (x0, y0, z0, r0, j10, j20, j30, j40) = dobot.pose() 

    dobot.wait(500)

    return x0, y0, z0

def move(x, y ,z):
    dobot.move_to(x, y, z, 0, wait=True)