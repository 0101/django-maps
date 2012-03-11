from paver.easy import *
import paver.doctools
from paver.setuputils import setup


options(
    sphinx=Bunch(
        builddir='build',
        sourcedir='source',
    ),
    minilib = Bunch(
        extra_files=["doctools"]
    )
)

setup(
    name='Django Maps',
    packages=['django_maps'],
    version='0.1',
)
