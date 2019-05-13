SquidReport
==========

[![Python 3.x](https://img.shields.io/badge/python-3.x-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://github.com/elcodigok/SquidReport/blob/master/LICENSE) [![Twitter](https://img.shields.io/badge/twitter-@elcodigok-blue.svg)](https://twitter.com/elcodigok)

SquidReport is a report generator that uses the Log file of the Proxy SQUID service.

**❮ NOTE ❯** This tool releases new versions on a regular basis. Make sure to update your dependencies frequently to get the latest version. Check out the changelog or CHANGELOG.md to learn about the new features.

-----


Usage
-----

    $ python3 srDomain.py -h 


Examples
--------

### Search domain in the log file

```bash
$ python3 squidReport.py -f /var/log/squid3/access.log --search "danielmaldonado.com.ar"
```

Project Home
------------

www.danielmaldonado.com.ar


Git Repository
--------------

https://github.com/elcodigok/SquidReport


Issues
------

https://github.com/elcodigok/SquidReport/issues
