#user_age = int(input("How old are you?"))
#print("You are " + str(user_age * 7) + " years old in dog years.")

#operators
#calculation = 2 ** 16
# to the power of is double asterisk **
#calculation = 5 / 3
#print(calculation)
#print(f"The result is: {calculation}")

#shortcut for reassigning a variable
#account_balance = 1000
#account_balance = account_balance + 500
#account_balance += 500
#print(account_balance)

#comparison = (5 > 3) and (4 == 4) and (2 > 3)
#print(comparison)

#if age > 0 and age < 18:
    #print("You are a minor.")


#if (age > 0 and name == "Yello") or (name == "Taylor":)
#if (age > 0) and (name == "Yello") or (name == "Taylor"):
    #print("You are either a minor or your name is Taylor or Yello.")

#LOOPS
#for i in range(5):
    #print(i)
#you don't have to use i, you can use any variable name
#for counter in range(5):
    #print(counter)
#for i in range(1, 10): #this would end this counter at 9, if you want it to end at 10, you would have to put 11 in the range
    #print(i)
#for i in range (1, 10, 2): # this counts by 2's #this would end this counter at 9, if you want it to end at 10, you would have to put 11 in the range
    #print(i)
#for i in range (0, 101, 5):
    #print(i)

#while age < 0:
    #print("You cannot be a negative age.")
    #age = int(input("How old are you?"))

    #if (age == -16):
        #break (an option, but lazy, makes it hard to debug) The oppostite of break is continue, which will skip the rest of the code and go back to the top of the loop.



#for i in range(1,4):
    #for j in range(1, 11):
        #print(f"Day {i}: Appointment {j}")
        
        
        
        
        
        
#odd number checker 
#numbers = [14, 2, 3, 45, 5]

#for num in numbers:
    #if num % 2 == 0:
        #print("Even")
    #else:
        #print("Odd")

#defining a function

#def is_odd(numero):
    #odd = True

    #if numero %2 == 0:
     #   odd = False
    #else:
     #   odd = True

    #return odd
#combining number checker and number checker
#for num in numbers:
 #   if is_odd(num):
  #      print(f"{num} is odd")
   # else:
    #    print(f"{num} is even")

#10/5/2026
#number = [11, 25, -2, 7, 18]
#range is start stop step
#this will print 0, 1, 2, 3, 4, just the range
#for i in range (0,5):
 #   print(i)

#for i in range(5):
 #   print(i+100)
#for i in range(5):
 #   print(number[i])
#for num in number:
 #   print(num)



#10/14/2026
#has_error: True
#while has_error:
 #   try: 
  #      number = int(input("Enter a number: "))
   #     print(number)

    #    has_error = False
    #except:
     #   print("Invalid number. Plese try again.")

#from (filename) import (function)

11//2/2026
#objects are immutable or mutable (cannot change or can change)
#what we store in variables is not the actual value, its the address to the value
#.append adds one item at a time, to the end of a list
#random_list = []
#random_list.extend(["yadda", "babba", "dodda"])
#extend lets you add multiple at a time
#print(random_list[-1]) this would print the last item in the list  
#stack and queue - stack uses lifo(last in, first out), queue uses fifo
#a list uses a stack, .pop removes the last item from the list. You can customize by doing .pop(#) <-- insert index number
#.remove, instead of passing the index pass the value you want to remove 
#random_list.remove("babba")
#random_list.append("yadda")
#print(random_list.count("yadda"))
#if "yadda" in random_list:
  #  print("Found the word!")
#random_list.sort() #puts it in alphabletical or numeric order 
#a tuple is a list that cannot change once it is first set 
#a set finds the overlap in a venn diagram (or the absence of overlap)