from tyclonielogger import TyclonieLogger


logger = TyclonieLogger()
print(logger.show_foreground_colours())
print(logger.show_background_colours())
print(logger.show_styles())


"""

datetime_format="%Y/%m/%d @ %H:%M:%S"
datetime_text_divider=" | "
datetime_background="YELLOW"
datetime_foreground="BLACK"
datetime_style="NORMAL"

log_identifier_foreground="GREEN"
log_identifier_background="NORMAL"
log_identifier_style="NORMAL"
log_message_foreground="NORMAL"
log_message_background="NORMAL"
log_message_style="NORMAL"
log_identifier_message_divider=": "
log_dividers_foreground="NORMAL"
log_dividers_background="NORMAL"
log_dividers_style="NORMAL"

warn_identifier_foreground="RED"
warn_identifier_background="NORMAL"
warn_identifier_style="BRIGHT"
warn_message_foreground="NORMAL"
warn_message_background="NORMAL"
warn_message_style="NORMAL"
warn_identifier_message_divider=": "
warn_dividers_foreground="NORMAL"
warn_dividers_background="NORMAL"
warn_dividers_style="NORMAL"

error_identifier_foreground="BLACK"
error_identifier_background="RED"
error_identifier_style="BRIGHT"
error_message_foreground="RED"
error_message_background="NORMAL"
error_message_style="NORMAL"
error_identifier_message_divider=": "
error_dividers_foreground="NORMAL"
error_dividers_background="NORMAL"
error_divider_style="NORMAL"

"""
