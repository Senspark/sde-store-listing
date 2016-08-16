#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../../app-stores-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 12eA-Z-OclHtUxaXb_E7xzR7Rw_LXX_9nJrz8V_h1FU8 -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)
