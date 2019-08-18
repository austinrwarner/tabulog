"""Convert semi-structured log files (such as 'Apache' access.log files)
into a tabular format (data.frame) using a standard template system.

.. moduleauthor:: Austin Nar <austin.nar@gmail.com>

"""

from .defaults import default_classes
from .parser import *
from .templates import *
