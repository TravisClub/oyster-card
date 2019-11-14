# Oyster Card System
Oyster Card System developed using Python

# The problem
You are required to model the following fare card system which is a limited version of London’s Oyster card system. At the end, you should be able to demonstrate a user loading a card with £30, and taking the following trips, and then viewing the balance.

- Tube Holborn to Earl’s Court
- 328 bus from Earl’s Court to Chelsea
- Tube Earl’s court to Hammersmith

# Installation
Follow these steps to setup the project

1 - Install dev prereqs (use equivalent linux or windows pkg mgmt)
----

    brew install python3.6
    brew install virtualenv


2 - Set up a Python virtual environment (from project root directory)
----

    make venv
    source venv/bin/activate


3 - Install required python packages into the virtual env
----
    make init


4 - Run the tests from project root directory
----
    . scripts/code-coverage.sh


5 - Run the code
----
    python oyster/oyster_card.py



