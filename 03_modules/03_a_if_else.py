"""
https://www.hackerrank.com/challenges/py-if-else?isFullScreen=true

Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""
if __name__ == '__main__':
    n = int(input().strip())
    
    # Write your logic here
    if n % 2 == 1:
      print("Weird")
    elif n > 1 and n < 6 :
      print("Not Weird")
    elif n > 5 and n < 21 :
      print("Weird")
    else:
      print("Not Weird")
    
