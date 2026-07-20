try :
    f = open('Somefile.txt','r')
    print(f.read())
    f.close()
except IOError:
    print('File Not Found')
    