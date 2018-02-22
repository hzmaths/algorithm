#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 00:38:09 2018

@author: deeplearning
"""

class EmptyException(BaseException):
    def __init__(self,message):
        self.message = message