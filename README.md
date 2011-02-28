Usage example:
==============

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='railscasts').style
    <class 'pygments_style_railscasts.RailscastsStyle'>


Export the style as CSS:
========================

    pygmentize -S railscasts -f html > railscasts.css


Please read the [official documentation][pygments] for further information
on the usage of pygment styles.


[pygments]: http://pygments.org/docs/
