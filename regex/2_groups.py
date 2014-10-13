import re

'''

'''
'''
named group: ?P<name>
non captured group: ?:
group(0): full RE, no actuall group
'''
p = re.compile('(?P<num>\d{2,3})(?:\D)') #only one group

content = file('/etc/motd','r').read()

print 'search object'
res = p.search(content)
print res
print res.groups() #groups return the number of groups in regular express
print res.group(0) #group 0 always exists, matching the whole string
print res.group(1) #group can be called from group number
print res.group('num') #group can also be called from group name

print p.findall(content) #findall will return all searched item

