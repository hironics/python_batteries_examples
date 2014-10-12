
'''
after decorator wrapping, i can use functools.wrapp to protect my internal information

'''
from functools import wraps

def tag(tag_name):  # <== it takes an argu, return a decorator
    def tags_dec(func):
        @wraps(func)
        def func_wrapper(name):
            'this is a wrapper'
            return "<{0}>{1}</{0}>".format(tag_name, name)
        return func_wrapper
    return tags_dec    

@tag('div')
def get_text(name):
    'return hello gretting'
    return "hello " + name


print get_text("hiro")    

print "however, the get_text's function name has been changed as well"
print get_text.__name__
print get_text.__doc__

