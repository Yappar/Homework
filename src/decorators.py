import logging


def log(filename=None):  # "../logs/masks.log"
    """Декоратор должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль)
    (если в параметрах декоратора указан файл)"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if filename is not None:
                logging.basicConfig(
                    filename=filename,
                    level=logging.DEBUG,
                    filemode="w",
                    format="%(asctime)s %(name)s %(levelname)s %(funcName)s %(message)s",
                )
                try:
                    func(*args)
                    result = func(*args, **kwargs)
                    logging.debug(f"{func.__name__} is ok, result is {result}")
                    return result
                except Exception:
                    logging.debug(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")
            elif filename is None:
                try:
                    func(*args)
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} is ok, result is {result}")
                except Exception:
                    print(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")
            return None

        return wrapper

    return my_decorator


"""Проверяем работу декоратора"""

if __name__=='__main__':
    @log("C:\\Users\\yappa\\Homework\\src\\mylog.txt")
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    print(my_function(1, 2))
# my_function ok
# my_function error: "тип ошибки". Inputs: (1, 2), {}
