import re

'''
all functions:
p.match
p.search
p.findall
p.finditer

p.split
p.sub

'''

p = re.compile('\d{2}')

content = file('/etc/motd','r').read()

print 'findall :'
print p.findall(content)

print '**replace**'
print p.sub('--', content)

''' split has two functions
    1. without group 
    2. with group
'''
print "split**"
print p.split(content)  #include only splitted values

p = re.compile('(\d{2})')
print p.split(content)  #include both splited and delimiters
