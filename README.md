# xdebugtoolkit

[![Build Status](https://travis-ci.org/AlexeyKupershtokh/xdebugtoolkit.png?branch=master)](https://travis-ci.org/AlexeyKupershtokh/xdebugtoolkit)

A toolkit for splitting, aggregating, analyzing and visualizing xdebug cachegrind files.

### Installation
```sh
sudo easy_install xdebugtoolkit [xdot]
```
or

```sh
sudo pip install xdebugtoolkit [xdot]
```
### Tools

* [cg2dot](https://code.google.com/p/xdebugtoolkit/wiki/cg2dot) - converter from [Xdebug cachegrind](http://www.xdebug.org/docs/profiler) files to the [dot](http://www.graphviz.org/) format.
* [cgsplit](https://code.google.com/p/xdebugtoolkit/wiki/cgsplit) - splitter for appended cachegrind files. May be useful in case your [xdebug.profiler_append](http://xdebug.org/docs/profiler#profiler_append) option is set to 1.
* [xdot-pygoocanvas]() - completely rewritten [xdot](https://code.google.com/p/jrfonseca/wiki/XDot) in order to make it utilize PyGooCanvas which gives extra performance on large graphs. You'll need to install PyGooCanvas in addition to [xdot requirements](https://code.google.com/p/jrfonseca/wiki/XDot#Requirements).
