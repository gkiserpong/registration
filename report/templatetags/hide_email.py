from django import template


def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    #if not nofail and index not in range(len(s)):
    #    raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return s[int(len(s)/2)] + newstring
    if index > len(s):  # add it to the end
        return s[int(len(s)/2)] + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring

# Filter
register = template.Library()

@register.filter
def hide_email(value):
    v_part = value.split('@')
    #v_index = len(v_part[0]) - 5
    v_index = 5
    v_new = replacer(v_part[0], "*****", v_index)
    return v_new + "@" + v_part[1]