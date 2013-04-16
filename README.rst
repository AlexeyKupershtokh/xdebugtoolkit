xdebugtoolkit
=============

|Build Status|

Installation
~~~~~~~~~~~~

.. code:: sh

    sudo easy_install xdebugtoolkit [xdot]

or

.. code:: sh

    sudo pip install xdebugtoolkit [xdot]

.. |Build Status| image:: https://travis-ci.org/AlexeyKupershtokh/xdebugtoolkit.png?branch=master
   :target: https://travis-ci.org/AlexeyKupershtokh/xdebugtoolkit

Tools
~~~~~

-  `cg2dot`_ - converter from `Xdebug cachegrind`_ files to the `dot`_
   format.
-  `cgsplit`_ - splitter for appended cachegrind files. May be useful in
   case your `xdebug.profiler\_append`_ option is set to 1.
-  `xdot-pygoocanvas`_ - completely rewritten `xdot`_ in order to make
   it utilize PyGooCanvas which gives extra performance on large graphs.
   You'll need to install PyGooCanvas in addition to `xdot
   requirements`_.

.. _cg2dot: 
.. _Xdebug cachegrind: http://www.xdebug.org/docs/profiler
.. _dot: http://www.graphviz.org/
.. _cgsplit: 
.. _xdebug.profiler\_append: http://xdebug.org/docs/profiler#profiler_append
.. _xdot-pygoocanvas: 
.. _xdot: https://code.google.com/p/jrfonseca/wiki/XDot
.. _xdot requirements: https://code.google.com/p/jrfonseca/wiki/XDot#Requirements
