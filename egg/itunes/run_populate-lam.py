#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../store-listing-toolkit/populate-v3.py metadata -platform iOS -prj-path . -sheet 11q1bVrQW5qNymmLfNej1sKSnZzncDeFGOgi20rY_6-I -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
