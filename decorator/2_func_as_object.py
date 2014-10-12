#!/usr/bin/env python

'''

examples on why function is just an object in python

'''

def greet(name):
    
    return "Hello "+ name


def greet2(name):
    '''
    define function inside another funciton
    '''
    def get_message():
        return "hello "
    result = get_message() + name
    return result

def call_func(func):
    other_nme = "john"
    return func(other_name)


print 'assign function to func'
func = greet

print 'call function'
print func('hiro')



