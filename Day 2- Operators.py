#!/bin/python3

import math
import os
import random
import re
import sys

mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())
tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100
totalCost = str(round(mealCost + tip + tax))
print (totalCost)
