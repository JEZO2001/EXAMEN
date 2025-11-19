import xlwings as xw
import numpy as np
import pandas as pd

wb = xw.Book()
caudales = wb.sheets.add("caudales")