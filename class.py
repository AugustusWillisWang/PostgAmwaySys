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

    value = []
    num = 1


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
print TABLE.num
