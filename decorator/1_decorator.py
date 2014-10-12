
def get_text(name):
    return "hello, {0} dolor sit there".format(name)


'''
in fact decorator is a function which takes func as argument and return another func

'''
def p_dec(func):  # <== pass in function object
    def func_wrapper(name):
        return "<p>{0}</p>".format( func(name) )
    return func_wrapper # <== return function object


my_get_text = p_dec(get_text)
print my_get_text("John")
