#!/usr/bin/env python

#
# PyMeld is released under the terms of the MIT License:
#
# Copyright (c) 2002-2009 Entrian Solutions Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

r"""A simple, lightweight system for manipulating HTML (and XML, informally)
using a Pythonic object model.  `PyMeld` is a single Python module,
_PyMeld.py_.    This beta version requires Python 2.2 or above, but the
final production version may work with previous releases of Python (with
slightly limited features) if there's sufficient demand.

*Features:*

 o Allows program logic and HTML to be completely separated - a graphical
   designer can design the HTML in a visual HTML editor, without needing to
   deal with any non-standard syntax or non-standard attribute names.  The
   program code knows nothing about XML or HTML - it just deals with objects
   and attributes like any other piece of Python code.

 o Designed with common HTML-application programming tasks in mind.
   Populating an HTML form with a record from a database is a one-liner
   (using the `%` operator - see below).  Building an HTML table from a set
   of records is just as easy, as shown in the example below.

 o No special requirements for the HTML/XML (or just one: attribute values
   must be quoted) - so you can use any editor, and your HTML/XML doesn't
   need to be strictly valid.

 o Works by string substitution, rather than by decomposing and rebuilding the
   markup, hence has no impact on the parts of the page you don't manipulate.

 o Does nothing but manipulating HTML/XML, hence fits in with any other Web
   toolkits you're using.

 o Tracebacks always point to the right place - many Python/HTML mixing
   systems use exec or eval, making bugs hard to track down.


*Quick overview*

A `PyMeld.Meld` object represents an XML document, or a piece of one.
All the elements in a document with `id=name` attributes are made available
by a Meld object as `object.name`.  The attributes of elements are available
in the same way.  A brief example is worth a thousand words:

>>> from PyMeld import Meld
>>> xhtml = '''<html><body>
... <textarea id="message" rows="2" wrap="off">Type your message.</textarea>
... </body></html>'''
>>> page = Meld(xhtml)                # Create a Meld object from XHTML.
>>> print page.message                # Access an element within the document.
<textarea id="message" rows="2" wrap="off">Type your message.</textarea>
>>> print page.message.rows           # Access an attribute of an element.
2
>>> page.message = "New message."     # Change the content of an element.
>>> page.message.rows = 4             # Change an attribute value.
>>> del page.message.wrap             # Delete an attribute.
>>> print page                        # Print the resulting page.
<html><body>
<textarea id="message" rows="4">New message.</textarea>
</body></html>

So the program logic and the HTML are completely separated - a graphical
designer can design the HTML in a visual XHTML editor, without needing to
deal with any non-standard syntax or non-standard attribute names.  The
program code knows nothing about XML or HTML - it just deals with objects and
attributes like any other piece of Python code.  Populating an HTML form with
a record from a database is a one-liner (using the `%` operator - see below).
Building an HTML table from a set of records is just as easy, as shown in the
example below:


*Real-world example:*

Here's a data-driven example populating a table from a data source, basing the
table on sample data put in by the page designer.  Note that in the real world
the HTML would normally be a larger page read from an external file, keeping
the data and presentation separate, and the data would come from an external
source like an RDBMS.  The HTML could be full of styles, images, anything you
like and it would all work just the same.

>>> xhtml = '''<html><table id="people">
... <tr id="header"><th>Name</th><th>Age</th></tr>
... <tr id="row"><td id="name">Example name</td><td id="age">21</td></tr>
... </table></html>'''
>>> doc = Meld(xhtml)
>>> templateRow = doc.row.clone()  # Take a copy of the template row, then
>>> del doc.row                    # delete it to make way for the real rows.
>>> for name, age in [("Richie", 30), ("Dave", 39), ("John", 78)]:
...      newRow = templateRow.clone()
...      newRow.name = name
...      newRow.age = age
...      doc.people += newRow
>>> print re.sub(r'</tr>\s*', '</tr>\n', str(doc))  # Prettify the output
<html><table id="people">
<tr id="header"><th>Name</th><th>Age</th></tr>
<tr id="row"><td id="name">Richie</td><td id="age">30</td></tr>
<tr id="row"><td id="name">Dave</td><td id="age">39</td></tr>
<tr id="row"><td id="name">John</td><td id="age">78</td></tr>
</table></html>

Note that if you were going to subsequently manipulate the table, using
PyMeld or JavaScript for instance, you'd need to rename each `row`, `name`
and `age` element to have a unique name - you can do that by assigning
to the `id` attribute but I've skipped that to make the example simpler.

As the example shows, the `+=` operator appends content to an element -
appending `<tr>` elements to a `<table>` in this case.


*Shortcut: the % operator*

Using the `object.id = value` syntax for every operation can get tedious, so
there are shortcuts you can take using the `%` operator.  This works just like
the built-in `%` operator for strings.  The example above could have been
written like this:

>>> for name, age in [("Richie", 30), ("Dave", 39), ("John", 78)]:
...      doc.people += templateRow % (name, age)

The `%` operator, given a single value or a sequence, assigns values to
elements with `id`s in the order that they appear, just like the `%` operator
for strings.  Note that there's no need to call `clone()` when you're using
`%`, as it automatically returns a modified clone (again, just like `%` does
for strings).  You can also use a dictionary:

>>> print templateRow % {'name': 'Frances', 'age': 39}
<tr id="row"><td id="name">Frances</td><td id="age">39</td></tr>

The `%` operator is really useful when you have a large number of data items
- for example, populating an HTML form with a record from an RDBMS becomes a
one-liner.

Note that these examples are written for clarity rather than performance, and
don't necessarily scale very well - using `+=` to build up a result in a loop
is inefficient, and PyMeld's `%` operator is slower than Python's built-in
one.  See `toFormatString()` in the reference manual for ways to speed up this
kind of code.


*Element content*

When you refer to a named element in a document, you get a Meld object
representing that whole element:

>>> page = Meld('<html><span id="x">Hello world</span></html>')
>>> print page.x
<span id="x">Hello world</span>

If you just want to get the content of the element as string, use the
`_content` attribute:

>>> print page.x._content
Hello world

You can also assign to `_content`, though that's directly equivalent to
assigning to the tag itself:

>>> page.x._content = "Hello again"
>>> print page
<html><span id="x">Hello again</span></html>
>>> page.x = "Goodbye"
>>> print page
<html><span id="x">Goodbye</span></html>

The only time that you need to assign to `_content` is when you've taken a
reference to an element within a document:

>>> x = page.x
>>> x._content = "I'm back"
>>> print page
<html><span id="x">I'm back</span></html>

Saying `x = "I'm back"` would simply re-bind `x` to the string `"I'm back"`
without affecting the document.


*Version and license*

This is version 2.1.4 of _PyMeld.py_, Copyright (c) 2002-2009 Entrian
Solutions.  It is Open Source software released under the terms of the MIT
License.
"""

__version__ = "2.1.4"
__author__ = "Richie Hindle <richie@entrian.com>"


import sys, string, re
from types import StringType, UnicodeType

# Entrian.Coverage: Pragma Stop
try:
    True, False, bool
except NameError:
    True = 1
    False = 0
    def bool(x):
        return not not x
# Entrian.Coverage: Pragma Start

# Regular expressions for tags and attributes.
openTagRE = re.compile(r"""(?ix)                 # Case-insensitive, verbose
    <(?P<tag>[-a-z0-9_:.]+)                      # Tag opens; capture its name
    (?:\s+[-a-z0-9_:.]+=(?P<quote1>["']).*?(?P=quote1))*   # Attributes
    \s*/?>                                       # Tag closes
    """)

openIDTagRE = r"""(?ix)                          # Case-insensitive, verbose
    <(?P<tag>[-a-z0-9_:.]+)                      # Tag opens; capture its name
    (?:\s+[-a-z0-9_:.]+=(?P<quote1>["']).*?(?P=quote1))* # Attributes before id
    \s+id=(?P<quote2>["'])(?P<id>%s)(?P=quote2)  # The 'id' tag
    (?:\s+[-a-z0-9_:.]+=(?P<quote3>["']).*?(?P=quote3))* # Attributes after id
    \s*/?>                                       # Tag closes
    """

attributeRE = r"""(?ix)
   (?P<space>\s+)
   (?P<name>%s)=(?P<quote>["'])(?P<value>.*?)(?P=quote)
   """

idRE = re.compile(r"""(?i)\s+id=(?P<quote>["'])(?P<id>.*?)(?P=quote)""")


def _findIDMatch(id, text):
    """Work around a possible RE bug:
    > m = re.search(r"<\w+(?:\s\w+='.*?')*\sid='x'>", "<A a='b'><B c='d' id='x'>")
    > m.span()
    (0, 25)
    """

    # To repeat the bug: return re.search(openIDTagRE % id, text)
    # The fix: check whether you can match again, *within* the original match.
    thisRE = openIDTagRE % id
    start = 0
    match = re.search(thisRE, text)
    prevMatch = match
    while match:
        prevMatch = match
        start = prevMatch.span()[0] + 1
        match = re.search(thisRE, '.' * start + text[start:prevMatch.end()])
    return prevMatch


class _MarkupHolder:
    """Keeps hold of the markup string, so that it can be shared between
    multiple Meld objects."""
    def __init__(self, s):
        self.count = 0
        self.s = s

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if name == 's':
            self.__dict__['count'] = self.count + 1


READ_ONLY_MESSAGE = "You can't modify this read-only Meld object"
class ReadOnlyError(Exception):
    """Raised if you try to modify a readonly Meld object."""
    pass


class Meld:
    """Represents an XML document, or a fragment of one.  Pass XML/XHTML
    source to the constructor.  You can then access all the elements with
    `id="name"` attributes as `object.name`, and all the attributes of the
    outermost element as `object.attribute`."""

    def __init__(self, source,
                 readonly=False, replaceUnderscoreWithDash=False):
        """Creates a `Meld` from XML source.  `readonly` does what it
        says.  replaceUnderscoreWithDash lets you write code like this:
        
        >>> html = '<html><div id="header-box">xxx</div></html>'
        >>> meld = Meld(html, replaceUnderscoreWithDash=True)
        >>> meld.header_box = "Yay!"
        >>> print meld.header_box
        <div id="header-box">Yay!</div>
        >>> del meld.header_box
        >>> print meld
        <html></html>
        """

        # Store the options and the markup.
        self._readonly = readonly
        self._dashes = replaceUnderscoreWithDash
        if source is not None:
            # This is a container-style Meld, representing the whole thing.
            if isinstance(source, StringType) or isinstance(source, UnicodeType):
                self._markup = _MarkupHolder(source)
                self._lastUpdate = -1
                self._name = None
                # No call to `self._updatePositions()` 'cos it's done lazily.
            else:
                raise TypeError, "Melds must be constructed from strings"

    def _makeChild(self, name, start):
        """Alternative constructor for internal use: makes a child Meld
        for a named element.  `start` is a shortcut - everywhere where this
        is used, we've already found the starting position of the child
        element as a side effect of determining that the element exists."""

        newObject = Meld(None, self._readonly, self._dashes)
        newObject._markup = self._markup
        newObject._lastUpdate = -1
        newObject._name = name
        newObject._updatePositions(start)
        return newObject

    def _updatePositions(self, start=None):
        """Finds the start and end positions of the start and end tag in
        the markup.  If the caller happens to know where the start tag starts,
        he can pass it in to save time."""

        if self._lastUpdate == self._markup.count:
            return

        # Find the start tag.
        if self._name is None:
            # This is a container-style Meld, representing the whole thing.
            # Look for the first opening element - we'll treat that as the
            # defining element, in the absence of an `id`.
            match = re.search(openTagRE, self._markup.s)
            if not match:
                raise ValueError, "This isn't any form of markup I recognize"
            self._tagName = match.group('tag')
            self._openStart = match.start()
            self._openEnd = match.end()
        else:
            # Find the start tag.
            if start is None:
                match = _findIDMatch(self._name, self._markup.s)
                self._tagName = match.group('tag')
                self._openStart = match.start()
                self._openEnd = match.end()
            else:
                match = re.search(openTagRE, self._markup.s[start:])
                self._tagName = match.group('tag')
                self._openStart = start + match.start()
                self._openEnd = start + match.end()

        # Now find the end tag in the rest of the HTML.  Most of this code
        # deals with nested tags - counting up nested opening tags and
        # counting down the closing tags until it gets to zero.
        rest = self._markup.s[self._openEnd:]
        depth = 1
        pos = 0
        while 1:
            openMatch = re.search('(?i)<%s(>|\s)' % self._tagName, rest[pos:])
            closeMatch = re.search('(?i)</%s>' % self._tagName, rest[pos:])
            if not closeMatch:
                # There's no matching closing tag.
                self._closeStart = self._closeEnd = self._openEnd
                break

            elif not openMatch:
                if depth == 1:
                    # We've found the matching closing tag.
                    self._closeStart = self._openEnd + pos + closeMatch.span()[0]
                    self._closeEnd = self._openEnd + pos + closeMatch.span()[1]
                    break
                else:
                    # We've found a closing tag, but it's for a nested opening tag.
                    depth = depth - 1
                    pos = pos + closeMatch.span()[1]

            elif openMatch.span()[0] < closeMatch.span()[0]:
                # We've found a nested opening tag.
                depth = depth + 1
                pos = pos + openMatch.span()[1]

            else: # closeMatch.span()[0] < openMatch.span()[0]
                depth = depth - 1
                if depth == 0:
                    # We've found the matching closing tag.
                    self._closeStart = self._openEnd + pos + closeMatch.span()[0]
                    self._closeEnd = self._openEnd + pos + closeMatch.span()[1]
                    break
                else:
                    # We've found a closing tag but it's for a nested opening tag.
                    pos = pos + closeMatch.span()[1]

        self._lastUpdate = self._markup.count

    def _findElementFromID(self, nodeID):
        """Returns the start position of the element with the given ID,
        or None."""
        self._updatePositions()

        # For the outermost element, include that element (otherwise you
        # couldn't access it by ID).  For all other elements, don't do that,
        # because you couldn't access nested elements with the same name.
        if self._name is None:
            start = self._openStart
            subset = self._markup.s[start:self._closeEnd]
        else:
            start = self._openEnd
            subset = self._markup.s[start:self._closeStart]
        match = _findIDMatch(nodeID, subset)
        if match:
            return start + match.start()
        else:
            return None

    def _quoteAttribute(self, value):
        """Minimally quotes an attribute value, using `&quot;`, `&amp;`,
        `&lt;` and `&gt;`."""
        value = value.replace('"', '&quot;')
        value = value.replace('<', '&lt;').replace('>', '&gt;')
        value = re.sub(r'&(?![a-zA-Z0-9]+;)', '&amp;', value)
        return value

    def _unquoteAttribute(self, value):
        """Unquotes an attribute value quoted by `_quoteAttribute()`."""
        value = value.replace('&quot;', '"').replace('&amp;', '&')
        return value.replace('&lt;', '<').replace('&gt;', '>')

    def __getattr__(self, name):
        """`object.<name>`, if this Meld contains an element with an `id`
        attribute of `name`, returns a Meld representing that element.

        Otherwise, `object.<name>` returns the value of the attribute with
        the given name, as a string.  If no such attribute exists, an
        AttributeError is raised.

        `object._content` returns the content of the Meld, not including
        the enclosing `<element></element>`, as a string.

        >>> p = Meld('<p style="one">Hello <b id="who">World</b></p>')
        >>> print p.who
        <b id="who">World</b>
        >>> print p.style
        one
        >>> print p._content
        Hello <b id="who">World</b>
        >>> print p.who._content
        World
        """

        if name == '_content':
            self._updatePositions()
            return self._markup.s[self._openEnd:self._closeStart]
        elif name[0] == '_':
            try:
                return self.__dict__[name]
            except KeyError:
                raise AttributeError, name
        if self._dashes:
            name = string.replace(name, '_', '-')
        self._updatePositions()
        start = self._findElementFromID(name)
        if start is not None:
            return self._makeChild(name, start)
        openTag = self._markup.s[self._openStart:self._openEnd]
        match = re.search(attributeRE % name, openTag)
        if match:
            return self._unquoteAttribute(match.group('value'))
        else:
            raise AttributeError, "No element or attribute named %r" % name

    def __setattr__(self, name, value):
        """`object.<name> = value` sets the XML content of the element with an
        `id` of `name`, or if no such element exists, sets the value of the
        `name` attribute on the outermost element.  If the attribute is not
        already there, a new attribute is created.

        >>> p = Meld('<p style="one">Hello <b id="who">World</b></p>')
        >>> p.who = "Richie"
        >>> p.style = "two"
        >>> p.align = "center"
        >>> p.who.id = "newwho"
        >>> print p
        <p align="center" style="two">Hello <b id="newwho">Richie</b></p>
        """

        if name[0] == '_' and name != '_content':
            self.__dict__[name] = value
            return
        if self._readonly:
            raise ReadOnlyError, READ_ONLY_MESSAGE
        if self._dashes:
            name = string.replace(name, '_', '-')
        self._updatePositions()
        if not isinstance(value, StringType) or isinstance(value, UnicodeType):
            value = str(value)
        if name == '_content':
            self._markup.s = self._markup.s[:self._openEnd] + \
                             value + \
                             self._markup.s[self._closeStart:]
            return
        start = self._findElementFromID(name)
        if start is not None:
            child = self._makeChild(name, start)
            if self._markup.s[child._openStart:child._closeEnd] == value:
                return   # `x.y = x.y`, as happens via `x.y += z`
            self._markup.s = self._markup.s[:child._openEnd] + \
                             value + \
                             self._markup.s[child._closeStart:]
        else:
            # Set the attribute value.
            openTag = self._markup.s[self._openStart:self._openEnd]
            attributeMatch = re.search(attributeRE % name, openTag)
            escapedValue = self._quoteAttribute(value)
            if attributeMatch:
                # This is a change to an existing attribute.
                attributeStart, attributeEnd = attributeMatch.span()
                quote = attributeMatch.group('quote')
                newOpenTag = openTag[:attributeStart] + \
                             '%s%s=%s%s%s' % (attributeMatch.group('space'),
                                               attributeMatch.group('name'),
                                               quote, escapedValue, quote) + \
                             openTag[attributeEnd:]
                self._markup.s = self._markup.s[:self._openStart] + \
                                 newOpenTag + \
                                 self._markup.s[self._openEnd:]
            else:
                # This is introducing a new attribute.
                newAttributePos = self._openStart + 1 + len(self._tagName)
                newAttribute = ' %s="%s"' % (name, escapedValue)
                self._markup.s = self._markup.s[:newAttributePos] + \
                                 newAttribute + \
                                 self._markup.s[newAttributePos:]
        if string.lower(name) == 'id':
            self._name = value

    def __delattr__(self, name):
        """Deletes the named element or attribute from the `Meld`:

        >>> p = Meld('<p style="one">Hello <b id="who">World</b></p>')
        >>> del p.who
        >>> del p.style
        >>> print p
        <p>Hello </p>
        """

        if name == '_content':
            self._updatePositions()
            self._markup.s = self._markup.s[:self._openEnd] + \
                             self._markup.s[self._closeStart:]
            return
        if name[0] == '_':
            try:
                del self.__dict__[name]
                return
            except KeyError:
                raise AttributeError, name
        if self._readonly:
            raise ReadOnlyError, READ_ONLY_MESSAGE
        if self._dashes:
            name = string.replace(name, '_', '-')
        self._updatePositions()
        start = self._findElementFromID(name)
        if start is not None:
            child = self._makeChild(name, start)
            self._markup.s = self._markup.s[:child._openStart] + \
                             self._markup.s[child._closeEnd:]
            return

        # Look for an attribute of this name.
        openTag = self._markup.s[self._openStart:self._openEnd]
        attributeMatch = re.search(attributeRE % name, openTag)
        if attributeMatch:
            attributeStart, attributeEnd = attributeMatch.span()
            newOpenTag = openTag[:attributeStart] + openTag[attributeEnd:]
            self._markup.s = self._markup.s[:self._openStart] + \
                             newOpenTag + \
                             self._markup.s[self._openEnd:]
        else:
            raise AttributeError, "No element or attribute named %r" % name

    def __mod__(self, values):
        """`object % value`, `object % sequence`, or `object % dictionary` all
        mimic the `%` operator for strings:

        >>> xml = '<x><y id="greeting">Hello</y> <z id="who">World</z></x>'
        >>> x = Meld(xml)
        >>> print x % ("Howdy", "everybody")
        <x><y id="greeting">Howdy</y> <z id="who">everybody</z></x>
        >>> print x % {'who': 'all'}
        <x><y id="greeting">Hello</y> <z id="who">all</z></x>

        Assignment for sequences happens in the same order that nodes with
        'id' attributes appear in the document, not including the top-level
        node (because if the top-level node were included, you'd only ever
        be able to assign to that and nothing else):

        >>> xml = '''<a id="a">
        ... <b>  <!-- `b` has no ID, hence is ignored. -->
        ...     <c id="c">First one</c>
        ...     <d id="d">Second one</d>
        ... </b>
        ... <e id="e">Third one; the content includes 'f':
        ...     <f id="f">Removed when 'e' is assigned to</f>
        ... </e>
        ... </a>'''
        >>> a = Meld(xml)
        >>> print a % ('One, with a <z id="new">new</z> node', 'Two', 'Three')
        <a id="a">
        <b>  <!-- `b` has no ID, hence is ignored. -->
            <c id="c">One, with a <z id="new">new</z> node</c>
            <d id="d">Two</d>
        </b>
        <e id="e">Three</e>
        </a>

        Giving the wrong number of elements to `%` raises the same exceptions
        as the builtin string `%` operator.  Unlike the builtin `%` operator,
        dictionaries don't need to specify all the keys:

        >>> print x % "Howdy"
        Traceback (most recent call last):
        ...
        TypeError: not enough arguments
        >>> print x % ("Howdy", "everybody", "everywhere")
        Traceback (most recent call last):
        ...
        TypeError: not all arguments converted
        >>> print x % {"greeting": "Howdy"}
        <x><y id="greeting">Howdy</y> <z id="who">World</z></x>
        """

        # Figure out whether we have a dictionary, a sequence, or a lone value.
        new = self.clone()
        new._updatePositions()
        if hasattr(values, 'values') and callable(values.values):
            # It's a dictionary.
            keys = values.keys()
            sequence = values.values()
        elif hasattr(values, '__getitem__') and \
             not isinstance(values, StringType) or isinstance(values, UnicodeType):
            # It's a sequence.
            keys = None
            sequence = list(values)
        else:
            # Assume it's a plain value.
            keys = None
            sequence = [values]

        # If we've derived a set of keys, just assign the values.
        if keys:
            for key, value in zip(keys, sequence):
                if self._dashes:
                    key = string.replace(key, '_', '-')
                if not isinstance(value, StringType) or isinstance(value, UnicodeType):
                    value = str(value)
                start = new._findElementFromID(key)
                if start is not None:
                    child = new._makeChild(key, start)
                    new._markup.s = new._markup.s[:child._openEnd] + \
                                    value + \
                                    new._markup.s[child._closeStart:]
        else:
            # No keys, so set the values in the order they appear.  We
            # reverse the sequence so we can use pop().
            sequence.reverse()
            pos = new._openEnd
            while sequence:
                value = sequence.pop()
                if not isinstance(value, StringType) or isinstance(value, UnicodeType):
                    value = str(value)
                subset = new._markup.s[pos:new._closeStart]
                match = _findIDMatch('[^\'"]*', subset)
                if not match:
                    # We've run out of elements with `id` attributes.
                    raise TypeError, "not all arguments converted"
                child = new._makeChild(match.group('id'), pos+match.start())
                new._markup.s = new._markup.s[:child._openEnd] + \
                                value + \
                                new._markup.s[child._closeStart:]
                addedSize = len(value) - (child._closeStart - child._openEnd)
                new._closeStart += addedSize
                new._closeEnd += addedSize
                pos = child._closeEnd + addedSize
            subset = new._markup.s[pos:new._closeStart]
            match = _findIDMatch('[^\'"]*', subset)
            if match:
                raise TypeError, "not enough arguments"

        return new

    def toFormatString(self, useDict=False):
        r"""Converts a Meld object to a string, with the contents of any tags
        with `id` attributes replaced with `%s` or `%(id)s`.  This lets you
        use Python's built-in `%` operator rather than PyMeld's, which can
        speed things up considerably when you're looping over a lot of data.
        Here's the example from the main documentation, speeded up by using
        `toFormatString()` and by avoiding repeated use of the `+=` operator:

        >>> xhtml = '''<html><table id="people">
        ... <tr id="header"><th>Name</th><th>Age</th></tr>
        ... <tr id="row"><td id="name">Example</td><td id="age">21</td></tr>
        ... </table></html>'''
        >>> doc = Meld(xhtml)
        >>> rowFormat = doc.row.toFormatString()
        >>> rows = []
        >>> for name, age in [("Richie", 30), ("Dave", 39), ("John", 78)]:
        ...      rows.append(rowFormat % (name, age))
        >>> doc.people = '\n' + doc.header + ''.join(rows)
        >>> print re.sub(r'</tr>\s*', '</tr>\n', str(doc))  # Prettify
        <html><table id="people">
        <tr id="header"><th>Name</th><th>Age</th></tr>
        <tr id="row"><td id="name">Richie</td><td id="age">30</td></tr>
        <tr id="row"><td id="name">Dave</td><td id="age">39</td></tr>
        <tr id="row"><td id="name">John</td><td id="age">78</td></tr>
        </table></html>

        So the inner loop no longer contains any PyMeld calls at all - it only
        manipulates strings and lists.  Here's what `doc.row.toFormatString()`
        actually returns - note that this is a string, not a PyMeld object:

        >>> print doc.row.toFormatString()
        <tr id="row"><td id="name">%s</td><td id="age">%s</td></tr>

        You can ask for a format string that expects a dictionary rather than
        a tuple using the `useDict` parameter:

        >>> print doc.row.toFormatString(useDict=True)
        <tr id="row"><td id="name">%(name)s</td><td id="age">%(age)s</td></tr>

        If your markup contains `%` symbols, they are correctly quoted in the
        resulting format string:

        >>> doc = Meld("<html><p>10% <span id='drink'>gin</span>.</p></html>")
        >>> print doc.toFormatString()
        <html><p>10%% <span id='drink'>%s</span>.</p></html>
        >>> print doc.toFormatString() % 'vodka'
        <html><p>10% <span id='drink'>vodka</span>.</p></html>
        """

        # Build a dictionary mapping from all the possible keys to special
        # marker values.  It doesn't matter if there's some text with `id='x'`
        # in there, because it will just be ignored.
        self._updatePositions()
        content = self._markup.s[self._openEnd:self._closeStart]
        quotesAndKeys = re.findall(r'\bid=(["\'])([^"\']+)\1', content)
        keysToMarkers = {}
        for unusedQuote, key in quotesAndKeys:
            if self._dashes:
                key = string.replace(key, '-', '_')
            keysToMarkers[key] = ":PyMeldMarker'%s':" % key

        # Now use the PyMeld `%` operator to populate the tags.
        format = str(self % keysToMarkers)

        # Convert the resulting marked-up string to a format string, by
        # quoting all the % characters then inserting %s directives.
        format = string.replace(format, '%', '%%')
        if useDict:
            return re.sub(r":PyMeldMarker'([^']+)':", r'%(\1)s', format)
        else:
            return re.sub(r":PyMeldMarker'[^']+':", r'%s', format)

    def clone(self, readonly=0, replaceUnderscoreWithDash=False):
        """Creates a clone of a `Meld`, for instance to change an attribute
        without affecting the original document:

        >>> p = Meld('<p style="one">Hello <b id="who">World</b></p>')
        >>> q = p.clone()
        >>> q.who = "Richie"
        >>> print q.who
        <b id="who">Richie</b>
        >>> print p.who
        <b id="who">World</b>
        """

        self._updatePositions()
        markup = self._markup.s[self._openStart:self._closeEnd]
        return Meld(markup, readonly, replaceUnderscoreWithDash)

    def __add__(self, other):
        """`object1 + object2` turns both objects into strings and returns the
        concatenation of the strings:

        >>> a = Meld('<html><span id="x">1</span></html>')
        >>> b = Meld('<html><span id="y">2</span></html>')
        >>> c = Meld('<html><span id="z">3</span></html>')
        >>> print a + b
        <html><span id="x">1</span></html><html><span id="y">2</span></html>
        >>> print a.x + b.y + c.z
        <span id="x">1</span><span id="y">2</span><span id="z">3</span>
        """

        if isinstance(other, Meld):
            other._updatePositions()
            other = other._markup.s[other._openStart:other._closeEnd]
        self._updatePositions()
        return self._markup.s[self._openStart:self._closeEnd] + other

    def __radd__(self, other):
        """See `__add__`"""
        # The case where `other` is a Meld can never happen, because
        # __add__ will be called instead.
        self._updatePositions()
        return other + self._markup.s[self._openStart:self._closeEnd]

    def __iadd__(self, other):
        """`object1 += object2` appends a string or a clone of a Meld to
        the end of another Meld's content.  This is used to build things
        like HTML tables, which are collections of other objects (eg. table
        rows).  See *Real-world example* in the main documentation."""

        if self._readonly:
            raise ReadOnlyError, READ_ONLY_MESSAGE
        if isinstance(other, Meld):
            other._updatePositions()
            other = other._markup.s[other._openStart:other._closeEnd]
        self._updatePositions()
        self._markup.s = self._markup.s[:self._closeStart] + \
                         other + \
                         self._markup.s[self._closeStart:]
        return self

    def __str__(self):
        """Returns the XML that this `Meld` represents.  Don't call
        this directly - instead convert a `Meld` to a string using
        `str(object)`.  `print` does this automatically, which is why
        none of the examples calls `str`."""

        self._updatePositions()
        if self._name is None:
            return str(self._markup.s)
        else:
            return str(self._markup.s[self._openStart:self._closeEnd])

    def __unicode__(self):
        """Returns the XML that this `Meld` represents.  Don't call
        this directly - instead convert a `Meld` to unicode using
        `unicode(object)`.  `print` does this automatically, which is why
        none of the examples calls `str`.  Note that PyMeld's ability to
        handle Unicode is largely untested."""

        self._updatePositions()
        return unicode(self._markup.s[self._openStart:self._closeEnd])


#
# Extra tests, for features that aren't tested by the (visible) docstrings:
#
__test__ = {
'entities and charrefs': """
>>> page = Meld('''<html><body>&bull; This "and&#160;that"...
... <span id="s" title="&quot;Quoted&quot; & Not">x</span></body></html>''')
>>> print page.s.title
"Quoted" & Not
>>> page.s.title = page.s.title     # Accept liberally, produce strictly.
>>> print page
<html><body>&bull; This "and&#160;that"...
<span id="s" title="&quot;Quoted&quot; &amp; Not">x</span></body></html>
>>> page.s.title = page.s.title + " <>"
>>> print page.s.title
"Quoted" & Not <>
>>> print page.s
<span id="s" title="&quot;Quoted&quot; &amp; Not &lt;&gt;">x</span>
""",

'assigning to _content': """
>>> page = Meld('''<html><span id="s">Old</span></html>''')
>>> page.s._content = "New"
>>> print page
<html><span id="s">New</span></html>
>>> page._content = "All new"
>>> print page
<html>All new</html>
""",

'deleting _content': """
>>> page = Meld('''<html><span id="s">Old</span></html>''')
>>> del page.s._content
>>> print page
<html><span id="s"></span></html>
""",

'constructing from an unknown type': """
>>> page = Meld(1)
Traceback (most recent call last):
...
TypeError: Melds must be constructed from strings
""",

'accessing a non-existent attribute': """
>>> page = Meld('<html><body id="body"></body></html>')
>>> print page.spam
Traceback (most recent call last):
...
AttributeError: No element or attribute named 'spam'
>>> del page.spam
Traceback (most recent call last):
...
AttributeError: No element or attribute named 'spam'
>>> print page.body.spam    # For non-container Melds
Traceback (most recent call last):
...
AttributeError: No element or attribute named 'spam'
>>> del page.body.spam      # For non-container Melds
Traceback (most recent call last):
...
AttributeError: No element or attribute named 'spam'
""",

'add new things':"""
>>> page = Meld('''<html><textarea id="empty"></textarea></html>''')
>>> page.empty = "Not any more"
>>> page.empty.cols = 60
>>> print page
<html><textarea cols="60" id="empty">Not any more</textarea></html>
""",

'readonly': """
>>> page = Meld('''<html><span id='no'>No!</span></html>''', readonly=True)
>>> page.no = "Yes?"
Traceback (most recent call last):
...
ReadOnlyError: You can't modify this read-only Meld object

>>> page.no.attribute = "Yes?"
Traceback (most recent call last):
...
ReadOnlyError: You can't modify this read-only Meld object

>>> page.no += "More?"
Traceback (most recent call last):
...
ReadOnlyError: You can't modify this read-only Meld object

>>> del page.no
Traceback (most recent call last):
...
ReadOnlyError: You can't modify this read-only Meld object
""",

'copy from one to another': """
>>> a = Meld('<html><span id="one">One</span></html>')
>>> b = Meld('<html><span id="two">Two</span></html>')
>>> a.one = b.two
>>> print a
<html><span id="one"><span id="two">Two</span></span></html>
>>> b.two = "New"
>>> print a  # Checking for side-effects
<html><span id="one"><span id="two">Two</span></span></html>
""",

'mixed-type add, radd and iadd': """
>>> a = Meld('<html><span id="one">1</span></html>')
>>> print a.one + "x"
<span id="one">1</span>x
>>> print "x" + a.one
x<span id="one">1</span>
>>> a.one += "y<z></z>"
>>> print a
<html><span id="one">1y<z></z></span></html>
""",

'access top-level element': """
>>> d = Meld("<x id='x'>spam</x>")
>>> print d.x
<x id='x'>spam</x>
""",

'access nested element with same name': """
>>> d = Meld("<x id='x'><x id='x'>spam</x></x>")
>>> print d.x.x
<x id='x'>spam</x>
>>> d = Meld("<outer><x id='x'><x id='x'>spam</x></x></outer>")
>>> print d.x.x
<x id='x'>spam</x>
""",

# This is just a smoke-test; proper Unicode support is untested, though
# the code does attempt to be unicode-friendly.
'unicode': r"""
>>> u = Meld(u'<html><span id="one">One</span></html>')
>>> a = Meld('<html><span id="two">Two</span></html>')
>>> u.one = a.two
>>> print repr(unicode(u))
u'<html><span id="one"><span id="two">Two</span></span></html>'
>>> a.two = Meld(u'<x a="Unicode Value"/>')
>>> print a
<html><span id="two"><x a="Unicode Value"/></span></html>
""",

'private attributes': """
>>> page = Meld('<html>x</html>')
>>> page._private = "Spam"
>>> print repr(page._private)
'Spam'
>>> print page
<html>x</html>
>>> del page._private
>>> print repr(page._private)
Traceback (most recent call last):
...
AttributeError: _private
>>> del page._private
Traceback (most recent call last):
...
AttributeError: _private
>>> print page
<html>x</html>
""",

'no markup': """
>>> page = Meld("Hello world")
>>> print page.spam
Traceback (most recent call last):
...
ValueError: This isn't any form of markup I recognize
""",

'nesting': """
>>> page = Meld('''<html>
... <span id="all">Hello
...     <span id="who">World
...         <span id='extra'>and friends</span>
...     </span>!
...     <span id="goodbye">Goodbye</span>
... </span>
... </html>''')
>>> print page.all
<span id="all">Hello
    <span id="who">World
        <span id='extra'>and friends</span>
    </span>!
    <span id="goodbye">Goodbye</span>
</span>
>>> print page.extra
<span id='extra'>and friends</span>
""",

're-bug': """
>>> page = Meld("<A a='a'><B b='b'><C c='c' id='x'></C></B></A>")
>>> print page.x    # Was "<B b='b'><C c='c' id='x'></C></B>"
<C c='c' id='x'></C>
""",

'underscores': """
>>> html = '<html><div id="header-box" dash-attr="_">xxx</div></html>'
>>> meld = Meld(html, replaceUnderscoreWithDash=True)
>>> print meld % {'header_box': 'Mod'}
<html><div id="header-box" dash-attr="_">Mod</div></html>
>>> print meld.toFormatString(useDict=True)
<html><div id="header-box" dash-attr="_">%(header_box)s</div></html>
>>> meld.header_box = 'yyy'
>>> meld.header_box.dash_attr = '___'
>>> print meld
<html><div id="header-box" dash-attr="___">yyy</div></html>
""",

'doctype': """
>>> html = '<!DOCTYPE html PUBLIC "abc" "xyz">\\n<html><x id="y">z</x></html>'
>>> meld = Meld(html)
>>> meld.a = 'a'
>>> meld.y = 'b'
>>> print meld
<!DOCTYPE html PUBLIC "abc" "xyz">\n<html a="a"><x id="y">b</x></html>
""",

'eichin-bug': """
>>> page = Meld('''<table><tr><td
... id="Instance_1_0">label</td><td id="Instance_1_1"></td><td
... id="Instance_1_2"></td><td id="Instance_1_3"> </td><td class="running"
... id="Instance_1_4">Running</td></tr>
... </table>''')
>>> print page.Instance_1_4
<td class="running"
id="Instance_1_4">Running</td>
""",
}


# Entrian.Coverage: Pragma Stop

def test():
    """Tests the `PyMeld` module, performing code coverage analysis if
    `Entrian.Coverage` is available.  Returns `(failed, total)`, a la
    `doctest.testmod`."""

    import doctest
    try:
        from Entrian import Coverage
        Coverage.start('PyMeld')
    except ImportError:
        Coverage = False

    ## # Profiling.
    ## import PyMeld
    ## import profile, pstats
    ## profile.run("import doctest, PyMeld; result = doctest.testmod(PyMeld)", "rjh")
    ## s = pstats.Stats("rjh")
    ## s.sort_stats('cumulative').print_stats()

    ## # Cheap benchmark, for comparing new versions with old.
    ## import PyMeld
    ## for i in range(100):
    ##     reload(doctest)
    ##     result = doctest.testmod(PyMeld)

    import PyMeld
    result = doctest.testmod(PyMeld)

    if Coverage:
        analysis = Coverage.getAnalysis()
        analysis.printAnalysis()
    return result

if __name__ == '__main__':
    failed, total = test()
    if failed == 0:     # Else `doctest.testmod` prints the failures.
        print "All %d tests passed." % total
