import re

'''
python learns regular expression from perl. it utilize everything from re module

This module divides functions into 2 levels:
    1. module level function
    2. object and object.method

'''

p = re.compile('Wel.*')

content = file('/etc/motd','r').read()

print 'match object'
res = p.match(content)
print res

print 'module level object'
print re.match('Wel.*', content)
