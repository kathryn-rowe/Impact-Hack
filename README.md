# Hey Congress!

Impact Hackathon hosted by General Assembly.

:star: Winner, Best Overall :star:

Team Members: Peter Travis, Zoe Shirah Gotch-Strain, Rocio, Kurt Bodden, Sam Colman, and Kathryn Rowe

Problem Statement: How do we create a better connection between members of Congress and the general public?

We created a central platform where Voters can inform themselves and express opinons about upcoming legislation. It is also a place where Representatives can directly see the desires of their constituents. After a bill is passed or defeated, voters can hold their representatives accountable and compare their views.

# Tech stack
Backend: Python, Flask, PostgreSQL

Frontend: HTML5, CSS, Bootstrap

Data and APIs: Data.gov, hoping to use Pro Publica API, but could not get API key in one day.

## Features

Homepage: sign-up or sign-in to directly see your Representatives.

![alt text](https://github.com/kathryn-rowe/Impact-Hack/blob/master/static/images/homepage.jpg "Homepage")

Complete survey to vote on issues that matter to you.

![alt text](https://github.com/kathryn-rowe/Impact-Hack/blob/master/static/images/Voting%20Page.png "Issues Page")

Vote on upcoming legislation.

![alt text](https://github.com/kathryn-rowe/Impact-Hack/blob/master/static/images/Voting%20Page-3.png "Vote Page")

See how other consituents in your district voted.

![alt text](https://github.com/kathryn-rowe/Impact-Hack/blob/master/static/images/Results.png "Results Page")

### Setup/Installation

Install requirements to run locally.

Clone repository:

```sh
$ git clone https://github.com/kathryn-rowe/Impact-Hack.git
```
Create virtual environment:

```sh
$ virtualenv env
```
Activate virtual environment:
```sh
$ source env/bin/activate
```
Install dependencies:
```sh
$ pip install -r requirements.txt
```
Create necessary secret keys for Flask. Save to secrets file and source secrets to env.

Create database 'voter_data'
```sh
$ createdb voter_data
```
Create tables and seed example data running seed.py. Be sure to uncomment final lines in seed.py.
```sh
$ python seed.py
```
If you want to use SQLAlchemy to query the database, run in interactive mode
```sh
$ python -i model.py
```

### Todos

 - We finished design process of project, but not full implementation. 
 - Write tests.

Other goals for project:
 - Be able to sort/filter voting results
 - Use API to obtain current bills 
 - Add on lobbying feature
 - Implement security into the app
 - Direct messages to members of congress
 - Registration as a member of congress


License
----

Copyright 2017 Kathryn Rowe

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [ebird]: <http://ebird.org/content/ebird/>

