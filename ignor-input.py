try :
    print('Press Return Or Ctrl+C:')
    ignore = input()
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt')
else :
    print('NO Exception')
    