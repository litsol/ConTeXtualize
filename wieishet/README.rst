========
WIEISHET
========

Typeset information from CWI's public accessible people database (PDB).

This is a simple example of how to retrieve information from a
database, wrap the data in a template, write the template to file and
compile the file into a PDF document with ConTeXt.

It is also an example of how to structure a complete Python module.


Dependencies
============

You will need the following pieces of software to continue:

1. ConTeXt
2. Git
3. Mercurial (hg)
4. pipenv
5. Python3


Installation
============

This GIT repository contains a Pipfile that names the Python packages
used to run and develop this software. Run the following commands to
instantiate a virtual environment with these packages and install the
'wieishet' console-script.

.. code:: console

  $ export PIPENV_VENV_IN_PROJECT=True
  $ pipenv install
  $ pipenv shell
  $ cd wieishet
  $ python setup.py install


The 'wieishet' console-script uses ConTeXt to typeset its data. If you
need to install ConTeXt, you find the necessary instructions at:
`Install CONTEXT LMTX <http://pragma-ade.com/install.htm>`_.

If your are CWI you can avail yourself of a pre-installed ConTeXt
distribution. Initialize it with the followint command:

.. code:: console

  $ source /opt/sw/context/tex/setuptex


PDB access
==========

You have to be behind the CWI firewall to reach the people database;
which means you either have to be at CWI or have tunneled into a CWI
desktop machine. If you have established a VPN connection to CWI from
home, your machine at home is effectively behind the CWI firewall.


Running the script
===========================
Now that everything is in place you can run the console-script like this:

.. code:: console

  $ wieishet aggelen

If all goes well ConTeXt will display a line something like this::

  This is LuaTeX, Version 1.11.2 (TeX Live 2020/dev)
   system commands enabled.

Afterwards, you should find a PDF file whose name is composed of the
last name of the individual you choose and the date the file was
created, e.g.,::

  Aggelen-04-August-2020.pdf

Compare the PDF contents with the result of running the PDB command
line tool available on every CWI desktop machine.

.. code:: console

  $ cwi aggelen


Developer notes
===============

You can modify the code following the usual procecures.

.. code:: console

  $ python setup.py develop
  $ pip install wieishet[dev]

Run the tests:

.. code:: console

  $ python setup.py test
  $ python run_tests.py


*FINIS*

.. Finis
.. Local Variables:
.. compile-command: "rst2html README.rst README.html && tidy -im README.html"
.. End:
