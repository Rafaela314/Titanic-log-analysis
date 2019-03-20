# Log Analisys Project
This is a project for [Udacity’s Full Stack Web Developer Nanodegree](https://br.udacity.com/course/full-stack-web-developer-nanodegree--nd004). This projects involved SQL queries and a Python reporting tool to answer specific questions.

## Project Description:

The assigned task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Questions to Answer:

1.	**What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
2.	**Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3.	**On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## This Project Requires a Bit of Setup: 
This project runs in a Linux-based virtual machine (VM) created using Vagrant.

### Environment dependencies:
- Python 2.7
- PostgreSQL
- psycopg2

### PreRequisite Installations:
- Install [Vagrant](https://www.vagrantup.com/downloads.html)
- Install [Virtual Box plataform package and the Extension Pack](https://www.virtualbox.org/wiki/Downloads)
- Clone the [vagrant setup files](https://github.com/udacity/fullstack-nanodegree-vm) from Udacity's Github to a directory of your choice. These files configure the virtual machine and install all the tools needed to run this project.
- Download the database set up [newsdata.sql](1.https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
) (extract from **newsdata.zip**) 
- Download this project: log_analysis.py
- Move the file to your **vagrant** directory within Virtual Machine.

### Required SQl views
This program uses four SQL views

**1) total_requests**
```
create view total_requests
as select date_trunc('day',time) as day, count(*) as totals
from log
group by day
```
**2) error_requests**
```
crete view error_requests as select date_trunc('day',time) as day, count(*) as errors
from log
where status LIKE '404%'
group by day
```
**3) percent**
```
create view percent as select total_requests.day,
total_requests.totals as numall,
error_requests.errors as numerror,
error_requests.errors::double precision/total_requests.totals ::double precision * 100 AS percentage_error
from total_requests, error_requests
where total_requests.day= error_requests.day;
```

### Start the Virtual Machine:
Open terminal, navigate to the folder where your vagrant is installed in and run these commands:
1. Run `vagrant up` to build the VM for the first time
2. Once It os built, `vagrant ssh` to log into the VM
3. `cd /vagrant` to change to your vagrant directory
4. `psql -d news -f newsdata.sql` to load the data
5. `psql -d news` to connect to database
6. **Enter the views listed above**
7. `exit` to quit psql module
8. `python log_analysis.py` to run the reporting tool