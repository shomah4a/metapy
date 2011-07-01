#-*- coding:utf-8 -*-

import sys

from metapy.expressions import Symbol, Literal
from metapy.blocks import For
from metapy.statements import Print, Pass



def test_print():

    Print(Literal('aaa')).next(Print(Literal('bbb'))).execute()
