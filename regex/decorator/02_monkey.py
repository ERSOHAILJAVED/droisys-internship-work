# monkey patching in the class

class Test:
    def class_method(self):
        print('function from class')


def noraml_func():
    print('normal function is calling')

Test().class_method()
noraml_func()

# monkey patch
Test().class_method=noraml_func
# dynamical function is changed
Test().class_method()
