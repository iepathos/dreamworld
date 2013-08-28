#!/usr/bin/bash
# Install script for Dreamworld Tech exam Django/Python
# This script is to setup a working environment for the
# app on AWS EC2

# These environment variables are used on my end with ec2-api-tools
export EC2_KEYPAIR=dreamworld
export EC2_URL=https://ec2.us-west-1.amazonaws.com
export EC2_PRIVATE_KEY=$HOME/jujubox/ec2/pk-N4N2HUPNB2OD7O6RSSYDEYTYLNBMPWWW.pem
export EC2_CERT=$HOME/jujubox/ec2/cert-N4N2HUPNB2OD7O6RSSYDEYTYLNBMPWWW.pem
export JAVA_HOME=/usr/lib/jvm/java-6-openjdk/

# SSH to server
#ssh -i dreamworld.pem ubuntu@54.215.190.18

# Bring OS up to speed
sudo apt-get update
sudo apt-get upgrade

# Essential Code Base
sudo apt-get install apache2 libapache2-mod-wsgi

sudo apt-get install python-pip python-setuptools

sudo apt-get install libpq-dev python-dev

# Virtualenv setup and my favorite wrapper
# Because this is the only app I will have on aws, 
# I'm skipping virtualenv setup
#sudo pip install virtualenv virtualenvwrapper

# PostgreSQL
# I'm using dj_database_url to connect to a postgresql
# database remotely.  Very handy for swapping from
# dev to production databases with everything in the cloud
#sudo apt-get install postgresql python-psycopg2
sudo apt-get install python-psycopg2

# Clone the repo from my git
sudo apt-get install git
git clone http://github.com/iepathos/dreamworld.git

# Install Django App requirements
cd /dreamworld
sudo pip install -r requirements.txt

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

# Sometimes this isn't set as executable after git cloning I find
# Ended up not being the case for me here.
#sudo chmod +x manage.py

# Sync up with the database 
python manage.py syncdb

# Move static files to /var/www/static for Apache to serve up
sudo python manage.py collectstatic

# Test
python manage.py test


