# -*- coding: utf-8 -*-

import os

def files(directory):
    paths = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        paths.append(path)
    return paths
