import datetime


now = datetime.datetime.now()


def Clock():
    print(now.strftime("%X"))


def Date():
    print(now.strftime("%d ""%B ""%Y"))
    
Clock()
