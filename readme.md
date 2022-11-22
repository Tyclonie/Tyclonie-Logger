# Tyclonie Logger

Version: 1.0
<br>
[GitHub](https://github.com/Tyclonie/Tyclonie-Logger)
<br>
pip install TyclonieLogger

## Documentation

### Requirements
These should automatically install during the install of Tyclonie Logger
<br>
Colorama (0.4.6) - pip install colorama==0.4.6

### Classes
TyclonieLogger()
- Arguments: datetime_format 
(default value="%Y/%m/%d @ %H:%M:%S") - Uses python library datetime for 
formatting [Datetime Documentation](https://docs.python.org/3/library/datetime.html)
- The TyclonieLogger class is what contains the functions and procedures required 
to log using the program, the functions and methods will be called from an
instance of the TyclonieLogger class

### Functions
log()
- Arguments: message
- Returns: Void (N/A)
- Logs the message that you pass into the console

warn()
- Arguments: message
- Returns: Void (N/A)
- Logs the message that you pass into the console as a warning, made to alert
the user of the program

error()
- Arguments: message
- Returns: Void (N/A)
- Logs the message that you pass into the console as an error, made to alert
the user of the program that someone bad has happened and it has been handled

get_datetime_formatted()
- Arguments: None
- Returns: String
- Gets the current date and time formatted in the format provided when its
TyclonieLogger instance was created. The use of this is for testing the format
you provided.

### Examples

Note: You may decide to use exact imports, using "**from tyclonielogger import 
TyclonieLogger**" instead of using "**import tyclonielogger**", simply then just
replace everywhere that says "**tyclonielogger.TyclonieLogger**" with 
"**TyclonieLogger**", and it will have the same effect

Using inheritance (Object Orientated Programming):
<br>
![](https://raw.githubusercontent.com/Tyclonie/Tyclonie-Logger/main/examples/inheritance_example.jpg)
<br>
Using sequencing:
<br>
![](https://raw.githubusercontent.com/Tyclonie/Tyclonie-Logger/main/examples/sequence_example.jpg)
<br>
Example output:
<br>
![](https://raw.githubusercontent.com/Tyclonie/Tyclonie-Logger/main/examples/output_example.jpg)
