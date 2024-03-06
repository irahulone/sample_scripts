# requires PyRoboteq library
# https://github.com/Miker2808/PyRoboteq

from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
controller = RoboteqHandler(debug_mode = False, exit_on_interrupt = False) 
is_connected = controller.connect("/dev/ttyACM0")

def get_abs_encoders(ch):
    val = [0, 0]
    data = controller.read_value(cmds.READ_ABSCNTR,1)   # ch 1 
    if data.startswith('C='):
        x = data.split('=')
        val[0] = int(x[1])

    data = controller.read_value(cmds.READ_ABSCNTR,2)   # ch 2
    if data.startswith('C='):
        x = data.split('=')
        val[1] = int(x[1])
    
    if (ch == 1):
        return val[0]
    elif (ch == 2):
        return val[1]


def get_busV():
    val = 0
    data = controller.read_value(cmds.READ_VOLTS,2)   # ch 1 
    if data.startswith('V='):
        x = data.split('=')
        val = int(x[1])/10.0
    return val  # volts


def cmd_motors(m1, m2):
    controller.dual_motor_control(m1, m2) 


if __name__ == "__main__":
    while True:

        cmd_motors(1,0)

        #print(get_abs_encoders(1))

        print(get_busV())
    