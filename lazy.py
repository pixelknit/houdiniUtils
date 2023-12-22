class Lazy:
    def __init__(self, fun, *args, **kwargs):
        self.fun = fun
        self.args = args
        self.kwargs = kwargs
        self.executed = False
        self.value = None

    # Binary Operators
    def __binary__(self, binfun, other):
        def fun(self, other):
            if type(other) == Lazy:
                other = other.__force__()
            return binfun(self.__force__(), other)
        return Lazy(fun, self, other)

    def __add__(self, other):
        return self.__binary__(lambda x,y: x+y, other)

    def __mul__(self, other):
        return self.__binary__(lambda x,y: x*y, other)

    def __sub__(self, other):
        return self.__binary__(lambda x,y: x-y, other)

    def __truediv__(self, other):
        return self.__binary__(lambda x,y: x/y, other)

    def __floordiv__(self, other):
        return self.__binary__(lambda x,y: x//y, other)

    def __mod__(self, other):
        return self.__binary__(lambda x,y: x%y, other)

    def __pow__(self, other):
        return self.__binary__(lambda x,y: x**y, other)

    def __or__(self, other):
        return self.__binary__(lambda x,y: x or y, other)

    def __and__(self, other):
        return self.__binary__(lambda x,y: x and y, other)

    def __xor__(self, other):
        return self.__binary__(lambda x,y: x^y, other)

    def __lshift__(self, other):
        return self.__binary__(lambda x,y: x<<y, other)

    def __rshift__(self, other):
        return self.__binary__(lambda x,y: x>>y, other)

    # Comparisons Operators
    def __lt__(self, other):
        return self.__binary__(lambda x,y: x<y, other)

    def __gt__(self, other):
        return self.__binary__(lambda x,y: x>y, other)

    def __le__(self, other):
        return self.__binary__(lambda x,y: x<=y, other)

    def __ge__(self, other):
        return self.__binary__(lambda x,y: x>=y, other)

    def __eq__(self, other):
        return self.__binary__(lambda x,y: x==y, other)

    def __ne__(self, other):
        return self.__binary__(lambda x,y: x!=y, other)

    # Unary Operators
    def __unary__(self, unfun):
        return Lazy(lambda x : unfun(x.__force__()), self)

    def __bool__(self):
        # __bool__ has to return a boolean --> force needed
        return self.__unary__(bool).__force__()

    def __str__(self):
        # __str__ has to return a string --> force needed
        return self.__unary__(str).__force__()

    def __pos__(self):
        return self.__unary__(lambda x:+x)

    def __neg__(self):
        return self.__unary__(lambda x:-x)

    def __invert__(self):
        return self.__unary__(lambda x:~x)

    def __repr__(self):
        if self.executed:
            val = repr(self.value)
        else:
            val = "_"
        return "Lazy({}) at {}".format(val, hex(id(self)))

    def __force__(self):
        if not self.executed:
            self.value = self.fun(*self.args, **self.kwargs)
            self.executed = True
        return self.value

def lazy(fun_or_val, *args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        # This is a single value, not a function
        lazy_object = Lazy(lambda x:x, fun_or_val)
        lazy_object.__force__()
        return lazy_object
    return Lazy(fun_or_val, *args, **kwargs)

def force(lazy_object):
    if type(lazy_object) != Lazy:
        return lazy_object
    return lazy_object.__force__()

def lazyif(condition, tbranch, fbranch):
    return lazy(lambda x : tbranch if force(x) else fbranch, condition)

def lazyfac(n):
    if n <= 1:
        return lazy(1)
    else:
        return lazyfac(n-1) * n

def lazyfac2(n):
    if n <= 1:
        return lazy(1)
    else:
        return lazy(lambda x : force(lazyfac(x-1) * x), n)
        # Note that it's not important wether we use lazyfac2 or lazyfac here.
        # Upon evaluation it makes no difference wether we defer the construction
        # of the term or not since it is being evaluated.

# sys.setrecursionlimit(5)
