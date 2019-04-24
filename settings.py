import logging
import numpy
import math
import sys
import os
declaredLogLevel = int((os.environ.get('logLevel')) or logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(declaredLogLevel)
import glob

scp_command = ''
platform = ''

if sys.platform.find('linux')>=0:
	try:
		ssh_command
	except NameError:
		ssh_command = 'ssh'
	ssh_options = ''
	scp_command = 'scp'
	del_command = '/bin/rm'
elif sys.platform.find('win')>=0:
	try:
		ssh_command
	except NameError:
		ssh_command = 'plink'
	ssh_options = ''
	scp_command = 'pscp'
	del_command = 'del'


def IsWindows():
	if sys.platform.find('linux')>=0:
		return False
	elif sys.platform.find('win')>=0:
		return True

def IsLinux():
	if sys.platform.find('linux')>=0:
		return True 
	elif sys.platform.find('win')>=0:
		return False 



def eng_string( x, format='%.4f', si=False):
		'''
		Returns float/int value <x> formatted in a simplified engineering format -
		using an exponent that is a multiple of 3.

		format: printf-style string used to format the value before the exponent.

		si: if true, use SI suffix for exponent, e.g. k instead of e3, n instead of
		e-9 etc.

		E.g. with format='%.2f':
				1.23e-08 => 12.30e-9
						 123 => 123.00
					1230.0 => 1.23e3
			-1230000.0 => -1.23e6

		and with si=True:
					1230.0 => 1.23k
			-1230000.0 => -1.23M
		'''
		x = numpy.float64(x)
		sign = ''
		if x < 0:
				x = -x
				sign = '-'
		exp = int( math.floor( math.log10( x)))
		exp3 = exp - ( exp % 3)
		x3 = x / ( 10 ** exp3)

		if si and exp3 >= -24 and exp3 <= 24 and exp3 != 0:
				exp3_text = 'yzafpnum kMGTPEZY'[ ( exp3 - (-24)) / 3]
		elif exp3 == 0:
				exp3_text = ''
		else:
				exp3_text = 'e%s' % exp3

		return ( '%s'+format+'%s') % ( sign, x3, exp3_text)

