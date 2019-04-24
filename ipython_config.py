#!/usr/bin/env python
#  vim: set fileencoding=utf-8 ff=unix tw=78 ai syn=python : per PEP 0263 
#       python 2.7.13 under Linux Ubuntu 14.04        Date : 2017-02-02
#      IPython 5.1.0   from Anaconda distribution
#
# _______________|  ipython_config.py : custom config file
#
'''
CHANGE LOG  Latest config version, see https://git.io/ipython_config.py
2017-02-02  Beautify "program" layout, cosmetic color changes: 
               this script is for configuration only, NOT startup.
               Use os.sep as directory separator for CROSS-PLATFORM.
2017-02-01  Add UTC timestamp to Out prompt.
2017-01-30  In prompt: newline indent current_directory _iN >>>
            Out prompt: indent _N timestamp_utc newline 
            Purpose is readability using the underscore abbreviations
            which can serve as variables at the command line,
            plus the results can be edited for doctests.
2017-01-29  Modify for IPython v5+, so deprecate PromptManager, and
               rewrite prompts using more tedious script and Pygments. 
            Insanity to configure PROMPTS starting from v5 of IPython, must see:
               https://github.com/ipython/ipython/issues/9388
            Adapted from @takluyver gist, circa July 2016:
            https://gist.github.com/takluyver/85b33db0836cdcc4baf252fd81937fa7
2014-07-18  First version.
'''

from IPython.terminal.prompts import Prompts, Token
from datetime import datetime
import os


c = get_config()
app = c.InteractiveShellApp

#  Use the following at any point in a config file to load a sub config
#  and merge it into the current one:
#load_subconfig('ipython_config.py', profile='default')#
#      Thus the scheme here is to OVERLAY OVER DEFAULT config.


#  ======================================================================== 
class MyPrompts(Prompts):
    def in_prompt_tokens(self, cli=None):
        truncdir = os.getcwd().split(os.sep)[-3:]
        est_nano = str(datetime.now())
        #          2017-02-01 13:46:27.260500
        est = est_nano.split('.')[0]
        #          2017-02-01 13:46:27
        #  truncated list of last parts of the current working directory
        return [
            (Token, u'\n'),
            (Token.Prompt, u''),
            (Token.Prompt, est),
            #(Token.Prompt, os.sep.join(truncdir)),#
						(Token.Prompt, u'_i:'),
            (Token.PromptNum, str(self.shell.execution_count)),
            (Token.Prompt, u' >>> '),
        ]
    
    def continuation_prompt_tokens(self, cli=None, width=None):
        if width is None:
            width = 4
            #width = self._width()#
        return [
            (Token.Prompt, (' ' * (width - 2)) + u'│ '),
        ]

    def out_prompt_tokens(self):
        est_nano = str(datetime.now())
        #          2017-02-01 13:46:27.260500
        est = est_nano.split('.')[0]
        return [
            (Token.OutPrompt, u'_ '),
            (Token.OutPromptNum, str(self.shell.execution_count)),
            (Token.Prompt, est),
            (Token, u' \n'),
        ]

#  Use IPython v5+ new API:
c.TerminalInteractiveShell.prompts_class = MyPrompts

#  Alternative: get "--classic" style PROMPTS by executing, "%doctest_mode"
#  ======================================================================== 



#  Original 2014 settings...
#c.InteractiveShell.separate_in = ''#
#c.InteractiveShell.separate_out = ''#
#c.InteractiveShell.separate_out2 = ''#


# 2017-01-29 Try v5 COLORS:
c.InteractiveShell.colors = 'lightbg'
#  'linux' is optimised for dark backgrounds.
#c.InteractiveShell.highlighting_style = 'native'#
#  'native' and 'paraiso-dark' are some compatible Pygments color schemes.


#  2014-07-18  gvim will not work with terminal.
c.TerminalInteractiveShell.editor = "vim"
#  2017-01-29  IPython 5.2 will invoke $EDITOR by F2 key. @takluyver

#  2017-01-29  .inputrc for readline ineffective as of IPython 5.0, fix:
c.TerminalInteractiveShell.editing_mode = 'vi'

#  "MULTILINE EDITING [v5 new feature] means that if you type e.g. 
#      for a in rage(5):<enter>
#  you can press up-arrow and go back to the line above, 
#  without having to cancel the input."

c.PrefilterManager.multi_line_specials = True


#  2014-07-18  For modified modules  AUTORELOAD
c.InteractiveShellApp.extensions = ['autoreload']
#  See also use of %reload and %dreload

dataPath = '/data/home'
homePath = '/home'
scmPath = 'scm/github/projects/machineConfigs'

c.InteractiveShellApp.exec_lines = [
    'from __future__ import division',
    'import scipy',
    '%alias_magic hsit hist',
    '%alias_magic h hist',
    '%load_ext autoreload',
    '%autoreload 2',
    '%autocall 1',
		'import ipyparallel as ipp',
		'PYHOME_LOCAL = "%s/psmith/python/"'%(homePath),
		'PYHOME = "%s/psmith/%s/"'%(homePath, scmPath),
		'%run -i {PYHOME}/startup.ipy'
]

c.InteractiveShellApp.exec_files= [
        '%s/psmith/%s/settings.py'%(homePath, scmPath),
        '%s/psmith/%s/startup3.py'%(homePath, scmPath),
]
#            _____ ADDITIONAL "lines"
#
#  Once you run %rehashx, all of your $PATH has been loaded as IPython
#  aliases, so you should be able to type any normal system command and have
#  it executed. See %alias? and %unalias? for details on the alias facilities.

lines = """
%rehashx
dataPath = '/data/home'
homePath = '/home'
scmPath = 'scm/github/projects/machineConfigs'

"""

app.exec_lines.append(lines)


