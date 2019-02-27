bool isDone = false;
bool isGoingUp = true;

int startTime = 0;
int timer = 1000;

int currentSteps = 0;
int totalSteps = 120;

int delayUp = 25;
int delayDown = 5;

int motor1pinA = 2;
int motor1pinB = 4;
int motor1pinC = 3;
int motor1pinD = 5;

void setup() {

  pinMode(motor1pinA, OUTPUT);
  pinMode(motor1pinB, OUTPUT);
  pinMode(motor1pinC, OUTPUT);
  pinMode(motor1pinD, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
//  if(millis() - startTime > timer){
//      Serial.println(isDone);
//  
//      isDone = !isDone;
//      startTime = millis();
//  }

  // first we're going up, for up to X steps
  if(currentSteps < totalSteps && isGoingUp){
    up();  
    currentSteps++;
  }else{ //if we've reached the top
    if(isGoingUp){ //we send a signal to the pi
      Serial.println("reached top");
      isGoingUp = false;
    }
    
    down();
    currentSteps--;

    if(currentSteps == 0){ //if we've reached the bottom
      Serial.println("reached bottom");
      isGoingUp = true;
    }
    
  }
  

}

void up(){
  digitalWrite(motor1pinA, HIGH);
  digitalWrite(motor1pinB, LOW);
  digitalWrite(motor1pinC, LOW);
  digitalWrite(motor1pinD, LOW);
  delay(delayUp);
  digitalWrite(motor1pinA, LOW);
  digitalWrite(motor1pinB, HIGH);
  digitalWrite(motor1pinC, LOW);
  digitalWrite(motor1pinD, LOW);
  delay(delayUp);
  digitalWrite(motor1pinA, LOW);
  digitalWrite(motor1pinB, LOW);
  digitalWrite(motor1pinC, HIGH);
  digitalWrite(motor1pinD, LOW);
  delay(delayUp);
  digitalWrite(motor1pinA, LOW);
  digitalWrite(motor1pinB, LOW);
  digitalWrite(motor1pinC, LOW);
  digitalWrite(motor1pinD, HIGH);
  delay(delayUp);
}

void down(){
  digitalWrite(motor1pinA, LOW);
  digitalWrite(motor1pinB, LOW);
  digitalWrite(motor1pinC, LOW);
  digitalWrite(motor1pinD, HIGH);
  delay(delayDown);
  digitalWrite(motor1pinA, LOW);
  digitalWrite(motor1pinB, LOW);
  digitalWrite(motor1pinC, HIGH);
  digitalWrite(motor1pinD, LOW);
  delay(delayDown);
  digitalWrite(motor1pinA, LOW);
  digitalWrite(motor1pinB, HIGH);
  digitalWrite(motor1pinC, LOW);
  digitalWrite(motor1pinD, LOW);
  delay(delayDown); 
  digitalWrite(motor1pinA, HIGH);
  digitalWrite(motor1pinB, LOW);
  digitalWrite(motor1pinC, LOW);
  digitalWrite(motor1pinD, LOW);
  delay(delayDown);
}

