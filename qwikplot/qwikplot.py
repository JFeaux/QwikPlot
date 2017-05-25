# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from matplotlib import rcParams as rc
import seaborn.apionly as sns

set_style_valid_args = {'default', 'pub_1col', 'pub_2col'}
col_width = 3.2
two_col_width = 7.75
def set_style(style='default', ratio=1., nrows=1, ncols=1, save_dir='.'):
    """ Sets rc parameters for matplotlib plots

    Function for setting rc parameters for nice matplotlib plots. 
    pub_1col and pub_2col produce publication quality plots 
    for one column and two column width figures respectively

    Args:
        style: string representing figure style. 
        ratio: height / width of figure frame.
        nrows: number of rows of figure frames 
        ncols: number of columns of figure frame
        save_dir: path of directory to save figure

    Returns:
        None

    Raises:
        ValueError: style must be one of set_style_valid_args
        
    """

    if style not in set_style_valid_args:
        raise ValueError('set_style: style must be one of %r' 
			 % set_style_valid_args)

    sns.set_palette('colorblind')

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
        rc['savefig.format'] = 'pdf'

    elif style[:3] == 'pub':
        rc['text.usetex'] = True
        rc['savefig.format'] = 'eps'
        rc['savefig.transparent'] = True
        rc['savefig.bbox'] = 'tight'
        rc['savefig.directory'] = os.chdir(save_dir)
        rc['lines.linewidth'] = 1.5
        rc['lines.markersize'] = 5
        rc['font.family'] = 'serif'
        rc['font.size'] = 11
        rc['axes.labelsize'] = 11
        rc['axes.labelpad'] = 8
        rc['xtick.labelsize'] = 10
        rc['ytick.labelsize'] = 10
        rc['legend.fontsize'] = 10

        if style == 'pub_1col':
            height = nrows * col_width * ratio / ncols
            rc['figure.figsize'] = (col_width, height)

        elif style == 'pub_2col':
            height = nrows * two_col_width * ratio / ncols
            rc['figure.figsize'] = (two_col_width, height)


