01.Problem: Read text
Write a program that reads text from the console (string) and prints it until it receives the "Stop" command.
input	    output
Nakov     Nakov
SoftUni   SoftUni
Sofia     Sofia
Bulgaria  Bulgaria
SomeText  SomeText
Stop
AfterStop
Europe
HelloWorld	

input	     output
Sofia      Sofia
Berlin     Berlin
Moscow     Moscow
Athens     Athens
Madrid     Madrid
London     London
Paris      Paris
Stop	

2.Problem: Password
Write a program that initially reads a user profile name and password. It then reads a login password.
• when entering a wrong password: prompt the user to enter a new password.
• when entering a correct password: we print "Welcome {username}!".

Sample input and output
input	  output
Nakov   Welcome Nakov!
1234
pass
1324
1234	

input	  output
Gosho   Welcome Gosho!
secret
secret	

03.Sum numbers
Write a program that reads an integer from the console and on each successive line integers until their sum is greater than or equal to the original number. 
After reading is complete, print the sum of the entered numbers.

Sample input and output
input 	output
100     100
10
20
30
40	

input	  output
20	    21
1
2
3
4
5
6

04.Problem: Sequence_2k+1
Write a program that reads a number n entered by the user and prints all numbers ≤ n from the sequence: 1, 3, 7, 15, 31, …. Each subsequent number is calculated by multiplying the previous one by 2 and adding 1.

Sample input and output
input	  output	    input	  output	        input	  output		        input	  output
3       1           8       1               17      1                 31      1
        3                   3                       3                         3
                            7                       7                         7
                                                    15                        15
                                                                              31

05.Problem: Account balance 
Write a program that calculates how much total money is in the account after you make a certain number of deposits. 
On each line you will receive the amount you need to deposit into the account until you receive a "NoMoreMoney" command. 
For each amount received, the console should display "Increase: " + the amount and add it to the account. 
If you get a number less than 0 the console should display "Invalid operation!" and the program to end. 
When the program ends, it should print "Total: " + the total amount in the account formatted to the second decimal place.

Sample input and output
input	      output
5.51          Increase: 5.51
69.42         Increase: 69.42
100           Increase: 100.00
NoMoreMoney   Total: 174.93

input	      output
120           Increase: 120.00
45.55         Increase: 45.55
-150	      Invalid operation!
              Total: 165.55

06.Problem: Max number
Write a program that, until receiving the "Stop" command, reads integers entered by the user, finds the largest among them, and prints it. 
Enter one number per line.

Sample input and output
input	  output        input	  output     input	  output      input	  output       input	  output
100       100           -10       20         45           99          999         999          -1         -1
99                      20                   -20                      Stop                     -2
80                      =30                   7                                                Stop
70                      Stop                  99                                    
Stop                                          Stop

07.Problem: Min number
Write a program that, until the "Stop" command is received, reads integers entered by the user, finds the smallest number among them, and prints it. 
Enter one number per line.

Sample input and output
input	  output        input	  output     input	  output      input	  output       input	  output
100       70            -10       -30        45           -20         999         999          -1         -2
99                      20                   -20                      Stop                     -2
80                      -30                  7                                                 Stop 
70                      Stop                 99
Stop                                         Stop 

08.Problem: Graduation
Write a program that calculates the grade point average of a student over his entire course. On the first line, you will get the student's name, and on each subsequent line, their annual grades. The student advances to the next grade if his annual grade is greater than or equal to 4.00. If the student is interrupted more than once, the student is expelled and the program ends, printing the name of the student and the class in which he was expelled.
  On successful completion of 12th grade to print:
"{student name} graduated. Average grade: {the average grade of the entire study}"
In case the student is excluded from school, to print:
"{student name} has been excluded at {grade in which he was excluded} grade"
The value must be formatted to the second decimal place.

Sample input and output
input	output
Gosho   Gosho graduated. Average grade: 5.53
5
5.5
6
5.43
5.5
6
5.55
5
6
6
5.43
5	

input	output
Mimi    Mimi has been excluded at 8 grade
5
6
5
6
5
6
6
2
3	




















