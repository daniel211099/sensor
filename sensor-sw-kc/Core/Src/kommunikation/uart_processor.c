/*
 * uart_processor.c
 *
 *  Created on: Nov 27, 2023
 *      Author: Daniel Alf
 */

#include <kommunikation/uart_processor.h>
#include <stdio.h>
#include <string.h>



// Funktion zur Initialisierung des UART-Prozessors
UartProcessor createUartProcessor(CommandEntry* dictionary) {
    UartProcessor uartProcessor;
    uartProcessor.commandDictionary = dictionary;
    return uartProcessor;
}

// Case-insensitive String-Vergleich
int strnicmp(const char *s1, const char *s2, size_t n) {
    while (*s1 && *s2 && n > 0) {
        if (tolower(*s1) != tolower(*s2))
            return -1;
        s1++;
        s2++;
        n--;
    }
    return 0;
}

void processCommand(UartProcessor* uartProcessor,uint8_t* receivedData,uint8_t receivedDataIndex) {
    for (int i = 0; uartProcessor->commandDictionary[i].command != NULL; ++i) {
    	if (strnicmp((char*)receivedData, uartProcessor->commandDictionary[i].command, strlen(uartProcessor->commandDictionary[i].command)) == 0) {
            // Rufe den entsprechenden Handler auf
    		uartProcessor->commandDictionary[i].functionPointer((char*)receivedData);
            return;
        }
    }
}
