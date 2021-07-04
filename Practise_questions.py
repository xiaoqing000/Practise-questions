# *** Capital the first letter*** #
# import sys
# def cap():
#     for line in sys.stdin:
#         print(line.title(),end="")
# cap()

#***  reverse a string *** #
#mport sys
    # read inuput string
#input=sys.stdin.readline()
#words = input.split()
    # then reverse the split string list and join using space
#reverse_sentence = ' '.join(reversed(words))
    # finally return the joined string
#print(reverse_sentence,end='')


# # ***  fibonacci  *** #
#Function for nth Fibonacci number
import sys 
for line in sys.stdin:
    n=int(line)
    def fib(n):
    #Check if input is 0 then it will
    #print incorrect input
        if n< 0:
            print("Incorrect input")
    # Check if n is 0
    # then it will return 0
        elif n  == 0:
            return 0
    # Check if n is 1,2
    # it will return 1
        elif n  == 1 or n  == 2:
            return 1
        else:
            return fib(n -1) + fib(n -2)
 
#Driver Program
print(fib(n))


print('Hello')


print("How are you")

print('I am good,thank you.')