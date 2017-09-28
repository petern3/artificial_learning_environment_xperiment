
from robot_chassis import Chassis
from control_user import User
from control_ai import AI

USER_CONTROL = True



main_chassis = Chassis()

if USER_CONTROL is True:
    controller = User(main_chassis)
else:
    controller = AI(main_chassis)
    
controller.run()