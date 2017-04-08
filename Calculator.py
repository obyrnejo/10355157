# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print ("5.Exponent")
print("6.Cubed")
print("7.Squared")
print("8.squareRoot")
print("9.Cosine")
print("10.Sine")

choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10):")

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))		



#test to see addition 2 +2 = 4, 5+3=8, 4+4=8
if choice == '1':
  def sum(first, second):
      return first + second

      

#test to see subtraction 2-2 = 0, 5-3=2, 4+0=4. 3-4=-1
elif choice == '2':
  def subtract (first, second):
    return first - second

	
#test to see mupltiplication 2 *2 = 4, 5*3=15, 4*0=4, 3*-4=-12
elif choice == '3':
  def multiply (first, second):
    return first * second

	
#test to see 2 /2 = 1, 5/2=2.5, 4/0=none, 3/-4=-0.75
elif choice == '4':	
  def divide (first, second):
    return first / float( second)

	
#test to see 2**3=8, 5**2=25, 4**0=1, 3**-4=0.012
elif choice == '5':
  def exponent (first, second):
    return first ** float( second)

	
#test to see cubed 2**3=8, 5**3=125, 4**3=64, 3**3=27
elif choice == '6':
  def cubed(num):
    return (num **(1.0 /3.0))


#test to see squared 2**2=4, 5**2=25, 4**2=16, 3**2=9
elif choice == '7':
  def squared (num):
    return (num ** (1.0 / 2.0))

	
#test to see squareRoot 81=9, 9=3, 64=8, 6=2.449
elif choice == '8':	
  def squareRoot(x):
	  return math.sqrt (x)
	

#test to see sine 1=0.841, 3= 0.141, 99=-0.999, 5=-0.958
elif choice == '9':	 
  def sine (x):
	  return sine(math.radians (x))
	
	
#test to see Cosine 1=0.540, 3= -0.99, 99=-0.04, 5=-0.283
elif choice == '10':  
  def cosine (x):
	  return cosine (math.radians (x))
