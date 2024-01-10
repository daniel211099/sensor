/*
 * uart_data.h
 *
 *  Created on: Nov 29, 2023
 *      Author: danie
 */

#ifndef INC_DATA_UART_DATA_H_
#define INC_DATA_UART_DATA_H_

#include <stdint.h>

typedef struct {
    uint8_t receivedData[64];
    int dataIndex;
    int messageComplete;
} UartData;

typedef struct {
    UartData data;

    // Getter-Methoden
    const uint8_t* (*getReceivedData)(const UartData* uartData);
    int (*getDataIndex)(const UartData* uartData);
    int (*getMessageComplete)(const UartData* uartData);

    // Setter-Methoden
    void (*setReceivedData)(UartData* uartData, const uint8_t* receivedData);
    void (*setDataIndex)(UartData* uartData, int dataIndex);
    void (*setMessageComplete)(UartData* uartData, int messageComplete);
} UartDataObject;

// Konstruktor
UartDataObject createUartDataObject();
#endif /* INC_DATA_UART_DATA_H_ */
