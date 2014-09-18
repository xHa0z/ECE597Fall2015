#! /usr/bin/env node

var b = require('bonescript');

var UP = "P9_11";
var DOWN = "P9_15";
var LEFT = "P9_21";
var RIGHT = "P9_27";
var CLR = "P9_12";


var LED1 = "P9_13";
var LED2 = "P9_17";
var LED3 = "P9_23";
var LED4 = "P9_29";

var col;
var row;

var currentX=0;
var currentY=0;

var playground = new Array(10);
for( row = 0; row < 10; row++){
	playground[row] = new Array(10);
}
for(row = 0; row < 10; row++){
	for( col = 0; col < 10; col++){
		playground[row][col] = 0;
	}
}

console.log(playground);




b.pinMode(UP, b.INPUT, 7,'pullup');
b.pinMode(DOWN, b.INPUT, 7,'pullup');
b.pinMode(LEFT, b.INPUT, 7,'pullup');
b.pinMode(RIGHT, b.INPUT, 7,'pullup');
b.pinMode(CLR, b.INPUT, 7, 'pullup');


b.pinMode(LED1, b.OUTPUT, 7, 'disable');
b.pinMode(LED2, b.OUTPUT, 7, 'disable');
b.pinMode(LED3, b.OUTPUT, 7, 'disable');
b.pinMode(LED4, b.OUTPUT, 7, 'disable');


b.attachInterrupt(UP, true, b.CHANGE, goUP);
b.attachInterrupt(DOWN, true, b.CHANGE, goDOWN);
b.attachInterrupt(LEFT, true, b.CHANGE, goLEFT);
b.attachInterrupt(RIGHT, true, b.CHANGE, goRIGHT);
b.attachInterrupt(CLR, true, b.CHANGE, goCLR);

function goCLR(x){
	if(x.value == 0){
		for(i = 0; i < 10; i++)
			for(j = 0; j < 10; j++)
			playground[i][j] = 0;
	}
	console.log(playground);
}

function goUP(x){
	if(x.value == 0){
		b.digitalWrite(LED1,b.HIGH);
		if(currentX != 0) currentX = currentX-1;
		else currentX = currentX;
	}
	if(x.value == 1){
		b.digitalWrite(LED1, b.LOW);
		playground[currentX][currentY] = 1;
		console.log(playground);
	}
}

function goDOWN(x){
	if(x.value == 0){
		b.digitalWrite(LED2, b.HIGH);
		if(currentX != 9) currentX = currentX+1;
		else currentX = currentX;
	}
	if(x.value == 1){
		b.digitalWrite(LED2, b.LOW);
		playground[currentX][currentY] = 1;
		console.log(playground);
	}
}

function goLEFT(x){
	if(x.value == 0){
		b.digitalWrite(LED3, b.HIGH);
		if(currentY != 0) currentY = currentY-1;
		else currentY = currentY;
	}
	if(x.value == 1){
		b.digitalWrite(LED3, b.LOW);
		playground[currentX][currentY] = 1;
		console.log(playground);
	}
}

function goRIGHT(x){
	if(x.value == 0){
		b.digitalWrite(LED4, b.HIGH);
		if(currentY != 9) currentY = currentY+1;
		else currentY = currentY;
	}
	if(x.value == 1){
		b.digitalWrite(LED4, b.LOW);
		playground[currentX][currentY] = 1;
		console.log(playground);
	}
}
