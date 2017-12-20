# 1 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino"
# 1 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino"
# 2 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino" 2







// Motor pin definitions (Stepper motor 1)





// Motor pin definitions (Stepper motor 2)






// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48 Stepper Motor
AccelStepper stepper1(8, 3 /* IN1 on the ULN2003 driver 1*/, 5 /* IN3 on the ULN2003 driver 1*/, 4 /* IN2 on the ULN2003 driver 1*/, 6 /* IN4 on the ULN2003 driver 1*/);
AccelStepper stepper2(8, 8 /* IN1 on the ULN2003 driver 2*/, 10 /* IN3 on the ULN2003 driver 2*/, 9 /* IN2 on the ULN2003 driver 2*/, 11 /* IN4 on the ULN2003 driver 2*/);

char buffer;
int index = 0;
int serialInt[8 + 1];
String input;

// Only run once at the begining
void setup()
{
    // Initialize serial communcation with 57600 baud rate
    Serial.begin(57600);

    // Stepper1 Testing
    stepper1.setMaxSpeed(1024);
    stepper1.setAcceleration(1024);
    // Stepper2 Testing
    stepper2.setMaxSpeed(1024);
    stepper2.setAcceleration(1024);
}

// Continuously running until power off
void loop()
{
    // Stepper run a step
    stepper1.run();
    stepper2.run();
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
            if (index == 8)
            {
                index = 0;
                // servoAngle_0 = serialInt[0] * 100 + serialInt[1] * 10 + serialInt[2];
                // servoSpeed_0 = serialInt[3] * 100 + serialInt[4] * 10 + serialInt[5];
                // servoAngle_1 = serialInt[6] * 100 + serialInt[7] * 10 + serialInt[8];
                // servoSpeed_1 = serialInt[9] * 100 + serialInt[10] * 10 + serialInt[11];

                stepper1.moveTo(serialInt[0] * 1000 + serialInt[1] * 100 + serialInt[2] * 10 + serialInt[3]);
                stepper2.moveTo(serialInt[4] * 1000 + serialInt[5] * 100 + serialInt[6] * 10 + serialInt[7]);
            }
        }
        else
        {
            index = 0;
        }
    }
}
