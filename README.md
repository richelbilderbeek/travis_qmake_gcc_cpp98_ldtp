# travis_qmake_gcc_cpp98_ldtp

[![Travis CI logo](TravisCI.png)](https://travis-ci.org)

[![Build Status](https://travis-ci.org/richelbilderbeek/travis_qmake_gcc_cpp98_ldtp.svg?branch=master)](https://travis-ci.org/richelbilderbeek/travis_qmake_gcc_cpp98_ldtp)

This GitHub is part of [the Travis C++ Tutorial](https://github.com/richelbilderbeek/travis_cpp_tutorial).

I could not get LDTP to work on this console application. Please send me an email if you know how.

The goal of this project is to have a clean Travis CI build, with specs:
 * Build system: `qmake`
 * C++ compiler: `gcc`
 * C++ version: `C++98`
 * Libraries: `STL` only
 * Code coverage: none
 * UI testing: yes, using LDTP
 * Source: one single file, `main.cpp`

More complex builds:
 * Use of C++11: [travis_qmake_gcc_cpp11_ldtp](https://www.github.com/richelbilderbeek/travis_qmake_gcc_cpp11_ldtp)
 * Use of C++14: [travis_qmake_gcc_cpp14_ldtp](https://www.github.com/richelbilderbeek/travis_qmake_gcc_cpp14_ldtp)
