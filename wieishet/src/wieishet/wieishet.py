#! /bin/env python
# -*- coding: utf-8 -*-

"""Typeset PDB Information"""

# Standard modules
import argparse
import datetime
import logging
import os
import pprint
import subprocess
import sys
# from ipdb import set_trace

# Third party modules
from pdb_client.api import get_person
from pdb_client.exceptions import NotFound

# Local modules
from templates import PDB

# Configure Pretty Printing and Logging
pp = pprint.PrettyPrinter(indent=4)
logging.Formatter()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s" , level=logging.ERROR
)


class Wieishet:
    """ Wieishet Class """

    def __init__(self):
        """
        Class Constructor. We do nothing more
        here that initialize our instance variables.
        """
        self.args = None
        self.filename = None
        self.who = None
        self.person = None

    def parse_arguments(self):
        """
        Parse the command line argument.
        There's only one!
        """
        parser = argparse.ArgumentParser()
        parser = argparse.ArgumentParser(description="Who is it.")
        parser.add_argument("who", help="Who?")
        self.args = parser.parse_args()
        self.who = self.args.who

    def inquire(self):
        """
        Query CWI's People Database (PDB.)
        If we have a match, instantiate a PDB
        dataclass object with selected values
        """
        try:
            person = get_person(self.who)
            logging.info(pprint.pformat(person))
        except NotFound:
            raise ValueError(f"I'm sorry but {self.who} isn't in the people database.")
        self.person = PDB(
            person["fullname"],
            person["firstname"],
            person["lastname"],
            person["room"],
            person["phone"],
            person["contract_set"][0]["department"]["name"],
            person["email"],
            person["account_set"][0]["login"],
            person["image_uri"]
        )

    def compose(self):
        """
        Our PDB template knows how to render itself
        with its's data so we merely have to print it.
        """
        date = datetime.date.today().strftime("-%d-%B-%Y")
        self.filename = f"{self.person.lastname}{date}.tex"
        with open(self.filename, "w") as location:
            print(self.person, file=location)

    def typeset(self):
        """
        Run ConTeXt to typeset the data
        """
        cmd = [
            "context",
            "--once",
            "--batchmode",
            "--noconsole",
            "--silent",
            self.filename,
        ]
        proc = subprocess.Popen(cmd)
        proc.communicate()
        retcode = proc.returncode
        base = os.path.splitext(self.filename)[0]
        if retcode != 0:
            os.unlink(base + ".pdf")
            raise ValueError(
                "Error {} executing command: {}".format(retcode, " ".join(cmd))
            )
        os.unlink(base + ".log")
        os.unlink(base + ".tuc")
        os.unlink(base + ".tex")


def main():
    """
    Primum Movens
    """
    who = Wieishet()
    who.parse_arguments()
    who.inquire()
    who.compose()
    who.typeset()


if __name__ == "__main__":
    sys.exit(main())


# Finis
# Local Variables:
# compile-command: "flake8  wieishet.py; pylint -f parseable wieishet.py"
# End:
