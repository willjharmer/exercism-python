+++
date = "2016-03-15"
draft = false
title = "Usage"
weight = 2
+++

In order to run the tests or use the code, you will need to install Python 3.5. I prefer to use conda from continuum analytics to manage my Python versions and development and production environments. To install and the tests with conda, do the following:


```bash
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
  bash miniconda.sh -b -p $HOME/miniconda
  export PATH="$HOME/miniconda/bin:$PATH"
  hash -r
  conda config --set always_yes yes --set changeps1 no
  conda update -q conda
  conda info -a
  conda env create -q QUIET --file environment.yml
  source activate exercism

  nosetests */*_test.py
```

