# The MIT License (MIT)
#
# Copyright (c) 2019 Chris L Chapman
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
"""
`tap_on_adafruit`
================================================================================


.. todo:: Describe what the library does.


* Author(s): Chris L Chapman

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/SeattleChris/CircuitPython_tap_on_adafruit.git"

default_map = """{"doubleTap":{"1":{"hid":25,"unicode":"\\u0076","description":"","modifiers":0},"2":{"hid":30,"unicode":"\\u0021","description":"","modifiers":2},"4":{"hid":13,"unicode":"\\u006A","description":"","modifiers":0},"5":{"hid":36,"unicode":"\\u0026","description":"","modifiers":2},"6":{"hid":52,"unicode":"\\u0022","description":"","modifiers":2},"7":{"hid":57,"unicode":"\\u0043","description":"","modifiers":0},"8":{"hid":20,"unicode":"\\u0071","description":"","modifiers":0},"9":{"hid":56,"unicode":"\\u003F","description":"","modifiers":2},"10":{"hid":54,"unicode":"\\u002C","description":"","modifiers":0},"12":{"hid":56,"unicode":"\\u002F","description":"","modifiers":0},"13":{"hid":55,"unicode":"\\u003E","description":"","modifiers":2},"15":{"hid":52,"unicode":"\\u0027","description":"","modifiers":0},"16":{"hid":26,"unicode":"\\u0077","description":"","modifiers":0},"17":{"hid":29,"unicode":"\\u007A","description":"","modifiers":0},"18":{"hid":47,"unicode":"\\u005B","description":"","modifiers":0},"19":{"hid":38,"unicode":"\\u0028","description":"","modifiers":2},"29":{"hid":51,"unicode":"\\u003A","description":"","modifiers":2},"30":{"hid":45,"unicode":"\\u002D","description":"","modifiers":0},"31":{"hid":55,"unicode":"\\u002E","description":"","modifiers":0}},"singleTap":{"1":{"hid":4,"unicode":"\\u0061","description":"","modifiers":0},"2":{"hid":8,"unicode":"\\u0065","description":"","modifiers":0},"3":{"hid":17,"unicode":"\\u006E","description":"","modifiers":0},"4":{"hid":12,"unicode":"\\u0069","description":"","modifiers":0},"5":{"hid":7,"unicode":"\\u0064","description":"","modifiers":0},"6":{"hid":23,"unicode":"\\u0074","description":"","modifiers":0},"8":{"hid":18,"unicode":"\\u006F","description":"","modifiers":0},"9":{"hid":14,"unicode":"\\u006B","description":"","modifiers":0},"10":{"hid":16,"unicode":"\\u006D","description":"","modifiers":0},"11":{"hid":9,"unicode":"\\u0066","description":"","modifiers":0},"12":{"hid":15,"unicode":"\\u006C","description":"","modifiers":0},"13":{"hid":10,"unicode":"\\u0067","description":"","modifiers":0},"14":{"hid":42,"unicode":"\\u0042\\u0061\\u0063\\u006B\\u0073\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":0},"15":{"hid":21,"unicode":"\\u0072","description":"","modifiers":0},"16":{"hid":24,"unicode":"\\u0075","description":"","modifiers":0},"17":{"hid":28,"unicode":"\\u0079","description":"","modifiers":0},"18":{"hid":5,"unicode":"\\u0062","description":"","modifiers":0},"19":{"hid":19,"unicode":"\\u0070","description":"","modifiers":0},"20":{"hid":29,"unicode":"\\u007A","description":"","modifiers":0},"21":{"hid":26,"unicode":"\\u0077","description":"","modifiers":0},"22":{"hid":20,"unicode":"\\u0071","description":"","modifiers":0},"23":{"hid":13,"unicode":"\\u006A","description":"","modifiers":0},"24":{"hid":22,"unicode":"\\u0073","description":"","modifiers":0},"25":{"hid":40,"unicode":"\\u0045\\u006E\\u0074\\u0065\\u0072","description":"","modifiers":0},"26":{"hid":27,"unicode":"\\u0078","description":"","modifiers":0},"27":{"hid":25,"unicode":"\\u0076","description":"","modifiers":0},"29":{"hid":6,"unicode":"\\u0063","description":"","modifiers":0},"30":{"hid":11,"unicode":"\\u0068","description":"","modifiers":0},"31":{"hid":44,"unicode":"\\u0053\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":0}},"tripleTap":{"1":{"hid":31,"unicode":"\\u0040","description":"","modifiers":2},"2":{"hid":61,"unicode":"\\u003D","description":"","modifiers":0},"5":{"hid":33,"unicode":"\\u0024","description":"","modifiers":2},"6":{"hid":32,"unicode":"\\u0023","description":"","modifiers":2},"9":{"hid":37,"unicode":"\\u002A","description":"","modifiers":2},"12":{"hid":103,"unicode":"\\u002B","description":"","modifiers":2},"13":{"hid":54,"unicode":"\\u003C","description":"","modifiers":2},"15":{"hid":37,"unicode":"\\u0025","description":"","modifiers":2},"16":{"hid":45,"unicode":"\\u005F","description":"","modifiers":2},"18":{"hid":48,"unicode":"\\u005D","description":"","modifiers":0},"19":{"hid":39,"unicode":"\\u0029","description":"","modifiers":2},"29":{"hid":51,"unicode":"\\u003B","description":"","modifiers":0}},"shift":{"1":{"hid":4,"unicode":"\\u0061","description":"","modifiers":2},"2":{"hid":8,"unicode":"\\u0065","description":"","modifiers":2},"3":{"hid":17,"unicode":"\\u006E","description":"","modifiers":2},"4":{"hid":12,"unicode":"\\u0069","description":"","modifiers":2},"5":{"hid":7,"unicode":"\\u0064","description":"","modifiers":2},"6":{"hid":23,"unicode":"\\u0074","description":"","modifiers":2},"8":{"hid":18,"unicode":"\\u006F","description":"","modifiers":2},"9":{"hid":14,"unicode":"\\u006B","description":"","modifiers":2},"10":{"hid":16,"unicode":"\\u006D","description":"","modifiers":2},"11":{"hid":9,"unicode":"\\u0066","description":"","modifiers":2},"12":{"hid":15,"unicode":"\\u006C","description":"","modifiers":2},"13":{"hid":10,"unicode":"\\u0067","description":"","modifiers":2},"14":{"hid":42,"unicode":"\\u0042\\u0061\\u0063\\u006B\\u0073\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":0},"15":{"hid":21,"unicode":"\\u0072","description":"","modifiers":2},"16":{"hid":24,"unicode":"\\u0075","description":"","modifiers":2},"17":{"hid":28,"unicode":"\\u0079","description":"","modifiers":2},"18":{"hid":5,"unicode":"\\u0062","description":"","modifiers":2},"19":{"hid":19,"unicode":"\\u0070","description":"","modifiers":2},"20":{"hid":29,"unicode":"\\u007A","description":"","modifiers":2},"21":{"hid":26,"unicode":"\\u0077","description":"","modifiers":2},"22":{"hid":20,"unicode":"\\u0071","description":"","modifiers":2},"23":{"hid":13,"unicode":"\\u006A","description":"","modifiers":2},"24":{"hid":22,"unicode":"\\u0073","description":"","modifiers":2},"25":{"hid":40,"unicode":"\\u0045\\u006E\\u0074\\u0065\\u0072","description":"","modifiers":0},"26":{"hid":27,"unicode":"\\u0078","description":"","modifiers":2},"27":{"hid":25,"unicode":"\\u0076","description":"","modifiers":2},"29":{"hid":6,"unicode":"\\u0063","description":"","modifiers":2},"30":{"hid":11,"unicode":"\\u0068","description":"","modifiers":2},"31":{"hid":44,"unicode":"\\u0053\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":0}},"switch":{"1":{"hid":30,"unicode":"\\u0031","description":"","modifiers":0},"2":{"hid":31,"unicode":"\\u0032","description":"","modifiers":0},"3":{"hid":80,"unicode":"\\u0041\\u0072\\u0072\\u006F\\u0077\\u004C\\u0065\\u0066\\u0074","description":"","modifiers":0},"4":{"hid":32,"unicode":"\\u0033","description":"","modifiers":0},"5":{"hid":55,"unicode":"\\u002E","description":"","modifiers":0},"6":{"hid":82,"unicode":"\\u0041\\u0072\\u0072\\u006F\\u0077\\u0055\\u0070","description":"","modifiers":0},"8":{"hid":33,"unicode":"\\u0034","description":"","modifiers":0},"9":{"hid":81,"unicode":"\\u0041\\u0072\\u0072\\u006F\\u0077\\u0044\\u006F\\u0077\\u006E","description":"","modifiers":0},"10":{"hid":11,"unicode":"\\u0068","description":"","modifiers":8},"11":{"hid":44,"unicode":"\\u0053\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":8},"12":{"hid":79,"unicode":"\\u0041\\u0072\\u0072\\u006F\\u0077\\u0052\\u0069\\u0067\\u0068\\u0074","description":"","modifiers":0},"13":{"hid":43,"unicode":"\\u0054\\u0061\\u0062","description":"","modifiers":8},"14":{"hid":42,"unicode":"\\u0042\\u0061\\u0063\\u006B\\u0073\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":0},"15":{"hid":43,"unicode":"\\u0054\\u0061\\u0062","description":"","modifiers":0},"16":{"hid":34,"unicode":"\\u0035","description":"","modifiers":0},"17":{"hid":35,"unicode":"\\u0036","description":"","modifiers":0},"18":{"hid":36,"unicode":"\\u0037","description":"","modifiers":0},"19":{"hid":41,"unicode":"\\u0045\\u0073\\u0063","description":"","modifiers":0},"20":{"hid":37,"unicode":"\\u0038","description":"","modifiers":0},"21":{"hid":17,"unicode":"\\u006E","description":"","modifiers":8},"24":{"hid":38,"unicode":"\\u0039","description":"","modifiers":0},"30":{"hid":39,"unicode":"\\u0030","description":"","modifiers":0},"31":{"hid":44,"unicode":"\\u0053\\u0070\\u0061\\u0063\\u0065","description":"","modifiers":0}},"layoutId":"0VMKqB9hnBvSZXRU","mapStoreVersion":1,"layoutVersion":1,"layoutName":"Defult Tap Map","description":"The deafult map provided with a brand new strap.\nUseful when one wants to override his alternate map."}"""
