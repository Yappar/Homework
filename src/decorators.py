import logging


def log(filename=None):
    """Декоратор должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)
    (если в параметрах декоратора указан файл)"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if filename is not None:
                logging.basicConfig(
                    filename=filename,
                    level=logging.DEBUG,
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s",
                )
                try:
                    func(*args, **kwargs)
                    logging.debug(f"{func.__name__} is ok")
                except Exception:
                    logging.debug(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")
            elif filename is None:
                try:
                    func(*args)
                    print(f"{func.__name__} is ok")
                except Exception:
                    print(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")

        return wrapper

    return my_decorator


"""Проверяем работу декоратора"""


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


#
# my_function(1,"3")
# # #
# # my_function ok
# #
# # my_function error: "тип ошибки". Inputs: (1, 2), {}
#
# # print(my_function(1, 2))
