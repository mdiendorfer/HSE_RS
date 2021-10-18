# HSE - Research Seminar - Homework 3 RPA

**Date**: 18.10.2021
**Recording**: https://www.loom.com/share/c845ab430ce74c1a9339b3c4ca86c1aa

## ResearchGate robot description

The robot is used to automate the process of https://www.semanticscholar.org/ (or https://www.researchgate.net/) literature collection for the user-defined topic. Result of the process is an email with attached excel with info about each found article, and also downloaded PDF files of the 

### Used libraries

* [selenium](https://selenium-python.readthedocs.io/) - web-browser automation
* [pandas](https://pandas.pydata.org/) - work with datatables
* [smtplib](https://docs.python.org/3/library/smtplib.html) \ [email](https://docs.python.org/3/library/email.examples.html) - email creating and sending
* wcm - function for working with Windows credential manager
* [keyring](https://pypi.org/project/keyring/) - for the management of the email credentials

### Algorithm 

1. User defines a topic, number of pages, and receiver of the resulting email
2. Robot creates links for each search results page
3. Robot collects links to the articles from each page
4. Robot scraps article's info and downloads source docs if available
5. Robot writes all info to excel and sends email

### How to use

1. Open the files in an IDE
2. change the configuration in the "conf.py" file (included the configuration for keyring)
3. run the "main.py" file
4. watch how the program is working and see if you get an email with attached file and also downloaded files
