#! /usr/bin/env node

var b = require('bonescript');

var BTN1 = "P9_11";
var BTN2 = "P9_15";
var BTN3 = "P9_21";
var BTN4 = "P9_27";

var LED1 = "P9_13";
var LED2 = "P9_17";
var LED3 = "P9_23";
var LED4 = "P9_29";

b.pinMode(BTN1, b.INPUT, 7,'pullup');
b.pinMode(BTN2, b.INPUT, 7,'pullup');
b.pinMode(BTN3, b.INPUT, 7,'pullup');
b.pinMode(BTN4, b.INPUT, 7,'pullup');



b.pinMode(LED1, b.OUTPUT, 7, 'disable');
b.pinMode(LED2, b.OUTPUT, 7, 'disable');
b.pinMode(LED3, b.OUTPUT, 7, 'disable');
b.pinMode(LED4, b.OUTPUT, 7, 'disable');


b.attachInterrupt(BTN1, true, b.CHANGE, onLED1);
b.attachInterrupt(BTN2, true, b.CHANGE, onLED2);
b.attachInterrupt(BTN3, true, b.CHANGE, onLED3);
b.attachInterrupt(BTN4, true, b.CHANGE, onLED4);


function onLED1(x){
b.digitalWrite(LED1, x.value);
console.log("1"+x.value);
}

function onLED2(x){
b.digitalWrite(LED2, x.value);
console.log("2"+x.value);
}

function onLED3(x){
b.digitalWrite(LED3, x.value);
console.log("3"+x.value);
}

function onLED4(x){
b.digitalWrite(LED4, x.value);
console.log("4"+x.value);
}
