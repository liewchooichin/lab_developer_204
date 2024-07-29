# You have error messages that include the name of the 
# function emitting them. To copy such messages to other
# functions, you have to edit them each time, unless you
# can automatically find the name of the current function.

import sys

def hello_world():
    """Info about the function"""
    this_function_name = sys._getframe(  ).f_code.co_name
    print(f"{this_function_name=}")
    this_line_number = sys._getframe(  ).f_lineno
    print(f"{this_line_number=}")
    this_filename = sys._getframe(  ).f_code.co_filename
    print(f"{this_filename=}")

def whoami(  ):
    """This calling sys._getframe(1), you can get this information
    for the caller of the current function."""
    current_function = sys._getframe().f_code.co_name
    print(f"{current_function=}")
    return sys._getframe(1).f_code.co_name

def callersname(  ):
    """is calls sys._getframe with argument 1, because the 
    call to whoami is now frame 0."""
    current_function = sys._getframe().f_code.co_name
    print(f"{current_function=}")
    return sys._getframe(2).f_code.co_name

def main():
    """Main"""
    hello_world()

    calling_function = whoami()
    print(f"{calling_function=}")

    her = callersname()
    print(f"{her=}")


if __name__=="__main__":
    main()
