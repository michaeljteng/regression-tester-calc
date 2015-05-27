#!/bin/bash

rm ./parse-suite/parse-results.txt
touch ./parse-suite/parse-results.txt


echo "Testing 'x = 3 + 4', expecting Assigned to x: 7.000000" >> ./parse-suite/parse-results.txt
./calculator/calc x = 3 + 4 >> ./parse-suite/parse-results.txt
#echo "Testing 'x = asdf', expecting Error: Tried to assign non-number to x." >> ./parse-suite/parse-results.txt
#./calculator/calc x = asdf >> ./parse-suite/parse-results.txt
#echo "Testing '$', expecting Parse error after: $" >> ./parse-suite/parse-results.txt
#./calculator/calc $ >> ./parse-suite/parse-results.txt
echo "Testing 'x ^ 3', expecting Variable 'x' ^ 3" >> ./parse-suite/parse-results.txt
./calculator/calc x ^ 3 >> ./parse-suite/parse-results.txt
echo "Testing '2 ^ 2 ^ 3', expecting 256.000000" >> ./parse-suite/parse-results.txt
./calculator/calc 2 ^ 2 ^ 3 >> ./parse-suite/parse-results.txt
echo "Testing '-3 + --4', expecting 1.000000" >> ./parse-suite/parse-results.txt
./calculator/calc -3 + --4 >> ./parse-suite/parse-results.txt
echo "Testing '(2 + 3) / (6 + 4)', expecting 0.500000" >> ./parse-suite/parse-results.txt
./calculator/calc \(2 + 3\) / \(6 + 4\) >> ./parse-suite/parse-results.txt
