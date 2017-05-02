
"""
test_qwikplot
----------------------------------

Tests for `qwikplot` module.
"""

import pytest
import sys
sys.path.append('../')
from qwikplot import qwikplot


def test_set_style():
    qwikplot.set_style()
    qwikplot.set_style('default')
    qwikplot.set_style('default', save_dir='..')
    
