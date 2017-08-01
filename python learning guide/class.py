'''
A practice on how to write class
AW
2017.6.24
'''

from __future__ import division
# from types import MethodType

# def __doc__():
# print("doc")


class TABLE(object):
    '''
    You call this a doc?
    '''

    def __doc__(self):
        print'nodocisthebestdoc'

    def __init__(self, name, key="nokey", calc=2):
        self.name = name
        self.key = key
        self.pow = pow(calc, 2)

    def show(self):
        '''
        doc
        '''
        print "Show name:%s key:%s" % (self.name, self.key)

    def changename(self, name):
        '''
        one line is not enough
        '''
        if isinstance(name, str):
            self.name = name
        else:
            print "name should be str"

    value = 1
    numlist = []

    @property
    def getvalue(self):
        '''no note'''
        print'get value in %s : get %s' % (__name__, self.value)
        return self.value

    @getvalue.setter
    def getvalue(self, value):
        '''
        fuck
        '''
        self.value = value


class Listplus(object):
    '''
    none
    '''

    def __init__(self, *args, **kw):
        self.value = list(*args)
        self.remark = list(*args)
        # self.remark = list()
        print args
        print kw

    def setremark(self, remarkname, *args, **kw):
        '''just set'''
        setattr(self, remarkname, list(*args))
        print args
        print kw

    '''    def check(self):
        # check if len(self.value) == len(self.remark)
        return len(self.value) == len(self.remark)'''

    def show(self):
        '''
        show all the value and remarks in the listplus
        '''
        if len(self.value) == len(self.remark):
            for i in range(len(self.value)):
                print self.value[i]
                print self.remark[i]
        else:
            pass

    __slots__ = ('addon', 'value', 'remark')


# driver
TABLE = TABLE('a', 'b',)
TABLE.changename("poi")
print TABLE.pow
TABLE.show()
print dir(TABLE)
print getattr(TABLE, "__doc__", "1")
# TABLE.__doc__()
print TABLE.numlist
# TABLE.value
# TABLE.value=2
print TABLE.value
print TABLE.getvalue


class New(object):
    '''6.26'''

    def __init__(self):
        self.name = 1

    def __str__(self):
        return 'poi'

    __repr__ = __str__


class Fib(object):
    '''gen and more with fib'''

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000000:
            raise StopIteration()
        return self.a
    def __call__(self):
        print 'call fib directly'

    def __getitem__(self,inp):
        i=1
        aa=0
        bb=1
        while(i<inp):
            aa,bb=bb,aa+bb
            i=i+1
        return aa
        
    # def __getattribute__(self,n):
    #     if n=="poi":
    #         return "poi?"
    #         raise StandardError
    #     else:
    #         print "please input poi"

x=Fib()
for i in x:
    print i 

print x[5]
x()
