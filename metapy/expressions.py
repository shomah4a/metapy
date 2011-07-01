#-*- coding:utf-8 -*-

import base

import statements



class Expression(statements.Statement):
    u'''
    式
    '''



def __makeop():


    def make_operation(op):

        def operation(self, other):

            if not isinstance(other, Expression):
                other = Literal(other)

            return Binary(self, Operator(op), other)

        return operation



    def make_roperation(op):

        def operation(self, other):

            if not isinstance(other, Expression):
                other = Literal(other)

            return Binary(other, Operator(op), self)

        return operation


    def make_single(op):

        def operation(self):

            return Unary(Operator(op), self)
    

    compare = [
        ('lt', '<'),
        ('le', '<='),
        ('eq', '=='),
        ('ne', '!='),
        ('gt', '>'),
        ('ge', '>=')
        ]


    arismethic = [
        ('add', '+'),
        ('sub', '-'),
        ('mul', '*'),
        ('div', '/'),
        ('floordiv', '//'),
        ('mod', '%'),
        ('pow', '**'),
        ('lshift', '<<'),
        ('rshift', '>>'),
        ('and', '&'),
        ('xor', '^'),
        ('or', '|'),
        ]

    single = [
        ('neg', '-'),
        ('pos', '+'),
        ('invert', '~'),
        ]

    for m, op in compare+arismethic:

        n = '__{0}__'.format(m)

        setattr(Expression, n, make_operation(op))


    for m, op in compare+arismethic:

        n = '__r{0}__'.format(m)

        setattr(Expression, n, make_roperation(op))


__makeop()



class Paren(Expression):
    u'''
    括弧
    '''

    def __init__(self, exp):

        self.expression = exp




class Operator(base.Element):
    u'''
    オペレータ
    '''

    def __init__(self, symbol):
        u'''
        演算子
        '''

        self.symbol = symbol


    def _make_string(self, env):

        return self.symbol




class Binary(Expression):
    u'''
    二項演算

    :param lop: 左辺
    :type lop: :py:class:`base.Expression`
    :param op: 演算子
    :type op: :py:class:`Operator`
    :param rop: 右辺
    :type rop: :py:class:`base.Expression`
    
    '''


    def __init__(self, lval, op, rval):

        self.lval = lval
        self.op = op
        self.rval = rval



    def _make_string(self, env):
        u'''
        文字列を作る
        '''

        return u'{0} {1} {2}'.format(self.lval._make_string(env),
                                     self.op._make_string(env),
                                     self.rval._make_string(env))


class Unary(Expression):
    u'''
    単項演算

    :param op: 演算子
    :type op: :py:class:`Operator`
    :param val: 演算対象
    :type val: :py:class:`Expression`
    '''


    def __init__(self, op, val):

        self.operator = op
        self.value = val



    def _make_string(self, env):

        return u'{0} {1}'.format(self.operator._make_string(env),
                                 self.value._make_string(env))

        
        


class Literal(Expression):
    u'''
    即値
    
    :param value: 値
    '''

    def __init__(self, value):

        self.value = value


    def _make_string(self, env):

        return repr(self.value)



class Symbol(Expression):
    u'''
    変数とか

    :param name: シンボル名
    '''

    def __init__(self, name):

        self.name = name


    def _make_string(self, env):

        return self.name




