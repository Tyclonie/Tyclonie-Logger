# Tyclonie Logger

Version: 2.0
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
- Arguments: **options
(Full list of options are listed after the code examples along side its default 
value)
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

### TyclonieLogger() Options

#### Notes
- For selectable forground colours output show_foreground_colours on a 
TyclonieLogger instance
- For selectable background colours output show_background_colours on a
TyclonieLogger instance
- For selectable styles output show_styles on a TyclonieLogger instance
- They're layed out such that option=DEFAULT_VALUE
- After outputtind the selectable styles, if its hard to see text
you can highlight it in the terminal to make it easier to see

#### Options
datetime_format="%Y/%m/%d @ %H:%M:%S"
<br>
datetime_text_divider=" | "
<br>
datetime_background="YELLOW"
<br>
datetime_foreground="BLACK"
<br>
datetime_style="NORMAL"
<br>
log_identifier_foreground="GREEN"
<br>
log_identifier_background="NORMAL"
<br>
log_identifier_style="NORMAL"
<br>
log_message_foreground="NORMAL"
<br>
log_message_background="NORMAL"
<br>
log_message_style="NORMAL"
<br>
log_identifier_message_divider=": "
<br>
log_dividers_foreground="NORMAL"
<br>
log_dividers_background="NORMAL"
<br>
log_dividers_style="NORMAL"
<br>
warn_identifier_foreground="RED"
<br>
warn_identifier_background="NORMAL"
<br>
warn_identifier_style="BRIGHT"
<br>
warn_message_foreground="NORMAL"
<br>
warn_message_background="NORMAL"
<br>
warn_message_style="NORMAL"
<br>
warn_identifier_message_divider=": "
<br>
warn_dividers_foreground="NORMAL"
<br>
warn_dividers_background="NORMAL"
<br>
warn_dividers_style="NORMAL"
<br>
error_identifier_foreground="BLACK"
<br>
error_identifier_background="RED"
<br>
error_identifier_style="BRIGHT"
<br>
error_message_foreground="RED"
<br>
error_message_background="NORMAL"
<br>
error_message_style="NORMAL"
<br>
error_identifier_message_divider=": "
<br>
error_dividers_foreground="NORMAL"
<br>
error_dividers_background="NORMAL"
<br>
error_divider_style="NORMAL"
