### Install Python 3.7.0 unter CentOS 7
### Parallel - Installation
### #############################################################
yum install gcc
yum install openssl-devel
yum install libffi-devel
yum install tk
yum install tk-devel
yum install tcl
cd /usr/src
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar -xvf Python-3.7.0.tar.xz
cd Python-3.7.0/
./configure --prefix=/opt/python3.7 --enable-optimizations
make altinstall
ln -s /opt/python3.7/bin/python3.7 /usr/bin/python3.7
python3.7 --version
