# LAB - Class 19

## Project: Automation

## Author: Mike Shen

## Description:
Given a document potential-contacts, find and collect all email addresses and phone numbers.

Phone numbers may be in various formats.
- (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
- phone numbers with missing area code should presume 206
- phone numbers should be stored in xxx-yyy-zzzz format.

Once emails and phone numbers are found they should be stored in two separate documents.

The information should be sorted in ascending order.

Duplicate entries are not allowed.


## Links and Resources

[RFC 3696](https://www.rfc-editor.org/rfc/rfc3696)



## Setup

Install per requirements.txt

## How to initialize/run your application (where applicable)

From root directory, run:

python -m automation.automation

Will create two files in the automation\assets folder for email-contacts.txt and phone-contacts.txt

## How to use your library (where applicable)
N/A

## Tests

From root directory, run:

pytest
