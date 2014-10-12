from datetime import datetime
def log_start(func):
    def func_wrapper(*argc, **argv):
        print datetime.now() ," calling ", func.__name__
        func(*argc, **argv)
    return func_wrapper

@log_start
def hello(name):
    print "hello "+name

@log_start
def hostname():
    import os
    print os.listdir('/etc/')[:5]


hello('hiro')
hostname()
