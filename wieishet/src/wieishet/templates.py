# -*- coding: utf-8 -*-

"""Templates"""

from dataclasses import dataclass


@dataclass
class PDB:  # pylint: disable=R0902
    """
    This PDB dataclass contains both data,
    a presentation template and the means
    of filling the latter with the former.
    """
    fullname: str
    firstname: str
    lastname: str
    room: str
    phone: str
    department: str
    email: str
    account: str
    image: str
    template: str = (
        r"""\setuppagenumbering[state=off]
              \starttext
              \externalfigure[https://www.cwi.nl/intranet%s]
              \starttabulate[|r|l|]
                \NC Naam/Name \EQ {%s} \NC\NR
                \NC Roepnaam/Given name \EQ {%s} \NC\NR
                \NC Kamer/Office \EQ {%s} \NC\NR
                \NC Telefoon/Phone \EQ {%s} \NC\NR
                \NC Afdeling/Dept. \EQ {%s} \NC\NR
                \NC E-mail (Internet)\EQ {%s} \NC\NR
                \NC Account \EQ {%s} \NC\NR
               \stoptabulate
            \stoptext""")

    def __repr__(self):
        """
        A custom representation function that merely
        populates the template with the data.
        """
        return self.template % (
            self.image,
            self.fullname,
            self.firstname,
            self.room,
            self.phone,
            self.department,
            self.email,
            self.account,
        )


# Finis
# Local Variables:
# compile-command: "flake8  templates.py; pylint -f parseable templates.py"
# End:
