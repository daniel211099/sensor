/*
 * sensor_information.h
 *
 *  Created on: Nov 29, 2023
 *      Author: Daniel Alf
 */

#ifndef INC_DATA_SENSOR_H_
#define INC_DATA_SENSOR_H_

typedef struct Sensor Sensor;  // Vorwärtsdeklaration

typedef struct {
    float diameter;
    float frequency;
    float curve[5];
    int id;
    const char* type;
} SensorInformation;

struct Sensor {
    SensorInformation info;

    // Getter-Methoden
    float (*getDiameter)(const Sensor* sensor);
    float (*getFrequency)(const Sensor* sensor);
    const float* (*getCurve)(const Sensor* sensor);
    int (*getID)(const Sensor* sensor);
    const char* (*getType)(const Sensor* sensor);

    // Setter-Methoden
    void (*setDiameter)(Sensor* sensor, float diameter);
    void (*setFrequency)(Sensor* sensor, float frequency);
    void (*setCurve)(Sensor* sensor, const float curve[]);
    void (*setID)(Sensor* sensor, int id);
    void (*setType)(Sensor* sensor, const char* type);
};

// Konstruktor
Sensor initSensor(float diameter, float frequency,const float curve[5], int id, const char* type);

#endif /* INC_DATA_SENSOR_H_ */
