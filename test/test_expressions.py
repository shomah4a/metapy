#-*- coding:utf-8 -*-

import sys

from metapy.expressions import Symbol, Literal
from metapy.blocks import For
from metapy.statements import Print, Pass



def test_expressions():

    op = Literal(10) * Symbol('aaa')

    print op._make_string({})
    
    assert op._make_string({}) == '10 * aaa'

    it = Symbol('it')
    it2 = Symbol('it2')

    p = Print(it * it2)
    
    f = For(it, Literal(range(10)), p)

    f2 = For(it2, Literal(range(5)), f)
    
    print f2._make_string({})

    f2.execute()



def test_expression2():

    aa = 10

    assert (Literal(10) * Symbol('aa')).evaluate() == 100



