# NEWS DATA LOG ANALYSIS
This is a simple CLI report to get a feel for what is trending and how the News Data website is being utilized by viewers.
This project uses a mock PostgreSQL database for fictional views of a news website.  The provided python script, "newsdata_db-v3.py" uses the psycopg2 library to query the database and produce answers to the following questions:

## The News Data Log Analysis uses the logs of viewer activity to answer the following questions:

1. What are the most popular three articles of all time? 
	* Which articles have been accessed the most? 

2. Who are the most popular article authors of all time? 
	* That is, when you sum up all of the articles each author has written, which authors get the most page views?

3. On which days did more than 1% of requests lead to errors?


### REQUIREMENTS:
To run the database analysis, you will need to install the following programs on your computer.
1. [Vagrant](https://www.vagrantup.com/downloads.html) See instructions below.
2. [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1]) See instructions below.
3. Follow this [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to get a zip file of the SQL script that will create the database. Make sure to save this file in the chosen folder for this project.

### INSTALL VAGRANT
Download Vagrant from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

* Check your install by typing `vagrant --version`.  If installed correctly this should return the version number of your vagrant install.

### INSTALL VIRTUALBOX
Vagrant runs on top of VirtualBox. VirtualBox is the software that actually runs the virtual machine.  Go to [virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install it.  Install the platform package for your operating system.  You do not need the extension pack or the SDK. Also, you do not need to launch VirtualBox after installing it. Vagrant will launch the VirtualBox for you.

### SET UP YOUR FOLDER
Now you are ready to set up your folder. We will run Vagrant within this folder to access the news database and run our reports.
1. Make sure all of the provided files are in your selected folder. The zip file includes the following:
    * README.md - This is what you are reading.  :-)
    * newsdata.sql - This will create the database
    * newsdata_db-v3.py - This is the program that will create a report of the news database for you in the command line.
    * Vagrantfile - This file will be used by Vagrant to set your environment.

2. Now that all of the required files are in the folder we are ready to create the Vagrant environment. This will provide a stable environment to work within despite what may be on the rest of your computer and install dependencies needed for our database and reporting.
    * Run `vagrant init` in the command line from within your chosen file.
    * Now you can start the Vagrant environment with `vagrant up`.  Please note this step may take a while as it uses the Vagrantfile to download the appropriate dependencies.
    * Once `vagrant up` has finished you'll need to SSH into the Vagrant environtment using `vagrant ssh`.
    * Now you are in your new Linux VM! Follow the prompts to `cd /vagrant` to access the files within the Virtual Machine.

### SET UP THE DATABASE:
Once you have the requirements installed you can begin to set up the database.
* First, check that the install succeeded by typing `psql`. This will return your PostgreSQL version.
* Next, you'll want to run the SQL script to create the database. (Make sure to do this in the same folder as this README.md file and the newsdata_db-v3.py files.)
Run `psql -d news -f newsdata.sql` in the command line.
* Now you're ready to start exploring the the news data by running the Log Analysis Report!


### RUNNING A LOG ANALYSIS REPORT:
Run the Log Analysis Report in the command line by typing the following script:
`python newsdata_db-v3.py`
