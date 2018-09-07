# -*- coding: utf-8 -*-
# @Time    : 2018/8/10 15:00
# @Author  : Lsp

import os

ADJECTIVE = 'ADJECTIVE'
NOUN = 'NOUN'
ADVERB = 'ADVERB'
VERB = 'VERB'
s = 'The %s panda walked to the %s and then %s. A nearby %s was unaffected by these events.' % (
	ADJECTIVE, NOUN, ADVERB, VERB)
print(s)
print('Enter an %s :' % ADJECTIVE.lower())
ADJECTIVE = str(input())
print('Enter a %s :' % NOUN.lower())
NOUN = str(input())
print('Enter a %s :' % ADVERB.lower())
ADVERB = str(input())
print('Enter a %s :' % VERB.lower())
VERB = str(input())
s = 'The %s panda walked to the %s and then %s. A nearby %s was unaffected by these events.' % (
	ADJECTIVE, NOUN, ADVERB, VERB)
print(s)
with open(r'D:\madlibs.txt', 'w', encoding='utf-8') as f:
	f.write(s)
f.close()
