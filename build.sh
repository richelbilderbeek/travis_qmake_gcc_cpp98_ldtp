#!/bin/bash
qmake
make
# ./travis_qmake_gcc_cpp98_ldtp # Do not run this on Travis, as it prompts the user for input