include <webots/robot.h>
#include <webots/motor.h>
#include <webots/keyboard.h>
#include <stdio.h>

#define TIME_STEP 64

int main(int argc, char **argv) {
  wb_robot_init();
  wb_keyboard_enable(TIME_STEP);
  printf("Able\n");

     WbDeviceTag motors[2];
  char motors_names[2][4] = {"motor_1", "motor_2"};
  for (int i = 0; i < 2; i++) {
    motors[i] = wb_robot_get_device(motors_names[i]);
    wb_motor_set_position(motors[i], INFINITY);
    wb_motor_set_velocity(motors[i],0);
  }

  double left_speed = 1.0;
  double right_speed = 1.0;
  
  while (wb_robot_step(TIME_STEP) != -1) {

    int new_key = wb_keyboard_get_key();

    while (new_key > 0) {
      printf("%d\n",new_key);
      switch (new_key) {
      case 87://w
       printf("UP pressed\n");
       if(right_speed<0)left_speed = -right_speed;
       else left_speed = right_speed;
       left_speed += 1.0;
       right_speed += 1.0;
        break;

      case 83://s
        printf("DOWN pressed\n");
        if(right_speed>0)left_speed = -right_speed;
        else left_speed = right_speed;
        left_speed -= 1.0;
        right_speed -= 1.0;
        break;

      case 65://a
        printf("LEFT pressed\n");
        left_speed -= 0.5;
        right_speed += 0.5;
        break;

      case 68://d
        printf("RIGHT pressed\n");
        left_speed += 0.5;
        right_speed -= 0.5;
        break;
        
      case 69://e
        printf("RIGHT—UP pressed\n");
        left_speed += 1;
        right_speed = 1;
        break;
        
      case 81://q
        printf("LEFT—UP pressed\n");
        left_speed = 1;
        right_speed += 1;
        break;
        
      case 90://z
        printf("LEFT—DOWN pressed\n");
        left_speed = -1;
        right_speed -= 1;
        break;
        
      case 67://c
        printf("RIGHT—DOWN pressed\n");
        left_speed -= 1;
        right_speed = -1;
        break;

      case 70://f
        printf("A pressed\n");
        wb_keyboard_disable();
        break;
      }
      new_key = wb_keyboard_get_key();
      
     }
     
    if(left_speed>5)left_speed=5;
    else if(left_speed<-5)left_speed=-5;
    if(right_speed>5)right_speed=5;
    else if(right_speed<-5)right_speed=-5;
    
    wb_motor_set_velocity(motors[0],left_speed);
    wb_motor_set_velocity(motors[1],right_speed);
   
    }

  wb_robot_cleanup();

  return 0;
}
