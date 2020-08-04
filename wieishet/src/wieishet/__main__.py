# -*- coding: utf-8 -*-

"""
wieishet.

Command line handling
"""


import logging
import sys

from wieishet import LOG  # pylint: disable=E0001
from wieishet.wieishet import Wieishet


def main(argv=sys.argv):  # pylint: disable=W0102
    """Main function called from console command."""  # NOQA: D401
    logging.basicConfig()
    exit_code = 1
    try:
        app = Application(argv)
        app.run()
        exit_code = 0
    except KeyboardInterrupt:
        exit_code = 0
    except Exception as exc:  # pylint: disable=W0703
        LOG.exception(exc)
    sys.exit(exit_code)


class Application:  # pylint: disable=R0903
    """The main Application class.

    :param argv: The command line as a list as ``sys.argv``
    """

    def __init__(self, argv):
        """Empty function."""

    def run(self):  # pylint: disable=R0201
        """These statements are coppied from wieishet.py:main()."""  # NOQA: D401
        who = Wieishet()
        who.parse_arguments()
        who.inquire()
        who.compose()
        who.typeset()


if __name__ == '__main__':
    main()

# Finis
# Local Variables:
# compile-command: "flake8  __main__.py; pylint -f parseable __main__.py"
# End:
