.. _Changelog:

*********
Changelog
*********

All notable changes to the master branch of this project should be documented
clearly in this file. In progress (development branch) changes can be listed
under Unreleased.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

------------------------------------------------------------------------

Unreleased (development)
========================

v0.2.0
------

:Date: 2019-11-25

Changed
^^^^^^^
* Updated setup.py, for successful package building

Added
^^^^^
* Added loops to handle multiple input files and multiple output configs per
  input
* Table manipulation functions - these are called if arguments are supplied in
  the config file. This is not scalable, as functions are hard coded with if 
  statements to check for arguments.
* .ini configuration file, within package files.


:Date: 2019-12-30

Added
^^^^^
* mappers.py module, to allow global access to label_map variable. This
  variable is updated and used across the system.
* new variable names (from recode_to_binary) are appended to global label_map.
* Before tables are written to excel sheets, the variable labels are replaced
  with long meaningful labels from label_map.

Changed
^^^^^^^
* Table manipulation functions are now called dynamically, as specified in
  configuration files. Parameters (kwargs) are also specified explicitly in
  config.
* Moved count_table function to table_types.py, so that type of output table
  can be dynamically specified via config file.
* Refined produce_table and produce_subtable, to take instructions from the
  output config files.
* configuration from .ini to YAML, which is now read from a sibling directory
  to the input data. One config file is needed per required output file.
* Deleted debug log statements in table manipulation functions, in favour for
  one generec log call that outputs the function name and all input parameters.



------------------------------------------------------------------------

Released (master)
=================

v0.1.0
------
:Date: 2020-01-01


Added
^^^^^
* package directory structure (with init.py files)
* sphinx autodocumentation in docs directory
* blank `setup.py`
