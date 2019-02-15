"""dump_xml - A simple dictionary to XML converter that "Just Works"."""

__version__ = '1.0.0'
__author__ = 'James Cheese <james.cheese@intouch-ltd.com>'
__all__ = []

from xml.etree import ElementTree
from collections import OrderedDict, Sequence

def dump_xml(target, name, _parent=None):
    # type: (object, str, ElementTree.Element) -> ElementTree.Element
    """
    Takes the object in target and encodes it as an ElementTree XML node named *name*.

    If target is a dict, recursively build a subtree, adds it to parent and returns
    it. If you want these in a specific order, make sure to use an OrderedDict.
    If target is an ElementTree.Element, adds it to parent and returns it.
    If target is a sequence, build a set of elements from the items and adds them to
    parent. Returns None, as it does not return a single node. It is not valid to call
    it this way in a standalone manner without a parent node - an exception will be
    raised.
    Otherwise, call str() on target, and create, add to parent, and return an element
    containing that string value.

    Args:
        target: The object to encode
        name: Name for this element (or root element)
        
    Examples:
    >>> bytearray(ElementTree.tostring(dump_xml(1, "a")))
    bytearray(b'<a>1</a>')

    >>> bytearray(ElementTree.tostring(dump_xml(OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)]), "a")))
    bytearray(b'<a><apple>4</apple><banana>3</banana><orange>2</orange><pear>1</pear></a>')

    >>> bytearray(ElementTree.tostring(dump_xml(ElementTree.Element("nop"), "a")))
    bytearray(b'<a><nop /></a>')

    >>> bytearray(ElementTree.tostring(dump_xml({"a": [1,2,3]}, "b")))
    bytearray(b'<b><a>1</a><a>2</a><a>3</a></b>')

    >>> bytearray(ElementTree.tostring(dump_xml([1,2,3], "a")))
    Traceback (most recent call last):
    ...
    ValueError: Cannot XML serialize a sequence without a containing element

    >>> bytearray(ElementTree.tostring(dump_xml({"b": [4,5,{"c": {"d": False}}, ElementTree.Element("nop")],}, "a")))
    bytearray(b'<a><b>4</b><b>5</b><b><c><d>False</d></c></b><b><nop /></b></a>')
    """
    if _parent == None:
        pass # Do something?
    if isinstance(target, Sequence) and not isinstance(target, str):
        if _parent is None:
            raise ValueError("Cannot XML serialize a sequence without a containing element")
        for item in target:
            dump_xml(item, str(name), _parent)
        return None # Can't return a single node here.
    else:
        element = ElementTree.Element(str(name))
        if isinstance(target, dict):
            for key, value in target.items():
                dump_xml(value, key, element)
        elif isinstance(target, ElementTree.Element):
            element.append(target)
        else:
            element.text = str(target)
        if _parent is not None:
            _parent.append(element)
        return element

