#-*- coding:utf-8 -*-

import base
import expressions

import statements


class Block(statements.Statement):
    u'''
    ブロック要素

    :param statements: 複数文
    :param 
    
    '''

    def __init__(self, statements):

        self.statements = statements



    def _make_block(self, env):

        state = self.statements

        if isinstance(state, statements.Statement):
            state = [state]
        

        return '\n'.join(sum((
                    ['    ' + y for y in x._make_string(env).splitlines()]
                    for x in state), []))
        


    def _make_string(self, env):

        head = self._make_head(env)

        return head + '\n' + self._make_block(env)
        



class For(Block):
    u'''
    for 文

    :param var: イテレート変数
    :type var: :py:class:`expressions.Symbol`
    :param iterable: 式
    :type iterable: :py:class:`base.Expression`
    :param statements: 文
    :type statements: :py:class:`base.Statements`
    '''

    
    def __init__(self, var, iterable, statements=statements.Pass()):

        super(For, self).__init__(statements)

        self.var = var
        self.iterable = iterable



    def _make_head(self, env):

        return 'for {0} in {1}:'.format(self.var._make_string(env),
                                        self.iterable._make_string(env))

