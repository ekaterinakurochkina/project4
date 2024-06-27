from functools import wraps


def logging(filename=None):
    """Декоратор, который логирует вызов функции и ее результат
    в файл mylog.txt или в консоль"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename != None:
                    with open(filename, "a") as mylog:
                        mylog.write(f"{func, __name__} ok\n")
                elif filename == None:
                    print(f"{func, __name__} ok")
                return result
            except Exception as e:
                with open(filename, "a") as mylog:
                    (mylog.write(f"{func,__name__} error:{e}. Inputs: {args}, {kwargs}\n"))
                raise e

        return wrapper

    return decorator


@logging(filename="mylog.txt")
def my_function(x, y):
    """Функция сложения двух чисел"""
    return x + y


# проверка работы функции
print(my_function(2, 3))
