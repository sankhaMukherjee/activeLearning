import argparse

def sayHello(name=None):
    '''a function that says Hello
    
    Parameters
    ----------
    name : str or ``None``, optional
        This is the name that someone is going to greet you with, 
        by default ``None`` in which case, this is going to return
        the string ``'Hello World'``
    
    Returns
    -------
    str
        string to be returned
    '''

    if name is None:
        return f'Hello World'
    else:
        return f'Hello {name}'

    

def main():

    parser = argparse.ArgumentParser(prog ='activeLearning', 
                                     description ='Some basic definition for the package.')
    args = parser.parse_args()

    print('Arguments passed to the parser:')
    print(args)

    sayHello()

    return