#Yashkumar Shinde
Gr-11810825
#roll no-M-53
#Division-M

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
         
   else:  
       print(num,"is a prime number")  
         
else:  
     print(num,"is a prime number")
