/*
 * button.c:
 *	Test of a push button with an LED
 *	
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

#include <stdio.h>
#include <wiringPi.h>

#define	LED	0
#define BUTTON 2

int main (void)
{
	wiringPiSetup();

	pinMode(LED, OUTPUT); 
	pinMode(BUTTON, INPUT);

	while(1) {
		
		if (digitalRead(BUTTON) == 0) {
			digitalWrite(LED, HIGH) ;
		} 
		
		else {
			digitalWrite(LED, LOW);
		}
	}
	return 0;
}

