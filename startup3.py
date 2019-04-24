
# -*- coding: utf-8 -*-
import logging
import os
import glob
import sys
import re
import gzip
import mimetypes
import datetime
from xml.dom import minidom
declaredLogLevel = int((os.environ.get('logLevel')) or logging.INFO)
logging.basicConfig(level=declaredLogLevel, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(declaredLogLevel)
import sys
#do linux tests and append to the shared directories
#if settings.IsLinux():#
#do not need these appends as svn obviates this need
#sys.path.append('/home/userid/mount_points/Users/pasmith48/Documents/Python/')#
#sys.path.append('/home/userid/mount_points/Users/pasmith48/Documents/Python/MatplotlibExamples/')#
import imp
try:
	import exceptions
except:
	logger.debug('could not import exceptions')

try:
	import requests
except:
	logger.debug('import requests error')
try:
	import grequests
except:
	logger.debug('import grequests error')

try:
	import nltk
	import bs4
	import urllib
except:
	logger.debug('nltk,bs4,urllib')

try:
	import urllib2
except:
	logger.debug('import error')
import json
import copy
import itertools
from fractions import Fraction
import colorsys
import pickle
import time
try:
	import StringIO
except:
	logger.debug('import error')
import subprocess
import csv
import poplib, email
from email.header import decode_header, make_header
import locale
locale.setlocale(locale.LC_ALL, '')
#import matplotlib#
#matplotlib.use('QT4Agg')#
#from matplotlib import pyplot#
#from matplotlib.pyplot import hold, plot, show, gca ,gcf#


import pandas
from pandas.io import sql
from pandas import Series, DataFrame, MultiIndex, date_range, Panel, merge
from pandas.util.testing import rands
from pandas import DatetimeIndex
try:
	from pandas.tseries.index import Timestamp
except:
	logger.debug('could not set all pandas print options')

try:
	pandas.set_option('display.precision', 9)
	pandas.set_option('max_rows',500)
	pandas.set_option('max_columns', 15)
	pandas.set_printoptions(max_colwidth=100)
except:
	logger.debug('could not set all pandas print options')
	
try: 
	import numpy
	aaa = numpy.array
except:
	logger.debug('numpy modules failed to import')

try: #import Bio modules
	import Bio 
	import Bio.pairwise2
except:
	logger.debug('Bio modules failed to import')
	pass

try: #import scipy modules
	import scipy
except:
	logger.debug('scipy modules failed to import')
	pass

try: #import pytables modules
	import tables
except:
	logger.debug('pytables modules failed to import')

try: #import visualization modules
	import matplotlib
	import matplotlib.pyplot as plt
	from matplotlib.pyplot import hold, plot,hist,gca,gcf
	import matplotlib.dates as mdates
	import pylab
	from mpl_toolkits.axes_grid1 import host_subplot
	import mpl_toolkits.axisartist as AA
	import IPython
	from IPython.core.display import HTML
	from IPython.display import display, Math, Latex
except:
	logger.debug('some visualization modules failed to import')
	pass

try:
	from sklearn import datasets, svm
	from sklearn.feature_selection import SelectPercentile, f_classif
	from sklearn import preprocessing
	from sklearn import svm
	from sklearn.preprocessing import Scaler
except:
	logger.debug('some sklearn modules failed to import')
	pass

try:
	from sklearn.preprocessing import StandardScaler
	oldSklearn = False
except:
	#don't have this newer version of sklearn
	oldSklearn = True

try:
	import MySQLdb
	logger.debug('MySQLdb available')
except:
	logger.debug('MySQLdb failed to import')
	pass

try:
	import pymysql
	logger.debug('pymysql available')
except:
	logger.debug('pymysql failed to import')
	pass

try:
	import sqlalchemy
except:
	logger.debug('sqlalchemy failed to import')
	pass


if sys.platform.find('linux')>=0:
	sys.path.append('/home/userid/shadow')
	sys.path.append('/home/userid/python_code')
	sys.path.append('/srv/data/userid/python_code')
else:
	#sys.path.append('C:/Users/userid48/Stash/python_code/')
	pass
import settings
try:
	import Utilities
except:
	logger.debug("Utilities failed to import")
try:
	import MachineLearningA
except:
	logger.debug("MachineLearningA failed to import")
try:
	import HiveHelp
except:
	logger.debug("HiveHelp failed to import")
try:
	import QueryObject
except:
	logger.debug("QueryObject failed to import")
try:
    import ShellUtilities
except:
	logger.debug("ShellUtilities failed to import")
try:
	import RulesAnalysis
except:
	logger.debug("RulesAnalysis failed to import")

try:
	import ContentClassifier 
except:
	logger.debug("content classifer failed to import")

try:
	import JmxUtilities 
except:
	logger.debug("JmxUtilities failed to import")

try:
	import RunAntiPhishQueries 
except:
	logger.debug("RunAntiPhishQueries failed to import")

try:
	import WebScrapingUtilities
except:
	logger.debug('WebScrapingUtilities failed to import' )

try:
	import networkx
except:
	logger.debug('networkx failed to import' )

try:
	import graph_preparation
except:
	logger.debug('networkx failed to import' )

try:
	import highways
except:
	logger.debug('highways failed to import' )


try:
	mhist = hist
	del hist
except:
	logger.debug('failed some custom defs')
	pass
try:
	#mhist = matplotlib.pylab.histogram#
	vcf = pandas.Series.value_counts
	S = pandas.Series
	l = list
except:
	logger.debug('failed some custom defs')
	pass
try:

	hist = Utilities.SearchHistoryDirect
	history = Utilities.SearchHistoryDirect
except:
	logger.debug('failed Utilities some custom defs')
try:
	nbname = Utilities.GetIPythonNotebookName()
except:
	logger.debug('failed getting nbname method')


dia = csv.excel()
dia.delimiter = u'\x01'
dia.quoting = csv.QUOTE_NONE

diaTab = csv.excel()
diaTab.delimiter = u'\t'
diaTab.quoting = csv.QUOTE_NONE

diaVar = csv.excel()
diaVar.delimiter = ','
diaVar.quoting = csv.QUOTE_NONE

kwargsGrabResult = {}
kwargsGrabResult['remote'] = True
kwargsGrabResult['sshDestination'] = ''

kwargsRun = {}
kwargsRun['remote'] = True
kwargsRun['logQuery'] = True
kwargsRun['throttle'] = False
kwargsRun['rerunQuery'] = True
kwargsRun['sshDestination'] = ''
kwargsRun['sshCommand'] = 'ssh'
kwargsRun['localRoot'] = '/home/userid'
kwargsRun['getQueryOnly'] = False
kwargsRun['rerunQuery'] = False
kwargsRun['importQuery'] = True
kwargsRun['debugLevel'] = -2
kwargsRun['debug_level'] = -2

kwargsLocal = {}
kwargsLocal['localRoot'] = '/home/userid/data/shadow/'
kwargsLocal['remote'] = False
kwargsLocal['logQuery'] = True
kwargsLocal['throttle'] = False
kwargsLocal['reLocalQuery'] = True

kwargsProductionDebug = {}
kwargsProductionDebug['remote'] = True
kwargsProductionDebug['debugLevel'] = 9
kwargsProductionDebug['logQuery'] = True
kwargsProductionDebug['throttle'] = False
kwargsProductionDebug['sshDestination'] = ''

kwargsQueryOnly = kwargsRun.copy()
kwargsQueryOnly['getQueryOnly'] = True
kwargsQueryOnly['sshDestination'] = 'userid@'

kwargsQueryMySQL = {}
#kwargsQueryMySQL['sql'] = sql#
#kwargsQueryMySQL['db'] = db#

try:
    a_ = Utilities.ShorthandArray()
except:
    a_ = numpy.array
    print('failed in shorthand array')
ic = re.IGNORECASE



machines = []
typeOfLists = numpy.array

def safe(f):
    def wrapper(args):
        try:
            output = f(args)
        except:
            return 'NONE'
        return output
    return wrapper
