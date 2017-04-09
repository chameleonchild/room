#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(void){
        printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
        char c;
        char userInput[9];
        int manna;
        int gold;
        int i;
        char invString[100];
        //: try using get instead
        scanf("userInput=%c", &c);
        userInput[0]=c;
        for(i = 1; i < 8 && scanf("%c", &c) != EOF; i++){
                if(c == '&'){
                        break;
                }
                userInput[i]=c;
                userInput[i+1] = '\0';
        }
scanf("inventory=%d", &manna);
        scanf("%c%c%c%d", &c, &c, &c, &gold);
        fgets(invString, 100, stdin);
        printf("%s", invString);
        if(strcmp(userInput,"REFRESH") == 0){
                printf("<html><body><center>");
                printf("<img src =\"https://mpsapsiblog.files.wordpress.com/2015/11/7u.jpg\" width=\"900\" height=\"600\"></br>");
                printf("<font>To go to class, type PLAY.</font></br>");
                printf("<form action=\"http://cs.mcgill.ca/~gadach/cgi-bin/room.cgi\" method=\"post\">");
                printf("<input type =\"text\" name=\"userInput\"><input type = \"submit\" value=\"Submit\"></br>");
                printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
                printf("<font> Other options: DROP, EXIT, REFRESH </font></br></form></center>");
                printf("Inventory: %d manna and %d gold  </body></html>", manna, gold);
        }else if(strcmp(userInput, "EXIT") == 0){
                 FILE* in = fopen("../resources.csv", "r");
                int roomManna;
                int roomGold;
                fscanf(in,"%d,%d", &roomManna, &roomGold);
                fclose(in);
                roomGold += gold;
                system("rm ../resources.csv");
                FILE* out = fopen("../resources.csv", "w");
                fprintf(out, "%d,%d, 1", roomManna, roomGold);
                fclose(out);
                printf("<html><body> Sorry to see you leave! At least the classes are recorded </body></html>");
        }else if(userInput[0] =='D' && userInput[1] == 'R' && userInput[2] == 'O' && userInput[3] == 'P'){
                int drop = userInput[5] - '0';
                gold = gold - drop;
                manna = manna + (drop/2);
                FILE* in = fopen("../resources.csv", "r");
                int roomManna;
                int roomGold;
                fscanf(in,"%d,%d", &roomManna, &roomGold);
                fclose(in);
                roomGold += drop;
                system("rm ../resources.csv");
                FILE* out = fopen("../resources.csv", "w");
                fprintf(out, "%d,%d, 1", roomManna, roomGold);
                fclose(out);
                printf("<html><body><center>");
                printf("<img src =\"https://mpsapsiblog.files.wordpress.com/2015/11/7u.jpg\" width=\"900\" height=\"600\"></br>");
                printf("<font>To go to class, type PLAY.</font></br>");
                printf("<form action=\"http://cs.mcgill.ca/~gadach/cgi-bin/room.cgi\" method=\"post\">");
                printf("<input type =\"text\" name=\"userInput\"><input type = \"submit\" value=\"Submit\"></br>");
                printf("<input type=\"hidden\" name=\"inventory\" value=\"%d,%d\">", manna, gold);
                printf("<font> Other options: DROP, EXIT, REFRESH </font></br></form></center>");
                printf("Inventory: %d manna and %d gold  </body></html>", manna, gold);

        }else if(strcmp(userInput, "PLAY")==0){
                printf("a3/COMP296room.html </body> </html>");
        }else{
                printf("incorrect input");
                printf("%s </body></html>", userInput);
        }
        return 0;
}
