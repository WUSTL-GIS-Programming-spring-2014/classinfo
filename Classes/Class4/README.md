Modules
==========

* Quick notes on strings  
[String literal escape sequences](http://docs.python.org/2/reference/lexical_analysis.html#string-literals)  
  - Unicode strings (u'')  
    Encodes escape sequences and unicode characters  
  - Raw strings (r"")  
    Mostly used for regular expression matching (which never end in a backslash)  

* What is a Syntax Error?  
  - Error when parsing code for compiling  
  - Unconditionally fatal (will not compile)  
* What is an Exception?  
  - Run time error, and not unconditionally fatal  
  - Unhandled exceptions stop execution  

## Exception Examples  
```
	10 * (1/0)

	4 + x*3

	u'2' + 2

	mylist = [0,1,2,3]
	mylist[4]

	a = {'b':2}
	a['c']
	
	import xxyzz
```
[List of Built-In Exceptions](http://docs.python.org/2/library/exceptions.html#bltin-exceptions)  
  
## Handling Exceptions  
* ```try..except```  
* ```except Exception as e:```  
* ```except (Exception1,Exception2,Exception3)```   
  - This is a tuple  
  - Do not use ```except Exception1, Exception2:```  
* ```except: print "Unexpected error:", sys.exc_info()[0]``` Wildcard for all Exceptions  
* ```raise```  
*	```raise Exception```  
* ```try..finally```  
* ```try..except..else..finally```  

## Modules  
A *module* is a file with **definitions** plus **statements**  
You wrote a module for exercise 1.  

```__name__``` is the name of the module.  
Variables are in the module's symbol table, not global variables.  
[Simple Symbol Table example](https://github.com/WUSTL-GIS-Programming-spring-2014/class_four/blob/master/modulesymboltables.py)  

A *package* is a collection of submodules, e.g. arcpy.  

####Useful functions
* ```dir()```  
*	```help()```  

###```os``` module  
*Interacts with the operating system*  
* ```os.environ``` only shows environ when imported  
* ```os.access``` Access attributes of a path/file  
  - ```os.F_OK``` exists  
  - ```os.R_OK``` readable  
  - ```os.W_OK``` writeable  
  - ```os.X_OK``` executible  
* ```os.chdir``` This is equivalent to cd.  
* ```os.getcwd``` ```os.getcwdu``` Get the current working directory (as unicode).  
* ```os.remove``` ```os.rmdir``` Does not work if in use or directory is not empty.  

###```datetime``` module  
* ```datetime.date(year, month, day)``` All parameters are required.  
* ```datetime.date.today()``` Date object representing today's date (machine time).  
* ```datetime.time(hour, minute, second, microsecond, tzinfo)``` All patameters are optional other than hour.
* ```datetime.datetime(...)``` The Date parameters are required. Time patameters are optional.  
* ```datetime.datetime.now()```  Datetime object representing time right now (machine time).  
* ```datetime.timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)```  
Used for "date math" in days, second, and microseconds.  
* ```ctime()``` ctime formatting  
* ```strftime()``` custom formatting. See (http://strftime.org/) for more info.  

###```pytz``` module  
[Documentation](https://pypi.python.org/pypi/pytz/)  
Can install from [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/) * ```pytz.utc``` UTC timezone. Do operations in UTC, then convert to desired time zone.  
* ```pytz.timezone()``` Define a local timezone.  
  - 'US/Eastern'  
  - 'US/Central'  
* ```zone.localize()``` Add timezone to datetime object  
	
###In Class Exercise  
[Datetime Examples](https://github.com/WUSTL-GIS-Programming-spring-2014/class_four/blob/master/dtexamples.py)  
