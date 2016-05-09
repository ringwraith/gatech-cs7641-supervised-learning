# gatech-cs7641-supervised-learning
Code and datasets for Georgia Tech's CS7641 Spring 2016 Supervised Learning project.

## Source Code

Source code and supporting data for this machine learning analysis can be found at [this public Github repo](https://github.com/stormont/gatech-cs7641-supervised-learning).

## Weka

This analysis used Weka (version 3.6.13) running on Mac OS X, available [here](http://www.cs.waikato.ac.nz/ml/weka/downloading.html).

## Data Sets

Two data sets were used for classification, both from the UCI Machine Learning Repository.

The first data set, Nursery, was used to analyze the learning capabilities of various machine learning
algorithms on a classification problem related to school applications with features that emphasize
discrete background information of applicants. The full description of the Nursery data set can be
found [here](https://archive.ics.uci.edu/ml/datasets/Nursery).

The second data set, Low Resolution Spectrometer, was used to analyze the learning capabilities of
machine learning algorithms on classification of scientific data (primarily, wavelength data). The
full Spectrometer data set can be found [here](https://archive.ics.uci.edu/ml/datasets/Low+Resolution+Spectrometer).

The original, unmodified data sets can be found under `datasets/original_UCI_datasets/` in this
Github repo, in .arff format (compatible with Weka).

Each of these data sets were divided into separate training and test sets, following the guidance
provided by [this guide on Weka](https://weka.wikispaces.com/How+do+I+divide+a+dataset+into+training+and+test+set%3F). 
Both data sets had instances split 80% into a training set and 20% into a test set. Further, each
training set was then split into segments, varying from 10% to 100% of the training instances, in
10% increments.

The processed data sets can be found under `datasets/nursery/` and `datasets/spectrometer/` in this
Github repo, with self-descriptive naming reflective of these modifications.

## Algorithm Analysis

Five different machine learning algorithms were each run against all variants of these data sets
(with two separate kernels used in the Support Vector analysis). The output of each analysis was
written to a text file that can be found in the following hierarchy:
 * `{DATA_SET}/{ALGORITHM}/{RESULT}.txt`
 * `{DATA_SET}/{ALGORITHM}/{KERNEL}/{RESULT}.txt` (for Support Vectors)

To run these analyses, a Python (version 2.7) script can be run. It will locate and execute the
individual Weka commands used for the individual analyses, then output the result in the same
directory as each analysis.

This script can be found under `pyrunner/runner.py`. When run from the root level directory of
this Github repo, it will search for the individual `_to_run*.txt` files throughout this repo
and it will run the individual Weka commands listed therein.

**It is vital that the `weka.jar` file can be found using this Python script from a sibling
directory immediately above the level of this Github repo!** For instance, if this repo is at
`dir1/this_repo/`, the Weka installation should be located at
`dir1/weka/weka-3-6-13/weka.jar`.
