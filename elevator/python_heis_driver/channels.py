"""Equal to the defines in C.
Creates groups of sensors as well.

"""
class INPUT:
    PORT4          = 3
    OBSTRUCTION    = 0x300+23
    STOP           = 0x300+22
    FLOOR_COMMAND1 = 0x300+21
    FLOOR_COMMAND2 = 0x300+20
    FLOOR_COMMAND3 = 0x300+19
    FLOOR_COMMAND4 = 0x300+18
    FLOOR_UP1      = 0x300+17
    FLOOR_UP2      = 0x300+16

    PORT1          = 2
    FLOOR_DOWN2    = 0x200+0
    FLOOR_UP3      = 0x200+1
    FLOOR_DOWN3    = 0x200+2
    FLOOR_DOWN4    = 0x200+3
    SENSOR1        = 0x200+4
    SENSOR2        = 0x200+5
    SENSOR3        = 0x200+6
    SENSOR4        = 0x200+7
    
    IN_BUTTONS = [FLOOR_COMMAND1, FLOOR_COMMAND2, FLOOR_COMMAND3, FLOOR_COMMAND4]
    UP_BUTTONS = [FLOOR_UP1, FLOOR_UP2, FLOOR_UP3]
    DOWN_BUTTONS = [FLOOR_DOWN2, FLOOR_DOWN3, FLOOR_DOWN4]

    BUTTONS = IN_BUTTONS + UP_BUTTONS + DOWN_BUTTONS + [STOP]

    SENSORS = [SENSOR1, SENSOR2, SENSOR3, SENSOR4]

    ALL = BUTTONS + SENSORS + [OBSTRUCTION]

    NUM_FLOORS = len(SENSORS)

class OUTPUT:
    PORT3          = 3
    MOTORDIR       = 0X300+15
    LIGHT_STOP     = 0X300+14
    LIGHT_COMMAND1 = 0X300+13
    LIGHT_COMMAND2 = 0X300+12
    LIGHT_COMMAND3 = 0X300+11
    LIGHT_COMMAND4 = 0X300+10
    LIGHT_UP1      = 0X300+9
    LIGHT_UP2      = 0X300+8

    PORT2          = 3
    LIGHT_DOWN2    = 0X300+7
    LIGHT_UP3      = 0X300+6
    LIGHT_DOWN3    = 0X300+5
    LIGHT_DOWN4    = 0X300+4
    DOOR_OPEN      = 0X300+3
    FLOOR_IND1     = 0X300+1
    FLOOR_IND2     = 0X300+0

    PORT0          = 1
    MOTOR          = 0x100+0

    MOTOR_UP       = 0
    MOTOR_DOWN     = 1

    UP_LIGHTS = [LIGHT_UP1, LIGHT_UP2, LIGHT_UP3]
    DOWN_LIGHTS = [LIGHT_DOWN2, LIGHT_DOWN3, LIGHT_DOWN4]
    IN_LIGHTS = [LIGHT_COMMAND1, LIGHT_COMMAND2, LIGHT_COMMAND3, LIGHT_COMMAND4]
    FLOOR_LIGHTS = [FLOOR_IND1, FLOOR_IND2]
    LIGHTS = UP_LIGHTS + DOWN_LIGHTS + IN_LIGHTS + FLOOR_LIGHTS + [DOOR_OPEN]

    ALL = LIGHTS + [MOTOR, MOTORDIR]