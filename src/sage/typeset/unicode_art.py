# -*- coding: utf-8 -*-
r"""
Unicode Art

This module implements ascii art using unicode characters. It is a
strict superset of :mod:`~sage.typeset.ascii_art`.
"""

#*******************************************************************************
#       Copyright (C) 2013 Jean-Baptiste Priez <jbp@kerios.fr>,
#                     2015 Volker Braun <vbraun.name@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*******************************************************************************

from sage.typeset.character_art import CharacterArt
from sage.typeset.character_art_factory import CharacterArtFactory
import sage.typeset.symbols as symbol


class UnicodeArt(CharacterArt):
    r"""
    An Ascii art object is an object with some specific representation for
    *printing*.

    INPUT:

    - ``lines`` -- the list of lines of the representation of the ascii art
      object

    - ``breakpoints`` -- the list of points where the representation can be
      split

    - ``baseline`` -- the reference line (from the bottom)

    - ``atomic`` -- indicate if the ascii art representation is splittable
      (must be coherent with breakpoints)

    EXAMPLES::

        sage: i = var('i')
        sage: unicode_art(sum(pi^i/factorial(i)*x^i, i, 0, oo))
         pi*x
        e
    """
    _string_type = unicode


_unicode_art_factory = CharacterArtFactory(
    UnicodeArt, unicode, '_unicode_art_',
    (symbol.unicode_left_parenthesis, symbol.unicode_right_parenthesis),
    (symbol.unicode_left_square_bracket, symbol.unicode_right_square_bracket),
    (symbol.unicode_left_curly_brace, symbol.unicode_right_curly_brace),
)


def unicode_art(obj):
    r"""
    Return an unicode art representation

    INPUT:

    - ``obj`` -- anything. The object whose unicode art representation
      we want.

    OUTPUT:
    
    :class:`UnicodeArt` instance.

    EXAMPLES::

        sage: unicode_art(integral(exp(x+x^2)/(x+1), x))
            /
           |
           |   2
           |  x  + x
           | e
           | ------- dx
           |  x + 1
           |
          /

    TESTS::

        sage: n = var('n')
        sage: unicode_art(sum(binomial(2 * n, n + 1) * x^n, n, 0, oo))
         /        __________    \
        -\2*x + \/ -4*x + 1  - 1/
        --------------------------
                   __________
             2*x*\/ -4*x + 1
        sage: unicode_art(list(DyckWords(3)))
        ⎡                                   /\   ⎤
        ⎢            /\    /\      /\/\    /  \  ⎥
        ⎣ /\/\/\, /\/  \, /  \/\, /    \, /    \ ⎦
        sage: ascii_art(1)
        1
    """
    return _unicode_art_factory.build(obj)


empty_unicode_art = _unicode_art_factory.build_empty()

