#include <stdio.h>

int main (void) {
  int row = 10;
  int col = 10;
  char input;
  char playground[10][10];
  int currentX = 0;
  int currentY = 0;
  for (int i=0;i<row;i++)
    for (int j=0;j<col;j++)
      playground[i][j]='-';

  while(input!=EOF){

    for(int i = 0; i < row; i++){
      for(int j = 0; j < col; j++){
        //playground[i][j] = putchar('-');
        printf("%c",playground[i][j]);
      }printf("\n");
    }
    input = getchar();

    switch(input){
      case EOF: {
                  break;
                }

      case'w':{
                if(currentX != 0){
                  playground[currentX][currentY] = 'x';
                  currentX--;
                  playground[currentX][currentY] = 'x';
                }
                else playground[currentX][currentY] = 'x';

                break;
              }

      case's':{
                if(currentX != row-1){
                  playground[currentX][currentY] = 'x';
                  currentX++;
                  playground[currentX][currentY] = 'x';
                }
                else playground[currentX][currentY] = 'x';

                break;
              }
      case 'a':
              if(currentY != 0){
                currentY--;
                playground[currentX][currentY] = 'x';
              }
              else playground[currentX][currentY] = 'x';

              break;

      case 'd':
              if(currentY != 9){
                currentY++;
                playground[currentX][currentY] = 'x';
              }
              else playground[currentX][currentY] = 'x';
              break;
      default:
              break;
    }

  }

}

