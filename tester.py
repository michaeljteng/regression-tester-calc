#!/usr/bin/env python
import subprocess
from string import rstrip
import sys

def main():
  if len(sys.argv) <= 1:
    usage()  
  else:
    suite = sys.argv[1]
    tests = map(int, sys.argv[2:])
    if suite == 'arith' or suite == 'parse':
      test(suite, tests)
    elif suite == 'all':
      test('arith', tests)
      test('parse', tests)
    else:
      usage()

def usage():
  ab = open('./arith-suite/arith-baselines.txt', 'r')
  pb = open('./parse-suite/parse-baselines.txt', 'r')
  abase = map(rstrip, ab.readlines())
  pbase = map(rstrip, pb.readlines())
  print "Regression Tester for Calculator"
  print "\nusage: ./tester [suite] [tests ..]\n"
  print "arguments: suite         must specify one of suites, or use 'all'"
  print "                         current test suites are: arith, parse"
  print "           tests         use integers to denote subset of suite to test"
  print "                         note: using option 0 will update without running tests"
  print "                         current arith tests include:"
  print "                             0 - use this option to update baseline"
  i = 0
  while i < len(abase):
    print "                             " + str(i/2 + 1) + " - " + str(abase[i])
    i += 2
  print "                         current parse tests include:"
  print "                             0 - use this option to update baseline"
  i = 0
  while i < len(pbase):
    print "                             " + str(i/2 + 1) + " - " + str(pbase[i])
    i += 2
  ab.close()
  pb.close() 
    

def test(suite, tests):

  print "--------------------------------------------------\n"
  print "\nRunning the "+ suite + " suite on calculator program"
  subprocess.call("./"+ suite +"-suite/" +suite + "-tests.sh", shell=True)

  f = open('./' + suite + '-suite/'+ suite +'-results.txt','r')
  fbase = open('./' + suite + '-suite/'+ suite +'-baselines.txt', 'r+')

  results = map(rstrip, f.readlines())
  old = map(rstrip, fbase.readlines())
  i = 0
  update = False
  
  regressions = []
  baselines = []

  if 0 in tests:
    update = True
  while i < len(results):
    if not tests or i/2 + 1 in tests:
      print str(results[i])
      print "Result of " +suite +" test " + str(i/2 + 1) + ": " + str(results[i+1])
      if (" ".join(results[i].split("expecting")[1:]) != " " +results[i+1]):
        print "Test case failed!"
        regressions.append((str(i/2 + 1), str(results[i+1]), 'failed'))
      else:
        print "Test case passed!"
        regressions.append((str(i/2 + 1), str(results[i+1]), 'success'))
      if (" ".join(old[i].split("expecting")[1:]) != " " +old[i+1]):
        baselines.append((str(i/2 + 1), str(old[i+1]), 'failed'))
      else:
        baselines.append((str(i/2 + 1), str(old[i+1]), 'success'))

      print "------"
    i += 2
  
  print "--------------------------------------------------\n"
  print "\nRunning the regressions analysis on " + suite + " suite"

  counter = 0

  for i in xrange(len(regressions)):
    (x,y,z) = regressions[i]
    (a,b,c) = baselines[i]
    
    print "------"
    print "New test " + str(x) + " results:"
    print y +', '+z
    print "Baseline test "+ str(a)+ " results:"
    print b+', '+c
    print '\n'
    if c != z:
      if c == 'success':
        print "Changes to code has introduced a new bug!"
        print "Test number " + str(a) + " for the " + suite + " suite originally passes, but now fails"
      if c == 'failed':
        print "Changes to code has fixed a bug!"
        print "Test number " + str(a) + " for the " + suite + " suite originally fails, but now passes"
        print "Recommend running test suite with option 0 to store new baseline"

  print "--------------------------------------------------\n"
  if update == True:
    print "Updating the test suite baseline results" 
    subprocess.call("./"+ suite +"-suite/" +suite + "-bases.sh", shell=True)

  print "--------------------------------------------------\n"

if __name__ == "__main__":
  main()
