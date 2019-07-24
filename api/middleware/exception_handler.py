
def exceptionhander(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            print('ERROR - ', method.__name__, ' - ', str(e))
    return wrapper