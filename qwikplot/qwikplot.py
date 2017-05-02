# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import rcParams as rc
import seaborn as sns

set_style_valid_args = {'default'}
def set_style(style='default', save_dir='.'):
    if style not in set_style_valid_args:
        raise ValueError('set_style: style must be one of %r' 
			 % set_style_valid_args)
    if style == 'default':
        sns.set_context('paper')
        sns.set_style('white')
        sns.set_palette('colorblind')

        rc['text.usetex'] = True
        rc['font.size'] = 30
        rc['figure.figsize'] = (5, 5)
        rc['savefig.format'] = 'pdf'
        rc['savefig.transparent'] = True
        rc['savefig.bbox'] = 'tight'
        rc['savefig.directory'] = os.chdir(save_dir)
