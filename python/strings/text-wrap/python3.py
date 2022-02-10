

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    wrap_string = wrapper.fill(text=string)
    return wrap_string