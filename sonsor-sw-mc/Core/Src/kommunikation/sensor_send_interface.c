/*
 * sensor_send_interface.c
 *
 *  Created on: Nov 8, 2023
 *      Author: Daniel Alf
 */


#include <kommunikation/sensor_send_interface.h>
#include <stdio.h>
#include <string.h>


// Implementierung der Interface methoden
void sendDiameter_impl(UART_HandleTypeDef *huart,float value) {
	uint8_t tag[] = "diam ";
	uint8_t diameter[10];
	uint8_t endTag[] = "/r/n";

	sprintf((char *)diameter, "%.2f", value);

	HAL_UART_Transmit(huart, tag, 5, 10);
   	HAL_UART_Transmit(huart, diameter, strlen((char*)diameter), 10);
	HAL_UART_Transmit(huart, endTag, 4, 10);
}

void sendFrequency_impl(UART_HandleTypeDef *huart, float frequency) {
	uint8_t tag[] = "freq ";
	uint8_t freq[10];
	uint8_t endTag[] = "/r/n";

	sprintf((char *)freq, "%.0f", frequency);

	HAL_UART_Transmit(huart, tag, 5, 10);
   	HAL_UART_Transmit(huart, freq, strlen((char *)freq), 10);
	HAL_UART_Transmit(huart, endTag, 4, 10);
}

void sendCurve_impl(UART_HandleTypeDef *huart, const float curve[5]) {
	uint8_t tag[] = "curve ";
	uint8_t cur[10];
	uint8_t endTag[] = "/r/n";
	HAL_UART_Transmit(huart, " ", 1, 10);
	HAL_UART_Transmit(huart, tag, 5, 10);
	for(int i = 0; i < 5; i++){
		sprintf((char *)cur, "%.2f", curve[i]);
		HAL_UART_Transmit(huart, cur, strlen((char*)cur), 10);
		HAL_UART_Transmit(huart, " ", 1, 10);
	}
	HAL_UART_Transmit(huart, endTag, 4, 10);
}
void sendSN_impl(UART_HandleTypeDef *huart, int id) {
    uint8_t tag[] = "sn ";
    uint8_t id_str[10];
    uint8_t endTag[] = "\r\n";

    sprintf((char*)id_str, "%d", id);

    HAL_UART_Transmit(huart, tag, strlen((char*)tag), 10);
    HAL_UART_Transmit(huart, id_str, strlen((char*)id_str), 10);
    HAL_UART_Transmit(huart, endTag, strlen((char*)endTag), 10);
}
void sendType_impl(UART_HandleTypeDef *huart, const char* type) {
    uint8_t tag[] = "type ";
    uint8_t endTag[] = "\r\n";
    uint8_t hw[] = " hw1.0.0";
    uint8_t sw[] = " sw1.0.0";

    HAL_UART_Transmit(huart, tag, 5, 10);
    HAL_UART_Transmit(huart, (uint8_t*)type, (uint16_t)strlen(type), 10);  // Explizite Konvertierung
    HAL_UART_Transmit(huart, hw, strlen((char*)hw), 10);
    HAL_UART_Transmit(huart, sw, strlen((char*)sw), 10);
    HAL_UART_Transmit(huart, endTag, 4, 10);
}



SensorSendHandler createSendHandler(uint32_t timeout) {
    SensorSendHandler handler;
    handler.interface.sendDiameter = sendDiameter_impl;
    handler.interface.sendFrequency = sendFrequency_impl;
    handler.interface.sendCurve = sendCurve_impl;
    handler.interface.sendType = sendType_impl;
    handler.interface.sendSN = sendSN_impl;
    handler.interface.timeout = timeout;
    return handler;
}
