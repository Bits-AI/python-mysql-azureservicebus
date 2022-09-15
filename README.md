# Simple background script for MySQL-AzureServiceBus written in Python
Just a sample script to send data from MySQL database to Azure Service Bus written in Python.

<br />

Description
======
Sample script written in Python for sending messages to Microsoft Azure Service Bus, with MySQL as database connected using pyodbc. The final script (not this one) is up and running on client's server. Uploaded the sample template here for reference purposes.

Problem Statement
======
Client wants to send data from their local MySQL database server to Azure Service Bus, this script gets the job done. Unfortunately, the client insists their server is "top secret" and not willing to allow us to access their server to deploy this, and instead they want their IT staffs who are inexperienced in any scripting languages to handle the deployments.

After struggling for weeks, finally found out that the hosting server is too old to install Docker engine, wrong configurations on their end resulting in the data not going to their Azure Service Bus endpoint, task scheduler not working as expected to run the script due to wrong configurations on their end as well, etc. (sigh)

But in the end managed to get it up and running, so all is well.

Requirements
======
Python 3.6 or later.

Notable Packages and Dependencies used
======
* pyodbc - To access ODBC databases.

* azure-servicebus - Azure Service Bus client library for Python.

* docker

How to Run
======
Install docker engine and just

### `docker run`

If without docker, install the necessary requirements using pip and run the main file.

### `python main.py`