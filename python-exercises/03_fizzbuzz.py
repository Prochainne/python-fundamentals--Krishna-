"""Write a program that prints the numbers from 1 to n. But for 
multiples of fizz print "Fizz" instead of the number and for the multiples of 
buzz print "Buzz". For numbers which are multiples of both fizz and buzz print "FizzBuzz"."""
def fizzbuzz(n,fizz,buzz):
    for i in range(1, n+1):
        if i % (fizz*buzz) == 0:
            print("FizzBuzz")
        elif i % fizz == 0:
            print("Fizz")
        elif i % buzz == 0:
            print("Buzz")
        else:
            print(i)
n=int(input("Enter the number: "))
fizz=int(input("Enter the fizz number: "))
buzz=int(input("Enter the buzz number: "))
fizzbuzz(n,fizz,buzz) 