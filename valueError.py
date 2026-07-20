try :
    print(int('a'))
except ValueError:
    print('caught ValueError Exception')
else :
    print('No Except')