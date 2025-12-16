

def fun(uname,passw):
    if(s_uname==uname and s_pass == passw):
        return True
    else:
        return False
    
s_uname = "Manoj"
s_pass = "Thaniya"

uname= str(input())
passw= str(input())

print(fun(uname,passw))


# a = int(input())
# b =  int(input())
# c =  int(input())

# def add():
#     return (a+b)*c
# ans = add()
# print(ans)
