#include <AccelStepper.h>

#define EXPECTED_INPUT_LENGTH 9
#define HALFSTEP 8
#define ONE_REVOLUTION 4096
#define MAX_SPEED 2048
#define ACCELERATION 1024

// Motor pin definitions (Stepper motor 1)(X-Axis))
#define STEPPER_MOTOR1_PIN1 3 // IN1 on the ULN2003 driver 1
#define STEPPER_MOTOR1_PIN2 4 // IN2 on the ULN2003 driver 1
#define STEPPER_MOTOR1_PIN3 5 // IN3 on the ULN2003 driver 1
#define STEPPER_MOTOR1_PIN4 6 // IN4 on the ULN2003 driver 1

// Motor pin definitions (Stepper motor 2)(Y-Axis)
#define STEPPER_MOTOR2_PIN1 8  // IN1 on the ULN2003 driver 2
#define STEPPER_MOTOR2_PIN2 9  // IN2 on the ULN2003 driver 2
#define STEPPER_MOTOR2_PIN3 10 // IN3 on the ULN2003 driver 2
#define STEPPER_MOTOR2_PIN4 11 // IN4 on the ULN2003 driver 2

// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48 Stepper Motor
AccelStepper stepper1(HALFSTEP, STEPPER_MOTOR1_PIN1, STEPPER_MOTOR1_PIN3, STEPPER_MOTOR1_PIN2, STEPPER_MOTOR1_PIN4);
AccelStepper stepper2(HALFSTEP, STEPPER_MOTOR2_PIN1, STEPPER_MOTOR2_PIN3, STEPPER_MOTOR2_PIN2, STEPPER_MOTOR2_PIN4);

char buffer;
int index = 0;
int serialInt[EXPECTED_INPUT_LENGTH + 1];
int packageType;
int dx;
int dy;
String input;

// Only run once at the begining
void setup()
{
    // Initialize serial communcation with 57600 baud rate
    Serial.begin(57600);

    // Stepper1 Testing
    stepper1.setMaxSpeed(MAX_SPEED);
    stepper1.setAcceleration(ACCELERATION);
    // Stepper2 Testing
    stepper2.setMaxSpeed(MAX_SPEED);
    stepper2.setAcceleration(ACCELERATION);
}

// Continuously running until power off
void loop()
{
    // Stepper run a step
    stepper1.run();

    if (!(stepper2.currentPosition() <= 0 && dy < 0))
    {
        stepper2.run();
    }
    else
    {
        stepper2.setSpeed(0);
    }
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

                // Map package byte to different variables
                packageType = serialInt[0];
                dx = (serialInt[1] - 1) * (serialInt[2] * 100 + serialInt[3] * 10 + serialInt[4]);
                dy = (serialInt[5] - 1) * (serialInt[6] * 100 + serialInt[7] * 10 + serialInt[8]);
                stepper1.move(dx);
                stepper2.move(dy);
                // stepper1.moveTo(serialInt[0] * 1000 + serialInt[1] * 100 + serialInt[2] * 10 + serialInt[3]);
                // stepper2.moveTo(serialInt[4] * 1000 + serialInt[5] * 100 + serialInt[6] * 10 + serialInt[7]);
            }
        }
        else
        {
            index = 0;
        }
    }
}
