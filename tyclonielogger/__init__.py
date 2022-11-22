import datetime
import inspect
from colorama import Fore, Back, Style, init

""" PLEASE NOTE THAT ALL COLOUR INFORMATION IS FROM COLORAMA """


class TyclonieLogger:
    def __init__(self, **options):
        self.__set_options(options)
        self.__load_colours()

    def __load_colours(self) -> None:
        self.fore_colours = {}
        self.back_colours = {}
        self.styles = {}
        all_fore_colours = inspect.getmembers(Fore)
        for fore_colour in all_fore_colours:
            if isinstance(fore_colour[0], str) and fore_colour[0] != "__module__":
                self.fore_colours[fore_colour[0]] = fore_colour[1]
        self.fore_colours["NORMAL"] = self.fore_colours.get("RESET")
        all_back_colours = inspect.getmembers(Back)
        for back_colour in all_back_colours:
            if isinstance(back_colour[0], str) and back_colour[0] != "__module__":
                self.back_colours[back_colour[0]] = back_colour[1]
        self.back_colours["NORMAL"] = self.back_colours.get("RESET")
        all_styles = inspect.getmembers(Style)
        for style in all_styles:
            if isinstance(style[0], str) and style[0] != "__module__":
                self.styles[style[0]] = style[1]

    def __set_options(self, options) -> None:
        self.__dict__.update({"datetime_format": '%Y/%m/%d @ %H:%M:%S',
                              "datetime_text_divider": ' | ',
                              "datetime_text_divider_style": "NORMAL",
                              "datetime_text_divider_foreground": "NORMAL",
                              "datetime_text_divider_background": "NORMAL",
                              "datetime_background": 'YELLOW',
                              "datetime_foreground": 'BLACK',
                              "datetime_style": 'NORMAL',
                              "log_identifier_foreground": 'GREEN',
                              "log_identifier_background": 'NORMAL',
                              "log_identifier_style": 'NORMAL',
                              "log_message_foreground": 'NORMAL',
                              "log_message_background": 'NORMAL',
                              "log_message_style": 'NORMAL',
                              "log_identifier_message_divider": ': ',
                              "log_dividers_foreground": 'NORMAL',
                              "log_dividers_background": 'NORMAL',
                              "log_dividers_style": 'NORMAL',
                              "warn_identifier_foreground": 'RED',
                              "warn_identifier_background": 'NORMAL',
                              "warn_identifier_style": 'BRIGHT',
                              "warn_message_foreground": 'NORMAL',
                              "warn_message_background": 'NORMAL',
                              "warn_message_style": 'NORMAL',
                              "warn_identifier_message_divider": ': ',
                              "warn_dividers_foreground": 'NORMAL',
                              "warn_dividers_background": 'NORMAL',
                              "warn_dividers_style": 'NORMAL',
                              "error_identifier_foreground": 'BLACK',
                              "error_identifier_background": 'RED',
                              "error_identifier_style": 'BRIGHT',
                              "error_message_foreground": 'RED',
                              "error_message_background": 'NORMAL',
                              "error_message_style": 'NORMAL',
                              "error_identifier_message_divider": ': ',
                              "error_dividers_foreground": 'NORMAL',
                              "error_dividers_background": 'NORMAL',
                              "error_divider_style": 'NORMAL'})
        self.__dict__.update(options)

    def __get_style(self, option) -> str:
        return self.styles.get(self.__dict__.get(option))

    def __get_foreground_colour(self, option) -> str:
        print(option)
        print(self.fore_colours.get(self.__dict__.get(option)))
        return self.fore_colours.get(self.__dict__.get(option))

    def __get_background_colour(self, option) -> str:
        return self.back_colours.get(self.__dict__.get(option))

    def __get_datetime_formatted(self) -> str:
        return f"{self.__get_foreground_colour('datetime_foreground')}{self.__get_background_colour('datetime_background')}{self.__get_style('datetime_style')}{datetime.datetime.now().strftime(self.__dict__.get('datetime_format'))}{self.__get_style('datetime_text_divider_style')}{self.__get_style('datetime_text_divider_foreground')}{self.__get_style('datetime_text_divider_background')}{self.__dict__.get('datetime_text_divider')}{Style.RESET_ALL}"

    def log(self, message) -> None:
        print(f"{self.__get_datetime_formatted()}{Fore.GREEN}{Style.DIM}Log{Style.RESET_ALL}: {message}")

    def warn(self, message) -> None:
        print(f"{self.__get_datetime_formatted()}{Fore.RED}{Style.BRIGHT}Warning{Style.RESET_ALL}: {message}")

    def error(self, message) -> None:
        print(f"{self.__get_datetime_formatted()}{Back.RED}{Fore.BLACK}{Style.BRIGHT}Error{Style.RESET_ALL}: "
              f"{Fore.RED}{message}{Fore.RESET}")


if __name__ != "__main__":
    init()
