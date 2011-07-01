#-*- coding:utf-8 -*-

import base



class Statement(base.Element):
    u'''
    文
    '''

    def next(self, st):

        return StatementList([self, st])



class StatementList(Statement):


    def __init__(self, stlist):

        self.statements = stlist


    def next(self, st):

        return StatementList(self.statements+[st])


    def _make_string(self, env):

        return '\n'.join([x._make_string(env) for x in self.statements])
        



class Print(Statement):
    u'''
    print 文

    :param exps: 式
    :type exps: [:py:class:`base.Expression`]

    :param output: 出力先
    :param output: :py:class:`base.Expression`
    '''

    def __init__(self, *args, **argd):

        self.exps = args
        self.output = argd.get('file')



    def _make_string(self, env):

        tgt = ','.join(x._make_string(env) for x in self.exps)

        if self.output is not None:
            return 'print >> {0}, {1}'.format(self.output._make_string(env),
                                              tgt)
        else:
            return 'print {0}'.format(tgt)
    


class Pass(Statement):
    u'''
    なにもしない
    '''


    def _make_string(self, env):

        return 'pass'

