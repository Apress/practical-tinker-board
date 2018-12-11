/*
 * softPwm.c:
 *	Test of the software PWM driver. Needs 8 LEDs connected
 *	to the Pi - e.g. Ladder board.
 *
 * Copyright (c) 2012-2013 Gordon Henderson. <projects@drogon.net>
 ***********************************************************************
 * This file is part of wiringPi:
 *	https://projects.drogon.net/raspberry-pi/wiringpi/
 *
 *    wiringPi is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU Lesser General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    wiringPi is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU Lesser General Public License for more details.
 *
 *    You should have received a copy of the GNU Lesser General Public License
 *    along with wiringPi.  If not, see <http://www.gnu.org/licenses/>.
 ***********************************************************************
 */

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
