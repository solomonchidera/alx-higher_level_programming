#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    while x > 0:
        try:
            print("{}".format(my_list[count]), end="")
            count += 1
            x -= 1
        except (IndexError, ValueError, TypeError):
            pass
        except Exception:
            print("Catch all")
        finally:
            print("")
    return count