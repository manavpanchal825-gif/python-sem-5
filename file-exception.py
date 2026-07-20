try :
    f = open("demofile.txt")
    f.write("Lorum ipsum")
except :
    print("Something Went Wrong When Writing To The File")
finally:
    f.close()