  
 1. To access functions of the underlying operation system, would module would you use? ```os```, ```pytz```, or ```sys```?  
*os*    
  
 2. If you want an object to represent a full time stamp such as 2/12/2014 17:00:00.000, would you use a ```datetime```, ```pytz```, or ```time``` object?  
*datetime*  
  
 3.  
```
            #Start by setting the values of a, b, and c to zero  
            a = b = c = 0  
            #Then execute this try...except...finally block
            try:  
                a = 1  
                print x #This raises a NameError  
                a = 2  
            except NameError:  
                b = 1  
            except:  
                b = 2  
                raise  
            finally:  
                c = 1
```
What are the values of a, b, and c?  
  *a = 1*  
    *When ```print x``` raises an error, the next line is skipped, so a stays at 1 instead of being set to 2.*  
  *b = 1*  
    *The ```NameError``` exception is caught by the first ```except NameError``` clause. The second catch all ```except``` is skipped because the error has already been handled.*  
  *c = 1*  
    *The ```finally``` is executed after error handling as a last operation before exiting the ```try``` block.*  
