#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path
import shutil
import time,  datetime



def removeFileInFirstDir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)