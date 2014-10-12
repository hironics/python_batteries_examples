'''
closure is a combination of function code and its scope.
we want a function to retain a value when it was created even though the scope cease to exist. This technique of using the values of outer parameters within a dynamic function is another way of defining the closure.

'''
def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

f = startAt(10)
g = startAt(100)

print f(1), g(2)

print f, f.__closure__, f.__closure__[0]
print dir(f.__closure__[0])
print f.__closure__[0].cell_contents
