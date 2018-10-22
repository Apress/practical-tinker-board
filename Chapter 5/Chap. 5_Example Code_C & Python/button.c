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

