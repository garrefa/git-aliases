#!/usr/bin/env python

import re

def printBanner():
  print "README.MD Generator\n"
  print "---"

def readFile(fname):
  f = open(fname)
  content = f.read().splitlines()
  f.close()
  return content

def getDescriptionLinesInFile(lines):
  content = []
  pattern = re.compile('^\s*#.*$')
  replace_pattern = re.compile('^\s*#\s*')
  for line in lines:
    match = re.match(pattern,line)
    if match :
      temp = re.sub(replace_pattern, line, 1)
      content.append(temp)
  print content

if __name__ == '__main__':
  printBanner()
  file_content = readFile('all.gitconfig')
  getDescriptionLinesInFile(file_content)
