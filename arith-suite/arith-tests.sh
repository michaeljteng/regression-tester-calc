#!/bin/bash

rm ./arith-suite/arith-results.txt
touch ./arith-suite/arith-results.txt


echo "Testing '3 ^ 4', expecting 81.000000" >> ./arith-suite/arith-results.txt
./calculator/calc 3 ^ 4 >> ./arith-suite/arith-results.txt
echo "Testing '2 + 5', expecting 7.000000" >> ./arith-suite/arith-results.txt
./calculator/calc 2 + 5 >> ./arith-suite/arith-results.txt
echo "Testing '31 / 4', expecting 0.666667" >> ./arith-suite/arith-results.txt
./calculator/calc 31 % 4 >> ./arith-suite/arith-results.txt
echo "Testing '6 * 8', expecting 48.000000" >> ./arith-suite/arith-results.txt
./calculator/calc 6 * 8 >> ./arith-suite/arith-results.txt
echo "Testing '10 - 13', expecting -3.000000" >> ./arith-suite/arith-results.txt
./calculator/calc 10 - 13 >> ./arith-suite/arith-results.txt
echo "Testing '9 % 7', expecting 2.000000" >> ./arith-suite/arith-results.txt
./calculator/calc 9 % 7 >> ./arith-suite/arith-results.txt
