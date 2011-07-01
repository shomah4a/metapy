#-*- coding:utf-8 -*-


import sys


def make_environ(globals, locals):

    frame = sys._getframe()

    if globals is None:
        globals = frame.f_back.f_back.f_globals

    if locals is None:
        locals = frame.f_back.f_back.f_locals


    return globals, locals



class Element(object):
    u'''
    構文オブジェクト
    '''

    def evaluate(self, globals=None, locals=None):

        g, l = make_environ(globals, locals)

        return eval(self._make_string({}), g, l)


    def execute(self, globals=None, locals=None):

        g, l = make_environ(globals, locals)

        exec self._make_string({}) in g, l





