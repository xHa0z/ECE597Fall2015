void main (void){
	system("i2cset -y 1 0x48 1 0x82");
	system("i2cset -y 1 0x48 2 0x30");
	system("i2cset -y 1 0x48 3 0x4b");
	system("./gpio-int-test 20");
}
