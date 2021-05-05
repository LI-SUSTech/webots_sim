from controller import Robot,Keyboard
 
def main():
  
    robot = Robot()
    

    timestep = int(robot.getBasicTimeStep())
    

    keyboard = Keyboard()
    keyboard.enable(10*timestep )
    
    radar=robot.getDevice('LDS-01')
    radar.enable(timestep)
    

    wheel1 = robot.getDevice('wheel_1')
    wheel2 = robot.getMotor('wheel_2')
    wheel3 = robot.getMotor('wheel_3')
    wheel4 = robot.getMotor('wheel_4')
    

    camera = robot.getCamera('kinect color')
    cameraRange = robot.getRangeFinder('kinect range')
    camera.enable(4*timestep)
    cameraRange.enable(4*timestep)
    

    wheel1.setPosition(float('inf'))
    wheel2.setPosition(float('inf'))
    wheel3.setPosition(float('inf'))
    wheel4.setPosition(float('inf'))
    
    wheel1.setVelocity(0)
    wheel2.setVelocity(0)
    wheel3.setVelocity(0)
    wheel4.setVelocity(0)
    
    R_ = 0.1  
    S_ = 0.4  
    L_ = 0.41 
   
    while robot.step(timestep) != -1:
       
        v1 = wheel1.getVelocity() * R_
        v2 = wheel2.getVelocity() * R_
        vel = (v1+v2)/2
        
       
        temp_ = L_ * L_ + S_ * S_
        omega = (v2 - v1) * L_ / temp_
        print("v = " + str(vel) + ", omega = " + str(omega))
    
      
        key = keyboard.getKey()
        if key == ord('Q'):
            wheel1.setVelocity(1)
            wheel2.setVelocity(3)
            wheel3.setVelocity(3)
            wheel4.setVelocity(1)
        elif key == ord('E'):
            wheel1.setVelocity(3)
            wheel2.setVelocity(1)
            wheel3.setVelocity(1)
            wheel4.setVelocity(3)
        elif key == Keyboard.UP:
            wheel1.setVelocity(2)
            wheel2.setVelocity(2)
            wheel3.setVelocity(2)
            wheel4.setVelocity(2)
        elif key == Keyboard.DOWN:
            wheel1.setVelocity(-2)
            wheel2.setVelocity(-2)
            wheel3.setVelocity(-2)
            wheel4.setVelocity(-2)
        elif key == Keyboard.LEFT:
            wheel1.setVelocity(-2)
            wheel2.setVelocity(2)
            wheel3.setVelocity(2)
            wheel4.setVelocity(-2)
        elif key == Keyboard.RIGHT:
            wheel1.setVelocity(2)
            wheel2.setVelocity(-2)
            wheel3.setVelocity(-2)
            wheel4.setVelocity(2)
        else:
            wheel1.setVelocity(0)
            wheel2.setVelocity(0)
            wheel3.setVelocity(0)
            wheel4.setVelocity(0)
        
main()