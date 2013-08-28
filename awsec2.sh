#!/usr/bin/bash
# Install script for Dreamworld Tech exam Django/Python
# This script is to setup a working environment for the
# app on AWS EC2

ssh -i amazonaws.pem ubuntu@ec2-youraddress.compute-1.amazonaws.com

sudo apt-get update
sudo apt-get upgrade

# Essential Code Base
sudo apt-get install apache2 libapache2-mod-wsgi

sudo apt-get install python-pip

# Virtualenv setup and my favorite wrapper
# Because this is the only app I will have on aws, 
# I'm skipping virtualenv setup
#sudo pip install virtualenv virtualenvwrapper

# PostgreSQL
# I'm using dj_database_url to connect to a postgresql
# database remotely.  Very handy for swapping from
# dev to production databases with everything in the cloud
#sudo apt-get install postgresql python-psycopg2

# Clone the repo from my git
sudo apt-get install git
git clone git@github.com:iepathos/dreamworld.git

# Tell Apache where the WSGI is at
echo "WSGIScriptAlias / /home/ubuntu/dreamworld/dreamworld/wsgi.py" | sudo tee -a /etc/apache2/httpd.conf
echo "WSGIPythonPath /home/ubuntu/dreamworld/dreamworld" | sudo tee -a /etc/apache2/httpd.conf
echo "<Directory /home/ubuntu/dreamworld/dreamworld>" | sudo tee -a /etc/apache2/httpd.conf
echo "<Files wsgi.py>" | sudo tee -a /etc/apache2/httpd.conf
echo "Order deny,allow" | sudo tee -a /etc/apache2/httpd.conf
echo "Allow from all" | sudo tee -a /etc/apache2/httpd.conf
echo "</Files>" | sudo tee -a /etc/apache2/httpd.conf
echo "</Directory>" | sudo tee -a /etc/apache2/httpd.conf

echo "Include httpd.conf" | sudo tee -a /etc/apache2/apache2.conf

# Restart apache
sudo service apache2 restart

# Setup Apache to Serve Static Files
cd /var/www
sudo mkdir static
sudo mkdir media

sudo chown www-data static/
sudo chown www-data media/

# Install Django App requirements
cd /dreamworld
sudo pip install -r requirements.txt

# Usually not set as executable after git cloning I find
sudo chmod +x manage.py

# Sync up with the database 
python manage.py syncdb

# Move static files to /var/www/static for Apache to serve up
python manage.py collectstatic

# Test
python manage.py test


