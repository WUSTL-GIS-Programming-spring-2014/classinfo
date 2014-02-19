#Quiz 2: Lists and flow control  
Assume these variable definitions at the start of each question.  
```
a = [1,3]
b = [0,-1]
c = (2,4)
d = (3,9)
```

Provide the output (to standard output) of the following operations. If the operation results in an error, put 'Exception'.  
1.
```
a.extend(b)
print a  
```
  [1, 3, 0, -1]  

2.
```
a + b
print a
```
  [1, 3]  

3.
```
while a:
    print a.pop(),
```  
  3 1  

4.
```
for a in b:
    print a,
```  
  0 -1  

5.
```
a[0] = c
print a
```  
  [(2, 4), 3]  

6.
```
c[0] = a
print c
```  
  Exception  

