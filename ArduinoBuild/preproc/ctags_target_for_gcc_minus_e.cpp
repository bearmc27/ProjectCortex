# 1 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino"
# 1 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino"
# 2 "c:\\PersonalProject\\ProjectCortex\\StepperMotorArduino\\StepperMotorArduino.ino" 2







// Motor pin definitions (Stepper motor 1)(X-Axis))





// Motor pin definitions (Stepper motor 2)(Y-Axis)





// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48 Stepper Motor
AccelStepper stepper1(8, 6 /* IN1 on the ULN2003 driver 1*/, 8 /* IN3 on the ULN2003 driver 1*/, 7 /* IN2 on the ULN2003 driver 1*/, 9 /* IN4 on the ULN2003 driver 1*/);
AccelStepper stepper2(8, 2 /* IN1 on the ULN2003 driver 2*/, 4 /* IN3 on the ULN2003 driver 2*/, 3 /* IN2 on the ULN2003 driver 2*/, 5 /* IN4 on the ULN2003 driver 2*/);

char buffer;
int index = 0;
int serialInt[9 + 1];
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
    stepper1.setMaxSpeed(3072);
    stepper1.setAcceleration(2048);
    // Stepper2 Testing
    stepper2.setMaxSpeed(3072);
    stepper2.setAcceleration(2048);
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
            if (index == 9)
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
