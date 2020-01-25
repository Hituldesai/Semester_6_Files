/*
 * TITLE:
 * DATE:
 * AUTHOR:
 */ 


#define F_CPU 16000000

#include <avr/io.h>
#include <util/delay.h>

#include "glcd.h"	//User defined LCD library which contains the lcd routine s
// #include "glcd.c"

int main(void)
{
	GLCD_Init();
	GLCD_DisplayString("CS684 - 2020");
    while(1);
}