# -*- coding: utf-8 -*-
"""
    railscasts
    ~~~~~~~~~~

    Port of the railscasts color scheme for Vim.

    Based upon the work of Nick Moffitt and Josh O'Rourke.

    :copyright: Copyright 2011 Marcus Fredriksson
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text


class RailscastsStyle(Style):
    """
    Port of the railscasts color scheme for Vim.
    """

    default_style = ''

    background_color = '#222'
    highlight_color = '#e6e1dc'

    styles = {
        Comment:                'italic #bc9458',

        Error:                  '#ffc66d',

        Keyword:                '#cc7833',
        Keyword.Reserved:       '#da4939',
        Keyword.Type:           '#5a647e',

        Name:                   '#fff',
        Name.Attribute:         '#da4939',
        Name.Builtin:           '#6d9cbe',
        Name.Builtin.Pseudo:    '#5a647e',
        Name.Class:             '#ffc66d',
        Name.Constant:          '#6d9cbe',
        Name.Decorator:         '#da4939',
        Name.Function:          '#ffc66d',
        Name.Tag:               '#e8bf6a',

        Number:                 '#a5c261',

        Operator:               '#fff',
        Operator.Word:          '#cc7833',

        Punctuation:            '#fff',

        String:                 '#a5c261',
        String.Escape:          '#da4939',

        Text:                   '#fff',
    }
