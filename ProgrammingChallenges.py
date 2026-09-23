numbers = [12, 0, -3, -4, 5]
positive_count = 0
negative_count = 0
zero_count = 0
#for i in numbers
for i in numbers:
#look at number and print if it's positive, negative or zero
#if number is positive, increment positve counter
    if i > 0 :
        print ("Positive")
        positive_count += 1
    #if number is negative, increment negative counter
    elif i < 0 :
        print ("Negative")
        negative_count += 1
    #if number is zero, increment zero counter
    elif i == 0 :
        print ("Zero")
        zero_count += 1

#loop

#print final counts
print (f"Total number of positives: {positive_count}")
print (f"Total number of negatives: {negative_count}")
print (f"Total number of zeros: {zero_count}")