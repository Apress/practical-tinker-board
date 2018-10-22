#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include <wiringPi.h>
#include <softPwm.h>

int main (void)
{
  int LED = 0;
  int i;

  wiringPiSetup();

  pinMode (LED, PWM_OUTPUT) ;
  softPwmCreate (LED, 0, 100);

  while(1)
  {
    for (i = 0 ; i < 100 ; i++)
    {
      softPwmWrite (LED, i) ;
      delay (10) ;
    }

    for (i = 100 ; i >= 0 ; i--)
    {
      softPwmWrite (LED, i) ;
      delay (10) ;
    }
  }

  return 0 ;
}
