#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../../app-stores-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1942qfEABEBkTFZnWhPHrGqCt4a2FXEAimjQUz7bIkEM -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)
