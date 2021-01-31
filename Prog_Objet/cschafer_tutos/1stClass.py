#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================


def html_tag(tag):
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


html_h2 = html_tag("h2")
html_h2("coucou hey")


html_p = html_tag("p")
html_p("ceci est un paragraphe")