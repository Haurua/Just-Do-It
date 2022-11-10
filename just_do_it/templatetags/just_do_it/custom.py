from django import template
import datetime

register = template.Library()


@register.filter(name="boolean_val")
def boolean_val(boolean: bool) -> str:
    """Checks boolean value to determine the relevant string output.

    :parameter:
            boolean (object): boolean object to converted to string.
    :returns:
            (str): string representation of the boolean.
    """
    if boolean:
        return "YEP."
    else:
        return "NOPE."


@register.filter(name="date_only")
def date_only(date: datetime) -> str:
    """Remove the time from datetime object, as to display only the date.

    :parameter:
            date (object): datetime object to be string formatted.
    :returns:
            (str): formatted string with only the date.
    """
    return datetime.datetime.strftime(date, "%b, %d. %Y")
