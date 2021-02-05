from pynput.mouse import Listener

coordX = []
coordY=  []

xDIR = 0
yDIR = 0

def on_move(x, y):
    coordX.append(x)
    coordY.append(y)
    calculate()

def calculate():
    if len(coordX) == 2 or len(coordY) == 2  :
        
        xDIR = coordX[0]-coordX[1]
        coordX.clear()

        yDIR = coordY[0]-coordY[1]
        coordY.clear()

        if xDIR > 0:
            print("left")
        if xDIR < 0:
            print("right")
        if yDIR > 0:
            print("up")
        if yDIR < 0 :
            print("down")

        
with Listener(
        on_move=on_move) as listener:
    listener.join()
