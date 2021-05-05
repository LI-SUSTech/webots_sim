from controller import Robot

TIME_STEP = 64
robot = Robot()


wheels = []
wheelsNames = ['wheel_1', 'wheel_2']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(1.0)


while robot.step(TIME_STEP) != -1:
    pass