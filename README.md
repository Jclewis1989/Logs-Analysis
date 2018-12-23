# Logs-Analysis
A python application providing three queries, each pulling information from an SQL database

## The Virtual Machine

VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

**Ubuntu** users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

## Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](vagrantup.com). Install the version for your operating system.

**Windows** users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Download the VM configuration
There are a couple of different ways you can download the VM configuration.

* You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

* Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. **Change directory to the vagrant directory:**



## Download the data
Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)

To load the data, cd into the vagrant directory and use the command ``` psql -d news -f newsdata.sql ```.
Here's what this command does:

* ``` psql ``` — the PostgreSQL command line program
* ``` -d news ``` — connect to the database named news which has been set up for you
* ``` -f newsdata.sql ``` — run the SQL statements in the file newsdata.sql
* Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Getting an error?
If this command gives an error message, such as —
``` psql: FATAL: database "news" does not exist ```
``` psql: could not connect to server: Connection refused ```
* — this means the database server is not running or is not set up correctly. This can happen if you have an older version of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.

## Explore the data
Once you have the data loaded into your database, connect to your database using psql -d news and explore the tables using the \dt and \d table commands and select statements.

* ``` \dt ``` — display tables — lists the tables that are available in the database.
* ``` \d table ``` — (replace table with the name of a table) — shows the database schema for that particular table.
* Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

* The ``` authors ``` table includes information about the authors of articles.
* The ``` articles ``` table includes the articles themselves.
* The ``` log ``` table includes one entry for each time a user has accessed the site.
As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

## Connecting from your code
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

``` db = psycopg2.connect("dbname=news") ```