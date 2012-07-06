## Author: Hendy Chua
## Very basic version to install flask, mako and sqlalchemy
## Version 1
## Date: 05 July 2012

from fabric.api import local, lcd
from fabric.colors import blue, yellow

def setup():
    """
        Installs flask, mako and sqlalchemy using pip
    """
    
    ## installing flask
    print yellow("Installing latest Flask using pip... ")
    local("pip install flask")
    print blue("Finished installing flask")
    
    ## download Flask-Mako zip file from github first
    print yellow("Downloading Mako templates for Flask from github... ")
    local("git clone https://github.com/tzellman/flask-mako.git")
    print blue("Finished downloading Mako templates for Flask")
    
    ## installing Mako templates for flask
    print yellow("Installing Mako templates for Flask using tzellman's project on github... ")
    with lcd("flask-mako"):
        local("python setup.py install")
        
    print yellow("Clearing setup files for Mako-Flask... ")
    local("rm -rf flask-mako")
    print blue("Finished installing Mako templates for Flask")
    
    ##installing SQLAlchemy for Flask
    print yellow("Installing Flask-SQLAlchemy... ")
    local("pip install flask-sqlalchemy")
    print blue("Finished installing Flask-SQLAlchemy")
    
    print blue("Finished setup")
