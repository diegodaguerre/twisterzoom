Twister Zoom
============

How to Develop in Linux
=======================

* Install required system packages::

    apt-get install python-dev python-virtualenv

    or

    yum install python-devel python-virtualenv

* Create and activate development virtual environment::

    mkdir ~/envs
    virtualenv ~/envs/twisterzoom
    source ~/envs/twisterzoom/bin/activate
    
* Install required python packages inside virtual environment::

    pip install -r requirements.txt

* Run test suite::

    nosetests
