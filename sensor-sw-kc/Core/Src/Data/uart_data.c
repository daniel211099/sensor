/*
 * uart_data.c
 *
 *  Created on: Nov 29, 2023
 *      Author: danie
 */


#include "Data/uart_data.h"

// Getter-Methoden
const uint8_t* getReceivedData(const UartData* uartData) {
    return uartData->receivedData;
}

int getDataIndex(const UartData* uartData) {
    return uartData->dataIndex;
}

int getMessageComplete(const UartData* uartData) {
    return uartData->messageComplete;
}

// Setter-Methoden
void setReceivedData(UartData* uartData, const uint8_t* receivedData) {
    // Kopiere die Daten
    for (int i = 0; i < 64; i++) {
        uartData->receivedData[i] = receivedData[i];
    }
}

void setDataIndex(UartData* uartData, int dataIndex) {
    uartData->dataIndex = dataIndex;
}

void setMessageComplete(UartData* uartData, int messageComplete) {
    uartData->messageComplete = messageComplete;
}

// Konstruktor
UartDataObject createUartDataObject() {
    UartDataObject uartDataObject;
    uartDataObject.getReceivedData = &getReceivedData;
    uartDataObject.getDataIndex = &getDataIndex;
    uartDataObject.getMessageComplete = &getMessageComplete;
    uartDataObject.setReceivedData = &setReceivedData;
    uartDataObject.setDataIndex = &setDataIndex;
    uartDataObject.setMessageComplete = &setMessageComplete;

    // Initialisiere die Daten
    for (int i = 0; i < 64; i++) {
        uartDataObject.data.receivedData[i] = 0;
    }
    uartDataObject.data.dataIndex = 0;
    uartDataObject.data.messageComplete = 0;

    return uartDataObject;
}
