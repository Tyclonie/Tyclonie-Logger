### Tyclonie Logger

Requires Colorama.

Create an instance of the TyclonieLogger class, you can pass a custom format if you wish, using the datetime libraries format.
The default format is "%Y/%m/%d @ %H:%M:%S" This is (YYYY/MM/DD @ HH:MM:SS)

The functions you can call from the instance of TyclonieLogger are
get_datetime_formatted() -> str NOTE: (This will not be needed to be used by the user, unless you really want to)
log(message) -> None
warn(message) -> None
error(message) -> None