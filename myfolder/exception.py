# try:
#     a= int(input())
#     b= int(input())
#     print(a+b)
# except Exception:
#     print("wrrong input")

try:
    a= int(input())
    b= int(input())
    print(a+b)
except Exception as e :
    print("wrrong input",e)
finally:
    print("done")