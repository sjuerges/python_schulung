### Install Python 3.6.6 unter CentOS 7
### Parallel - Installation
### #############################################################
yum install gcc
yum install openssl-devel
yum install tk
yum install tk-devel
yum install tcl
cd /usr/src
wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz
tar -xvf Python-3.6.6.tar.xz
cd Python-3.6.6/
./configure --prefix=/opt/python3.6
make altinstall
ln -s /opt/python3.6/bin/python3.6 /usr/bin/python3.6
python3.6 --version
python --version
