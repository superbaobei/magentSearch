# This is a sample Python script.
import sys
print('-' * 40)
print(sys.path)
import ModuleTest
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import fibo
# from com.fib import calFib
#
import fib
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, name=', name)  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fibo.fib2(10)
    fib.calFib(10)
    print_hi('PyCharm')

    sum =0
    for a in range(5,10):
        sum+=a
    else:
        print(sum)

    ModuleTest.ModuleTest.mothod1(213)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
