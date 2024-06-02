[![python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org)
![Repo Size](https://img.shields.io/github/repo-size/Sulstice/global-chem)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Simple script to test the Cisco Genie parser

This script will parse the data in a text file containing the output of a "show" command.
The Genie library will parse the command into a Python dictionary and print it in the terminal.
Additionally, it will store the parsed data in a text file.

The script can be used to quickly map the structure of the data after it has been parsed.

## Getting Started

### Prerequisites

Before installing the software, ensure you have the following prerequisites:

 * Linux Environment: The script utilizes the pyATS Genie library for parsing, which is only supported on Linux platforms.
 * Python Version: The code is developed in Python 3.11.0rc1. Although it has not been tested on other versions, newer versions should generally be compatible.

### Installation

Go to the directory where you intend to save the repository and execute the following command:

```
git clone https://github.com/tmalbrecht/genie-test-parser.git
```

Move into the directory and setup a Python virtual environment:

```
cd genie-test-parser
python3 -m venv venv 
source venv/bin/activate
```

Install all required libraries:

```
pip install pyats-genie-command-parse
```

Check the link below for the pypi page from the library used to parse the commands:
https://pypi.org/project/pyats-genie-command-parse/

Check the link below to see all available parsed commands in the Genie library:
https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/?ref=packetswitch.co.uk#/parsers


## Usage

Navigate into the project directory and execute main.py:

```
python genie-test-parser.py
```

You can easily modify the script to test your own show commands. Simply update the text file(s) with the output from your show commands. Remember to also adjust the show command in the code accordingly.

