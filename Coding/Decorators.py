def dec1(fun1):
    def nowexecute():
         fun1()
         print("Harry")
    return nowexecute         
@dec1
def func2():
    print("hello")
func2()        