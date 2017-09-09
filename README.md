# Findtrip - Flight ticket spider

## Introduction
Fork from https://github.com/fankcoder/findtrip

Findtrip is a webspider for flight tickets by Scrapy, which contains major china ticket websites ---- Ctrip

Upgrade the code to adjust the ctrip website @ Sep 2017. Revise the structure for the result.

## Installation
```
git clone https://github.com/chckn/findtrip.git
```

## Requirement
./requirements.txt

Using selenium+ phantomjs

Get phantomjs from http://phantomjs.org/, the install package on apt is not the complete one.


## Execution

scrapy crawl Ctrip -o [FILENAME] --logfile=[LOGNAME]


