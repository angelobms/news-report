# news-report
Report of news

The program is created using:
+ [Python](https://www.python.org/) in the version 3;
+ [Flask](http://flask.pocoo.org/);
+ [Psycopg](http://initd.org/psycopg/).


# Prerequisites
+ You must have [Python](https://www.python.org/downloads/) installed;
+ You must have [Vagrant](https://www.vagrantup.com/) installed;
+ You must have [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
installed.


# Setup the VirtualBox
VirtualBox is the software that actually runs the virtual machine.
Download and install the platform package for your operating system.
You do not need the extension package or the SDK.
You do not need to start VirtualBox after installing it.
Vagrant will do that.

If you are running Ubuntu 14.04 install VirtualBox using the Ubuntu Software
Center instead. Due to a reported bug, installing VirtualBox from the site
can uninstall other software you need.


# Setup the Vagrant
Vagrant is the software that configures the VM and allows you to share files
between your host computer and the VM's file system. Download and install
the version of your operating system.

For installation on a Windows operating system the installer may ask you to
give network permissions to Vagrant or to make an exception in the firewall.
Be sure to allow this.

If Vagrant is successfully installed, you will be able to run
```vagrant --version``` on your terminal to see the version number.
The shell prompt on your terminal may be different. In the Linux, the
```$``` sign is the shell prompt.


# Config the VM
+ Copy and clone the repository
https://github.com/udacity/fullstack-nanodegree-vm
+ Change to the vargranfullstack-nanodegree-vm directory on your terminal
with ```cd/vargranfullstack-nanodegree-vm```
+ Change the directory to the vagrant directory: ```cd vagrant/ ```
+ Run the command ```vagrant up``` to start the virtual machine
+ Copy and clone the repository https://github.com/angelobms/news - report
inside the directory vagrant
+ Run ```vagrant ssh``` to log me on your newly installed Linux VM!


# Logging in and logging out
If you type ```exit``` (or Ctrl - D) at the shell prompt inside the VM, you
are logged off, and placed back in the shell of your host computer. To log
back in, make sure you are in the same directory and type ```vagrant ssh```
again.

If you restart your computer, you will need to run ```vagrant up``` to
restart the VM.


# Running the database
The PostgreSQL database server will automatically be started inside the VM.
You can use the ```psql``` command-line tool to access and execute SQL
statements. The Access to the database is performed with the user
```vagrant``` and password ```secret``` credential.


# Downloading the data
+ Download the data that will be used by the project
[here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August
/57b5f748_newsdata/newsdata.zip);
+ Unzip the ```newsdata.sql``` file in the ```vagrant``` directory
that is shared with the virtual machine;
+ Run the command ```psql - d news - f newsdata.sql```
(Executing this command will connect you to your installed database server
and execute the SQL commands on the downloaded file, creating tables and
populating them with data);
+ Run the command ```\c news``` to access the database news;
+ Run the command ```CREATE VIEW qtdStatusOkByTime AS SELECT DATE(time),
COUNT(status) AS qtd FROM log WHERE status = '200 OK' GROUP BY DATE(time)
ORDER BY qtd DESC``` to create the view ```qtdStatusOkByTime```
in the database ```news```.

# Runnig the news-report project

+ Inside the VM, change the directory to ``` /vagrant```;
+ Change the directory to the news - report directory: ```cd news-report/```;
+ Execute ```python news.py``` in the shell prompt on your terminal;
+ Open the link http://0.0.0.0:8000/ in bowser.


# Author
Angelo Brandão - angelobms@gmail.com
