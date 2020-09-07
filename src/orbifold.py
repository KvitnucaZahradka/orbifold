#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2020 September 07 00:14:23 (EST) 

@author: KanExtension
"""

from abc import ABC, abstractmethod
from typing import Tuple, List, Union, Iterable, Set, Dict, Iterator
from itertools import takewhile, tee, product, chain
import copy
import os
import sys
import re
import yaml
import json
import random
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
from functools import reduce, lru_cache
import matplotlib.pyplot as plt

# custom imports
import orbifold_utils as ou
import orbifold_warnings as ow


# define the rand
RAND = lambda: random.randint(0, 2*20)

# import the config
with open(os.path.split(__file__)[0], 'config', 'config.md') as handle:
    _config = yaml.safe_load(handle)


'''
N O D E   C L A S S
'''



