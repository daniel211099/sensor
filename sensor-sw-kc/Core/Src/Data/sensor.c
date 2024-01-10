/*
 * sensor.c
 *
 *  Created on: Nov 29, 2023
 *      Author: Daniel Alf
 */


#include "Data/sensor.h"
#include <stdlib.h>

// Getter-Methoden
float getDiameter(const Sensor* sensor) {
    return sensor->info.diameter;
}

float getFrequency(const Sensor* sensor) {
    return sensor->info.frequency;
}

const float* getCurve(const Sensor* sensor) {
    return sensor->info.curve;
}

int getID(const Sensor* sensor) {
    return sensor->info.id;
}

const char* getType(const Sensor* sensor) {
    return sensor->info.type;
}

// Setter-Methoden
void setDiameter(Sensor* sensor, float diameter) {
    sensor->info.diameter = diameter;
}

void setFrequency(Sensor* sensor, float frequency) {
    sensor->info.frequency = frequency;
}

void setCurve(Sensor* sensor,const float curve[5]) {
	for(int i = 0; i < 5; i++){
	    sensor->info.curve[i] = curve[i];
	}
}

void setID(Sensor* sensor, int id) {
    sensor->info.id = id;
}

void setType(Sensor* sensor, const char* type) {
    sensor->info.type = type;
}

// Konstruktor
Sensor initSensor(float diameter, float frequency,const float curve[5], int id, const char* type) {
    Sensor sensor;
    sensor.info.diameter = diameter;
    sensor.info.frequency = frequency;
    for(int i = 0; i < 5; i++){
    	sensor.info.curve[i] = curve[i];
    }
    sensor.info.id = id;
    sensor.info.type = type;

    // Initialisiere die Getter-Funktionen
    sensor.getDiameter = getDiameter;
    sensor.getFrequency = getFrequency;
    sensor.getCurve = getCurve;
    sensor.getID = getID;
    sensor.getType = getType;

    // Initialisiere die Setter-Funktionen
    sensor.setDiameter = setDiameter;
    sensor.setFrequency = setFrequency;
    sensor.setCurve = setCurve;
    sensor.setID = setID;
    sensor.setType = setType;

    return sensor;
}
