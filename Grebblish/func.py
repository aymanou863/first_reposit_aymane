def file_exist_or_not(path) :
    
    if os.path.isfile(path) :
        return True 
    else : 
        return False 
        

def print_fun(x):
    
    try :
        print(x)
    except:
        print("An exception occurred")