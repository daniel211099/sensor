/*
 * sensor_send_interface.h
 *
 *  Created on: Nov 8, 2023
 *      Author: Daniel Alf
 */


#ifndef INC_SENSOR_SEND_INTERFACE_H_
#define INC_SENSOR_SEND_INTERFACE_H_
#include "stm32f4xx_hal.h"
//#include "stm32f3xx_hal.h"

typedef struct {
    void (*sendDiameter)(UART_HandleTypeDef *huart, float diameter);
    void (*sendFrequency)(UART_HandleTypeDef *huart, float frequency);
    void (*sendCurve)(UART_HandleTypeDef *huart, const float curve[5]);
    void (*sendType)(UART_HandleTypeDef *huart, const char* type);
    void (*sendSN)(UART_HandleTypeDef *huart, int id);
    uint32_t timeout;
} SensorSendInterface;

typedef struct {
    SensorSendInterface interface;
    // Weitere interne Daten oder Konfigurationen, die benötigt werden
} SensorSendHandler;

SensorSendHandler createSendHandler();

#endif /* INC_SENSOR_SEND_INTERFACE_H_ */
