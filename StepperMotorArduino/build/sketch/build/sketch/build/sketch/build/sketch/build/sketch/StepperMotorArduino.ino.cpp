#include <Arduino.h>
#line 1 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino"
#line 1 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino"
#include <AccelStepper.h>

#define EXPECTED_INPUT_LENGTH 4
#define HALFSTEP 8
#define ONE_REVOLUTION 4096
#define MAX_SPEED 1024
#define ACCELERATION 1024

// Motor pin definitions
#define STEPPER_MOTOR1_PIN1 3 // IN1 on the ULN2003 driver 1
#define STEPPER_MOTOR1_PIN2 4 // IN2 on the ULN2003 driver 1
#define STEPPER_MOTOR1_PIN3 5 // IN3 on the ULN2003 driver 1
#define STEPPER_MOTOR1_PIN4 6 // IN4 on the ULN2003 driver 1

// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48 Stepper Motor
AccelStepper stepper1(HALFSTEP, STEPPER_MOTOR1_PIN1, STEPPER_MOTOR1_PIN3, STEPPER_MOTOR1_PIN2, STEPPER_MOTOR1_PIN4);

char buffer;
int index = 0;
int serialInt[EXPECTED_INPUT_LENGTH + 1];
String input;

// Only run once at the begining
void setup()
{
    // Initialize serial communcation with 57600 baud rate
    Serial.begin(57600);

    // Stepper1 Testing
    stepper1.setMaxSpeed(MAX_SPEED);
    stepper1.setAcceleration(ACCELERATION);
}

// Continuously running until power off
void loop()
{
    // Stepper run a step
    stepper1.run();
}

// Old version using Serial.readStringUntil
// Deprecated: This method halts the Arduino board physically until buffer read process finished, which is not ideal.

// void serialEvent()
// {
//     // Serial buffer have something
//     while (Serial.available())
//     {
//         // Read the buffer until "\n", basically doing readline
//         input = Serial.readStringUntil('\n');

//         // In case if the input is NOT the same length as expected, ignore it
//         if (input.length() == EXPECTED_INPUT_LENGTH)
//         {
//             stepper1.moveTo(input.toInt());
//         }
//     }
// }

// This method is run once every loop() time
void serialEvent()
{
    while (Serial.available())
    {
        buffer = Serial.read();
        if (isDigit(buffer))
        {
            // Convert from ASCII to int and put it into the array
            serialInt[index] = buffer - 48;
            index++;
            if (index == EXPECTED_INPUT_LENGTH)
            {
                index = 0;
                // servoAngle_0 = serialInt[0] * 100 + serialInt[1] * 10 + serialInt[2];
                // servoSpeed_0 = serialInt[3] * 100 + serialInt[4] * 10 + serialInt[5];
                // servoAngle_1 = serialInt[6] * 100 + serialInt[7] * 10 + serialInt[8];
                // servoSpeed_1 = serialInt[9] * 100 + serialInt[10] * 10 + serialInt[11];

                stepper1.moveTo(serialInt[0] * 1000 + serialInt[1] * 100 + serialInt[2] * 10 + serialInt[3]);
            }
        }
        else
        {
            index = 0;
        }
    }
}

