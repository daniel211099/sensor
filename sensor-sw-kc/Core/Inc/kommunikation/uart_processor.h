/*
 * uart_processor.h
 *
 *  Created on: Nov 27, 2023
 *      Author: Daniel Alf
 */

#ifndef INC_UART_PROCESSOR_H_
#define INC_UART_PROCESSOR_H_

#include <stdint.h>

// Definition der Befehlseintrag-Struktur
typedef struct {
    const char* command;
    void (*functionPointer)(const char* value);
} CommandEntry;

// Definition des UartProcessor-Typs
typedef struct {
    CommandEntry* commandDictionary;
} UartProcessor;

// Funktion zur Initialisierung des UART-Prozessors
UartProcessor createUartProcessor(CommandEntry* dictionary);

// Funktion zur Ausführung eines Commands mit dem UART-Prozessor
void processCommand(UartProcessor* uartProcessor,uint8_t* receivedData, uint8_t receivedDataIndex);

#endif /* INC_UART_PROCESSOR_H_ */
