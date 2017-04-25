# Web Scrawler for retrieving data from container-ship.com

======

One of my friends asked me if there is any way to retrieve data from [http://www.containership-info.com].
Firstly I thought about Selenium, but taking into account it is not a quite complex site, and I had no idea about Python3 and Scrapy I decided to test them out.
This repository contains my tiny script to process and retrieve data from [http://www.containership-info.com] so it can be added to any other editor for processing.
## Requirements
* Python3
* Scrapy
## Installation
I suggest to create a virtual environment and run script from it.
During installation scrapy will need libssl-dev package (at least it is called so on my Debian system), so just install it in advance.
Simple commands you may use to run everything as fast as possible:

`sudo apt-get install libssl-dev`

`virtualenv --python3 venv`

`. venv/bin/activate`

`pip install -f < requirements.txt`
## Usage
This script supports default scrappy's behaviour, so:
* To run script as it is `scrapy runspider containership_parser.py`
* To store data as CSV: `scrapy runspider containership_parser.py -o container.csv -t csv`
