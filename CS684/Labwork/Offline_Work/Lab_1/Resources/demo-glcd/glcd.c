#include <stdarg.h>
#include <avr/pgmspace.h>
#include "glcd.h"
#include "delay.h"


GLCD_Config GLCD;



const uint8_t ARR_GlcdFont_U8[][7] PROGMEM= {
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff}, /* 0x00  */
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff}, /* 0x10  */
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
		{0xff,0xff,0xff,0xff,0xff,0x00,0xff},
        {0x00,0x00,0x00,0x00,0x00,0xff,0xff}, /* Space 0x20 */
        {0x00,0x00,0x4f,0x00,0x00,0x00,0xff}, /* ! */
        {0x00,0x07,0x00,0x07,0x00,0x00,0xff}, /* " */
        {0x14,0x7f,0x14,0x7f,0x14,0x00,0xff}, /* # */
        {0x24,0x2a,0x7f,0x2a,0x12,0x00,0xff}, /* 0x */
        {0x23,0x13,0x08,0x64,0x62,0x00,0xff}, /* % */
        {0x36,0x49,0x55,0x22,0x20,0x00,0xff}, /* & */
        {0x00,0x05,0x03,0x00,0x00,0x00,0xff}, /* ' */
        {0x00,0x1c,0x22,0x41,0x00,0x00,0xff}, /* ( */
        {0x00,0x41,0x22,0x1c,0x00,0x00,0xff}, /* ) */
        {0x14,0x08,0x3e,0x08,0x14,0x00,0xff}, /* // */
        {0x08,0x08,0x3e,0x08,0x08,0x00,0xff}, /* + */
        {0x50,0x30,0x00,0x00,0x00,0x00,0xff}, /* , */
        {0x08,0x08,0x08,0x08,0x08,0x00,0xff}, /* - */
        {0x00,0x60,0x60,0x00,0x00,0x00,0xff}, /* . */
        {0x20,0x10,0x08,0x04,0x02,0x00,0xff}, /* / */
        {0x3e,0x51,0x49,0x45,0x3e,0x00,0xff}, /* 0 0x30 */
        {0x40,0x42,0x7f,0x40,0x40,0x00,0xff}, /* 1 */
        {0x42,0x61,0x51,0x49,0x46,0x00,0xff}, /* 2 */
        {0x21,0x41,0x45,0x4b,0x31,0x00,0xff}, /* 3 */
        {0x18,0x14,0x12,0x7f,0x10,0x00,0xff}, /* 4 */
        {0x27,0x45,0x45,0x45,0x39,0x00,0xff}, /* 5 */
        {0x3c,0x4a,0x49,0x49,0x30,0x00,0xff}, /* 6 */
        {0x01,0x71,0x09,0x05,0x03,0x00,0xff}, /* 7 */
        {0x36,0x49,0x49,0x49,0x36,0x00,0xff}, /* 8 */
        {0x06,0x49,0x49,0x29,0x1e,0x00,0xff}, /* 9 */
        {0x00,0x36,0x36,0x00,0x00,0x00,0xff}, /* : */
        {0x00,0x56,0x36,0x00,0x00,0x00,0xff}, /* ; */
        {0x08,0x14,0x22,0x41,0x00,0x00,0xff}, /* < */
        {0x14,0x14,0x14,0x14,0x14,0x00,0xff}, /* = */
        {0x00,0x41,0x22,0x14,0x08,0x00,0xff}, /* > */
        {0x02,0x01,0x51,0x09,0x06,0x00,0xff}, /* ? */
        {0x3e,0x41,0x5d,0x55,0x1e,0x00,0xff}, /* @ 0x40 */
        {0x7e,0x11,0x11,0x11,0x7e,0x00,0xff}, /* A */
        {0x7f,0x49,0x49,0x49,0x36,0x00,0xff}, /* B */
        {0x3e,0x41,0x41,0x41,0x22,0x00,0xff}, /* C */
        {0x7f,0x41,0x41,0x22,0x1c,0x00,0xff}, /* D */
        {0x7f,0x49,0x49,0x49,0x41,0x00,0xff}, /* E */
        {0x7f,0x09,0x09,0x09,0x01,0x00,0xff}, /* F */
        {0x3e,0x41,0x49,0x49,0x7a,0x00,0xff}, /* G */
        {0x7f,0x08,0x08,0x08,0x7f,0x00,0xff}, /* H */
        {0x00,0x41,0x7f,0x41,0x00,0x00,0xff}, /* I */
        {0x20,0x40,0x41,0x3f,0x01,0x00,0xff}, /* J */
        {0x7f,0x08,0x14,0x22,0x41,0x00,0xff}, /* K */
        {0x7f,0x40,0x40,0x40,0x40,0x00,0xff}, /* L */
        {0x7f,0x02,0x0c,0x02,0x7f,0x00,0xff}, /* M */
        {0x7f,0x04,0x08,0x10,0x7f,0x00,0xff}, /* N */
        {0x3e,0x41,0x41,0x41,0x3e,0x00,0xff}, /* O */
        {0x7f,0x09,0x09,0x09,0x06,0x00,0xff}, /* P 0x50 */
        {0x3e,0x41,0x51,0x21,0x5e,0x00,0xff}, /* Q */
        {0x7f,0x09,0x19,0x29,0x46,0x00,0xff}, /* R */
        {0x26,0x49,0x49,0x49,0x32,0x00,0xff}, /* S */
        {0x01,0x01,0x7f,0x01,0x01,0x00,0xff}, /* T */
        {0x3f,0x40,0x40,0x40,0x3f,0x00,0xff}, /* U */
        {0x1f,0x20,0x40,0x20,0x1f,0x00,0xff}, /* V */
        {0x3f,0x40,0x38,0x40,0x3f,0x00,0xff}, /* W */
        {0x63,0x14,0x08,0x14,0x63,0x00,0xff}, /* X */
        {0x07,0x08,0x70,0x08,0x07,0x00,0xff}, /* Y */
        {0x61,0x51,0x49,0x45,0x43,0x00,0xff}, /* Z */
        {0x00,0x7f,0x41,0x41,0x00,0x00,0xff}, /* [ */
        {0x02,0x04,0x08,0x10,0x20,0x00,0xff}, /* \ */
        {0x00,0x41,0x41,0x7f,0x00,0x00,0xff}, /* ] */
        {0x04,0x02,0x01,0x02,0x04,0x00,0xff}, /* ^ */
        {0x40,0x40,0x40,0x40,0x40,0x00,0xff}, /* _ */
        {0x00,0x00,0x03,0x05,0x00,0x00,0xff}, /* ` 0x60 */
        {0x20,0x54,0x54,0x54,0x78,0x00,0xff}, /* a */
        {0x7F,0x44,0x44,0x44,0x38,0x00,0xff}, /* b */
        {0x38,0x44,0x44,0x44,0x44,0x00,0xff}, /* c */
        {0x38,0x44,0x44,0x44,0x7f,0x00,0xff}, /* d */
        {0x38,0x54,0x54,0x54,0x18,0x00,0xff}, /* e */
        {0x04,0x04,0x7e,0x05,0x05,0x00,0xff}, /* f */
        {0x08,0x54,0x54,0x54,0x3c,0x00,0xff}, /* g */
        {0x7f,0x08,0x04,0x04,0x78,0x00,0xff}, /* h */
        {0x00,0x44,0x7d,0x40,0x00,0xff,0xff}, /* i */
        {0x20,0x40,0x44,0x3d,0x00,0xff,0xff}, /* j */
        {0x7f,0x10,0x28,0x44,0x00,0xff,0xff}, /* k */
        {0x41,0x7f,0x40,0x00,0xff,0xff,0xff}, /* l */
        {0x7c,0x04,0x7c,0x04,0x78,0x00,0xff}, /* m */
        {0x7c,0x08,0x04,0x04,0x78,0x00,0xff}, /* n */
        {0x38,0x44,0x44,0x44,0x38,0x00,0xff}, /* o */
        {0x7c,0x14,0x14,0x14,0x08,0x00,0xff}, /* p 0x70 */
        {0x08,0x14,0x14,0x14,0x7c,0x00,0xff}, /* q */
        {0x7c,0x08,0x04,0x04,0x00,0xff,0xff}, /* r */
        {0x48,0x54,0x54,0x54,0x24,0x00,0xff}, /* s */
        {0x04,0x04,0x3f,0x44,0x44,0x00,0xff}, /* t */
        {0x3c,0x40,0x40,0x20,0x7c,0x00,0xff}, /* u */
        {0x1c,0x20,0x40,0x20,0x1c,0x00,0xff}, /* v */
        {0x3c,0x40,0x30,0x40,0x3c,0x00,0xff}, /* w */
        {0x44,0x28,0x10,0x28,0x44,0x00,0xff}, /* x */
        {0x0c,0x50,0x50,0x50,0x3c,0x00,0xff}, /* y */
        {0x44,0x64,0x54,0x4c,0x44,0x00,0xff}, /* z */
        {0x08,0x36,0x41,0x41,0x00,0x00,0xff}, /* { */
        {0x00,0x00,0x77,0x00,0x00,0x00,0xff}, /* | */
        {0x00,0x41,0x41,0x36,0x08,0x00,0xff}, /* } */
        {0x08,0x08,0x2a,0x1c,0x08,0x00,0xff}, /* <- */
        {0x08,0x1c,0x2a,0x08,0x08,0x00,0xff}, /* -> */
        {0xff,0xff,0xff,0xff,0xff,0x00,0xff}, /*  0x80 */
};



/*************************************************************************************************
                                Local Functions
*************************************************************************************************/
static void glcd_CmdWrite( uint8_t var_lcdCmd_u8);
static void glcd_DataWrite( uint8_t var_data_u8);
static void glcd_BusyCheck();
static void glcd_SelectPage0();
static void glcd_SelectPage1();
/************************************************************************************************/
								


/**************************************************************************************************
void GLCD_Init
***************************************************************************************************
 * Function name:  GLCD_Init
 * I/P Arguments:  none
 * Return value    : none

 * description  :This function is used to initialize the GLCD.
                 
**************************************************************************************************/
void GLCD_Init()
{
	M_GlcdControlBusDirection = C_PortOutput_U8; /* Configure the data bus and Control bus as Output */
    M_GlcdDataBusDirection = C_PortOutput_U8;
	M_GlcdControlBusDirection1 = C_PortOutput_U8;


    /* Select the Page0/Page1 and Enable the GLCD */
    glcd_SelectPage0();
    glcd_CmdWrite(0x3F);
    glcd_SelectPage1();
    glcd_CmdWrite(0x3F);
    DELAY_ms(10);

    /* Select the Page0/Page1 and Enable the GLCD */
    glcd_SelectPage0();
    glcd_CmdWrite(0xc0);
    glcd_SelectPage1();
    glcd_CmdWrite(0xc0);

   /* Clear the complete LCD and move the cursor to beginning of page0*/
    GLCD_Clear();
}










/***************************************************************************************************
                         void GLCD_Clear()
 ***************************************************************************************************
 * I/P Arguments: none.
 * Return value    : none

 * description  :This function clears the LCD and moves the cursor to beginning of first line on page0
 ***************************************************************************************************/
void GLCD_Clear()
{
    uint8_t line,cursor,inversion;

    inversion = GLCD.Invertdisplay;
	GLCD.Invertdisplay = 0x00;
	
    for(line=0;line<8;line++)  /* loop through all the 8lines to clear the display */
    {
         GLCD_GoToLine(line);  /* Go to beginning of the specified line on page0 */
        
        for(cursor=0;cursor<128;cursor++) /* Clear all the 128 pixels of selected line */
        {
            if(cursor==64)  /* Has the cursor reached end of page0 */
            {
                GLCD_GoToPage(1); /*  then set it to beginning of page1 */
                
            }
            glcd_DataWrite(0x00); /* Clear each pixel by displaying blank */
        }
    }
	
	GLCD.Invertdisplay = inversion;

    GLCD_GoToLine(0);
}













/***************************************************************************************************
      void GLCD_SetCursor(uint8_t pageNumber,uint8_t lineNumber,uint8_t CursorPosition)
 ***************************************************************************************************
 * I/P Arguments: char row,char col
                 row -> line number(line1=1, line2=2),
                        For 2line LCD the I/P argument should be either 1 or 2.
                 col -> char number.
                        For 16-char LCD the I/P argument should be between 0-15.
 * Return value    : none

 * description  :This function moves the Cursor to specified position

                   Note:If the Input(Line/Char number) are out of range 
                        then no action will be taken
 ***************************************************************************************************/
 /* TODO: change the var names, Add logic for page handling */
void GLCD_SetCursor(uint8_t pageNumber,uint8_t lineNumber,uint8_t CursorPosition)
{
    if(    ((pageNumber == 0x00)   || (pageNumber == 0x01))
	    && ((lineNumber >=0x00)    && (lineNumber <= C_GlcdLastLine_U8))
	    && ((CursorPosition>=0x00) && (CursorPosition <= 63)) )
	  {
	    if(pageNumber==0x00)  /* Check for page number and set accordingly */
         {
           glcd_SelectPage0();
         }
        else
	     {
            glcd_SelectPage1();
	      }	 

        GLCD.PageNum = pageNumber; /* Keep the track of page selected */
        GLCD.LineNum=lineNumber | C_FirstLineNumberAddress_U8; /* Select the specified line number */
        GLCD.CursorPos=CursorPosition |0x40; /* Select the specified cursor position */
        glcd_CmdWrite(GLCD.CursorPos); /* Command the LCD to move to specified page,line,cursor*/
        glcd_CmdWrite(GLCD.LineNum);
	}
}







void GLCD_GetCursor(uint8_t *page_ptr,uint8_t *line_ptr,uint8_t *cursor_ptr)
{

    *page_ptr=GLCD.PageNum;
    *line_ptr=GLCD.LineNum;
    *cursor_ptr=GLCD.CursorPos;
}



/***************************************************************************************************
                      void GLCD_GoToPage(uint8_t pageNumber)
 ***************************************************************************************************
 * I/P Arguments: uint8_t: Line number.
 * Return value    : none

 * description  :This function moves the Cursor to beginning of the specified line.
        If the requested line number is out of range, it will not move the cursor.

     Note: The line numbers run from 1 to Maxlines,
 ***************************************************************************************************/
 /* TODO: change the desp and variable name */
void GLCD_GoToPage(uint8_t pageNumber)
{

    if((pageNumber==0) || (pageNumber ==1))
    { /* for 128/64 GLCD only page 0&1 are supported.
        Select the specified page and move the cursor accordingly */
        if(pageNumber == 0)
        {

            glcd_SelectPage0();
        }
        else
        {
            glcd_SelectPage1();
        }
        GLCD.PageNum=pageNumber;
        GLCD.CursorPos=0x40;
        glcd_CmdWrite(GLCD.LineNum);
        glcd_CmdWrite(GLCD.CursorPos);
    }
}







/***************************************************************************************************
                         void GLCD_GoToLine(uint8_t var_lineNumber_u8)
 ***************************************************************************************************
 * I/P Arguments: uint8_t: Line number.
 * Return value    : none

 * description  :This function moves the Cursor to beginning of the specified line.
        If the requested line number is out of range, it will not move the cursor.

     Note: The line numbers run from 0 to Maxlines-1, For 128x64 the line numbers will be 0-7
***************************************************************************************************/
/* Todo: All constants for the magic numbers */
void  GLCD_GoToLine(uint8_t var_lineNumber_u8)
{
    if(var_lineNumber_u8 <= C_GlcdLastLine_U8)
    {   /* If the line number is within range
         then move it to specified line on page0 and keep track*/
        GLCD.LineNum = var_lineNumber_u8+C_FirstLineNumberAddress_U8;
        GLCD_GoToPage(0);
    }
}





/***************************************************************************************************
                         void  GLCD_GoToNextLine()
 ***************************************************************************************************
 * I/P Arguments: none
 * Return value    : none

 * description  :This function moves the Cursor to beginning of the next line.
        If the cursor is on last line and NextLine command is issued then 
        it will move the cursor to first line.
 ***************************************************************************************************/
void  GLCD_GoToNextLine()
{
    /*Increment the current line number.
      In case it exceeds the limit, rool it back to first line */
    GLCD.LineNum++;
    if(GLCD.LineNum > C_LastLineNumberAddress_U8)
      GLCD.LineNum = C_FirstLineNumberAddress_U8;
    GLCD_GoToPage(0); /* Finally move it to next line on page0 */
}




void GLCD_EnableDisplayInversion()
{
	GLCD.Invertdisplay = 0xff;
}



void GLCD_DisableDisplayInversion()
{
	GLCD.Invertdisplay = 0x00;
}




/***************************************************************************************************
                       void GLCD_DisplayChar( char var_lcdData_u8)
 ***************************************************************************************************
 * I/P Arguments: ASCII value of the char to be displayed.
 * Return value    : none

 * description  : This function sends a character to be displayed on LCD.
                  Any valid ascii value can be passed to display respective character

 ***************************************************************************************************/
 /* Add the comments for decoding the character, Even offset handling*/
void GLCD_DisplayChar(uint8_t var_lcdData_u8)
{
    uint8_t dat;
	const uint8_t *ptr;

    if(((GLCD.PageNum == 0x01) && (GLCD.CursorPos>=0x7c)) || (var_lcdData_u8=='\n'))
    {
        /* If the cursor has reached to end of line on page1
        OR NewLine command is issued Then Move the cursor to next line */
        GLCD_GoToNextLine();
    }
       if(var_lcdData_u8!='\n') /* TODO */
    {
        ptr= &ARR_GlcdFont_U8[var_lcdData_u8][0]; /* Get the address of the Character pattern from LookUp */
        while(1)
        {
            if((GLCD.PageNum == 0x00) && (GLCD.CursorPos==0x80))
            {
                /* If the cursor has reached to end of line on page0
                     Then Move the cursor to Page1 */
                GLCD_GoToPage(1);
            }

            dat= pgm_read_byte(ptr++);/* Get the data to be displayed for LookUptable*/

            if(dat==0xff) /* Exit the loop if End of char is encountered */
                break;

            glcd_DataWrite(dat); /* Display the data and keep track of cursor */
            GLCD.CursorPos++;
        }
    }
}






/***************************************************************************************************
                       void GLCD_DisplayString(char *ptr_stringPointer_u8)
 ***************************************************************************************************
 * I/P Arguments: String(Address of the string) to be displayed.
 * Return value    : none

 * description  :
               This function is used to display the ASCII string on the lcd.
                 1.The ptr_stringPointer_u8 points to the first char of the string
                    and traverses till the end(NULL CHAR)and displays a char each time.

 ***************************************************************************************************/
#if (Enable_GLCD_DisplayString==1)
void GLCD_DisplayString(char *ptr_stringPointer_u8)
{
    while((*ptr_stringPointer_u8)!=0)
        GLCD_DisplayChar(*ptr_stringPointer_u8++); // Loop through the string and display char by char
}
#endif


/***************************************************************************************************
                       static void glcd_CmdWrite( uint8_t var_lcdCmd_u8)
 ***************************************************************************************************
 * I/P Arguments: 8-bit command supported by LCD.
 * Return value    : none

 * description :This function sends a command to GLCD.
                Some of the commonly used commands are defined in lcd.h.
                For more commands refer the data sheet and send the supported command.                
                The behavior is undefined if unsupported commands are sent.    
 ***************************************************************************************************/
static void glcd_CmdWrite( uint8_t var_cmd_u8)
{
    glcd_BusyCheck();
    M_GlcdDataBus = var_cmd_u8;
    M_GlcdClearBit(M_GlcdControlBus,GLCD_RS);           // Select the Command Register by pulling RS LOW
#ifdef GLCD_RW
    M_GlcdClearBit(M_GlcdControlBus,GLCD_RW);           // Select the Write Operation  by pulling RW LOW
#endif
    M_GlcdSetBit(M_GlcdControlBus,GLCD_EN);             // Send a High-to-Low Pulse at Enable Pin
    DELAY_us(2);
    M_GlcdClearBit(M_GlcdControlBus,GLCD_EN);
}






/*************************************************************************************************
                       static void glcd_DataWrite( uint8_t dat)
 *************************************************************************************************
 * I/P Arguments: uint8_t: 8-bit value to be sent to LCD.
 * Return value    : none

 * description : This functions is used to send a byte of data to LCD.                 .    
 *************************************************************************************************/
static void glcd_DataWrite( uint8_t var_data_u8)
{
    glcd_BusyCheck();
    M_GlcdDataBus = var_data_u8 ;
    M_GlcdSetBit(M_GlcdControlBus,GLCD_RS);           // Select the Data Register by pulling RS High
#ifdef GLCD_RW
    M_GlcdClearBit(M_GlcdControlBus,GLCD_RW);           // Select the Write Operation  by pulling RW LOW
#endif
    M_GlcdSetBit(M_GlcdControlBus,GLCD_EN);             // Send a High-to-Low Pulse at Enable Pin
    DELAY_us(2);
    M_GlcdClearBit(M_GlcdControlBus,GLCD_EN);
}







/*************************************************************************************************
                       static void glcd_BusyCheck()
 *************************************************************************************************
 * I/P Arguments: none.
 * Return value    : none

 * description : This functions is used check whether LCD is busy.
                 It waits till the LCD is busy by polling the LCD busy flag.
                 After completing the previous operation, LCDs clears its internal busy flag.
 *************************************************************************************************/
static void glcd_BusyCheck()
{
    uint8_t busyflag;
    
#ifdef GLCD_RW                    //Perform Busy check if GLCD_RW pin is used

    util_UpdateBit(M_GlcdDataBusDirection,GLCD_D7,C_PinInput_U8); // Configure busy pin as input
    M_GlcdClearBit(M_GlcdControlBus,GLCD_RS);           // Select the Command Register by pulling RS LOW
    M_GlcdSetBit(M_GlcdControlBus,GLCD_RW);             // Select the Read Operation for busy flag by setting RW
    do
    {
        M_GlcdClearBit(M_GlcdControlBus,GLCD_EN);             // Send a High-to-Low Pulse at Enable Pin
        DELAY_us(2);    
        M_GlcdSetBit(M_GlcdControlBus,GLCD_EN);
        DELAY_us(2);
        busyflag = util_GetBitStatus(M_GlcdDataBusInput,GLCD_D7);
    }while(busyflag);

    util_UpdateBit(M_GlcdDataBusDirection,GLCD_D7,C_PinOutput_U8);
#else
    /* Busy flag cannot be read as GLCD_RW is not available hence Extra delay of 1ms is added 
      to ensure the LCD completes previous operation and ready to receive new commands/data */
    DELAY_ms(1);  
#endif
}


static void glcd_SelectPage0() 
 { 
   M_GlcdSetBit(M_GlcdControlBus1,GLCD_CS1); 
   M_GlcdClearBit(M_GlcdControlBus1,GLCD_CS2); 
 }

static void glcd_SelectPage1() 
 {
   M_GlcdSetBit(M_GlcdControlBus1,GLCD_CS2);  
   M_GlcdClearBit(M_GlcdControlBus1,GLCD_CS1); 
 }




