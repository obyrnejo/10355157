from Calculator import*

import unittest
import math 


class MyTest (unittest.TestCase):
#test to see 2+2=4, 5+3=8, 4+4=8
    def testAdd (self):
        self.assertEqual(sum(2,2),4)
        self.assertEqual(sum(5,3),8)
        self.assertEqual(sum(4,4),8)
        
#test to see 2-2=0, 5-3=2, 4-0=4
    def testSubtract(self):
        self.assertEqual(subtract(2,2), 0)
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(4,0),4)        
        self.assertEqual(subtract(3,4), -1)
        
#test to see 2*2=4, 5*3=15, 4*0=4
    def testMultiply(self):
        self.assertEqual(multiply(2,2), 4)
        self.assertEqual(multiply(5,3),15)
        self.assertEqual(multiply(4,0),0)        
        self.assertEqual(multiply(3,-4), -12)
                
#test to see 2/2=1, 5/3=1.6, 4/0=
    def testDivide(self):
        self.assertEqual(divide(2,2), 1)
        self.assertEqual(divide(5,2),2.5)
        self.assertEqual(divide(4,0),none)        
        self.assertEqual(divide(3,-4),-0.75 )
		
#test to see 2**3=8, 5**2=25, 4**0=1, 3**-4=0.012
    def testExponent(self):
        self.assertEqual(exponent(2,3), 8)
        self.assertEqual(exponent(5,2),25)
        self.assertEqual(exponent(4,0),1)        
        self.assertEqual(exponent(3,-4),0.012 )
			
#test to see 2**3=8, 5**3=125, 4**3=64, 3**3=27
    def testCubed(self):
        self.assertEqual(cubed(2,3), 8)
        self.assertEqual(cubed(5,3),125)
        self.assertEqual(cubed(4,3),64)        
        self.assertEqual(cubed(3,3),27)			
        
#test to see 2**2=, 5**2=25, 4**2=16 3**2=9
    def testSquared(self):
        self.assertEqual(squared(2,2), 4)
        self.assertEqual(squared(5,2),25)
        self.assertEqual(squared(4,2),16)        
        self.assertEqual(squared(3,3),9)		

#test to see 81=9, 9=3, 64=8, 6=2.449
    def testSquareRoot(self):
        self.assertEqual(squareRoot(81),9)
        self.assertEqual(squareRoot(9),3)
        self.assertEqual(squareRoot(64),8)        
        self.assertEqual(squareRoot(6), 2.449)	
		
#test to see 1=0.841, 3= -0.99, 99=-0.999, 5=-0.958
    def testSine(self):
        self.assertEqual(sine(1), 0.841)
        self.assertEqual(sine(3),0.141)
        self.assertEqual(sine(99),-.0999)        
        self.assertEqual(sine(5), -.0958)	
		
#test to see 1=0.540, 3= -0.99, 99=-0.04, 5=-0.283
    def testCosine(self):
        self.assertEqual(cosine(1), 0.540)
        self.assertEqual(cosine(3),-0.99)
        self.assertEqual(cosine(99),0.04)        
        self.assertEqual(cosine(5), 0.283)			        		
		
if __name__ == '__main__':
    unittest.main()
