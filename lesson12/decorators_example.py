
def percent(func):
    def inner(*args, **kwargs):
        header, footer = "%"*20, "%"*20
        return f"{header}\n{func(*args,**kwargs)}\n{footer}"
    return inner

def and_symbol(func):
    def inner(*args, **kwargs):
        header, footer = "&"*20, "&"*20
        return f"{header}\n{func(*args,**kwargs)}\n{footer}"
    return inner

def add_footer_header(sign, quantity):
    def midlle_level(func):
        def inner(some_msg):
            footer = sign * quantity
            header = sign * quantity
            return f"{header}\n{func(some_msg)}\n{footer}"
        return inner
    return midlle_level


#@and_symbol
#@percent
@add_footer_header("#", 10)
def hi(msg):
    return "***\n$$$\n" + msg + "\n$$$\n***"

print(hi('hello my fellow friends'))
