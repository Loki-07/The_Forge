#!/bin/bash

echo " ===================================================================================================================================="                                                                                                                                    
echo "               __       _    _ _        _ 					"                                  
echo "              / /  ___ | | _(_| )__    /_\  _ __ _ __ ___   ___  _ __ _   _ 	"
echo "             / /  / _ \| |/ / |/ __|  //_\\| '__| '_   _ \ / _ \| '__| | | |	"
echo "            / /__| (_) |   <| |\__ \ /  _  \ |  | | | | | | (_) | |  | |_| |	"
echo "            \____/\___/|_|\_\_||___/ \_/ \_/_|  |_| |_| |_|\___/|_|   \__  |	"
echo "                                                                       |___/ 	"
echo " ===================================================================================================================================="                                                                                                                                    
echo ""
echo "                                       Created in Lokis Forge"
echo "                                        Lokis-notebook.org "
echo ""
echo "                                         Last Update 8/12/2020"
echo ""
echo ""
echo "Preparing your system for Weapons Package... Standby"
cd ~/Desktop
mkdir tools
cd tools
echo ""
echo "Your Tools will be installed on the Desktop in the tools Folder"
echo ""
echo "Updating your system and Distro now..."
echo ""
dpkg --add-architecture i386
apt-get update
echo ""
read -p " Update complete, press any key to continue"
apt-get upgrade 
echo ""
read -p "Upgrade complete, press any key to continue"
echo ""
echo ""
#==========================================================#
# All apt-get installs go here
#==========================================================#
echo "Installing Base Packages Now"
echo ""
echo ""
echo " Installing:"
echo " -- Terminator - alternative terminal tool"
echo " -- ftp service"
echo " -- Python pip, python3 pip"
echo " -- Dependancies for Git Hub based tools"
echo " -- Blood Hound - windows priv esc and unnumeration tool"
echo " -- AWS CLI and Boto3"
echo ""
echo ""
apt-get install wine32 -y
apt-get install mingw-w64 -y
apt-get install terminator -y 
apt-get install vsftpd -y  
apt-get install python3 -y 
apt-get install python-pip -y 
apt-get install python3-pip -y 
apt-get install libncurses5-dev -y 
apt-get install bloodhound -y
apt-get install gobuster -y
apt-get install awscl -y
apt-get install golang-go -y
#oneoff Domain finder
apt-get install urlcrazy -y
#Collection of lists for security testing
apt-get install seclists -y
apt-get install powershell -y
apt-get install veil -y
# Oracle Tools
apt-get install oscanner -y
apt-get install tnscmd10g -y
#
apt-get install smtp-user-enum -y
#VOIP Attack
apt-get install sipvicious -y
#large active directory recon
apt-get install crackmapexec -y
pip install boto3
echo ""
echo ""
echo "Initilizing the Metasploit Database"
systemctl start postgresql
msfdb init
echo ""
echo ""
echo " Installing Tor service and browser"
echo ""
echo " Creating a User - kali for use with Tor "
adduser --home-dir /home/kali kali
echo ""
echo ""
apt-get install tor 
apt install torbrowser-launcher
xhost si:localuser:kali
echo "to run tor browser in the future use -- sudo -u kali -H torbrowser-launcher -- "
echo "running tor as root will fail "
echo ""
echo ""
cd ~/Desktop/tools
#==========================================================#
echo ""
echo ""
#==========================================================#
# All Git Hub Installs go Below Here
#==========================================================#
echo "Installing weapons package into the tools Folder now..."
echo ""
echo ""
echo "Updating Search Sploit"
echo ""
searchsploit -u
read -p "Searchsploit update complete, press any key to continue"
echo ""
echo ""
echo "Installing What Breach "
git clone https://github.com/Ekultek/WhatBreach
cd WhatBreach
pip install -r requirements.txt
cd ~/Desktop/tools
echo ""
echo ""
echo "Installing WinboxExploit - Mikcortik"
git clone https://github.com/BigNerd95/WinboxExploit
echo ""
echo ""
echo "Installing pwnedOrNot"
git clone https://github.com/thewhiteh4t/pwnedOrNot
echo ""
echo ""
echo "Installing Sublist3r"
git clone https://github.com/aboul3la/Sublist3r.git
echo ""
echo ""
echo "Installing Routersploit"
git clone https://www.github.com/threat9/routersploit
cd routersploit
python3 -m pip install -r requirements.txt
echo ""
echo ""
cd /~Desktop/tools
echo ""
echo ""
#### Go Lang install replaced with apt-get install golang-go
#echo "Installing Go Language"
#mkdir golang
#cd golang
#wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz
#tar -xvf go1.12.7.linux-amd64.tar.gz
#export GOROOT=/root/Desktop/tools/golang/go
#export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

cd ~/Desktop/tools
echo ""
echo ""
echo "Installing Slurp S3 Recon tool"
git clone https://github.com/hehnope/slurp
cd slurp
go build
cd ~/Desktop/tools
echo ""
echo ""

echo "Installing One-Lin3r"
pip3 install one-lin3r
#git clone https://github.com/D4Vinci/One-Lin3r.git
#cd One-Lin3r
#pip install One-Lin3r
cd ~/Desktop/tools
echo ""
echo ""
echo "Installing Powershell Empire"
git clone https://github.com/EmpireProject/Empire.git
cd Empire
chmod +x setup/install.sh 
./setup/install.sh
cd ~/Desktop/tools
echo ""
echo ""
echo "Installing Legion (Formerlay Spart)"
#Install legion
git clone https://github.com/carlospolop/legion.git
cd legion/git
./install.sh
ln -sf /root/tools/legion/legion.py /usr/bin/legion
cd ~/Desktop/tools
echo ""
echo ""
echo "Installing Powersploit"
#Install Powersploit
git clone https://github.com/PowerShellMafia/PowerSploit
cd ~/Desktop/tools
#echo "Installing Powersploit"

echo "Installing LinEnum Script"
git clone https://github.com/rebootuser/LinEnum.git
cd ~/Desktop/tools

echo ""
echo ""
echo ""
echo ""
echo "================================================================================="
echo ""
echo " Your tools have been installs in ~/Desktop/tools"
echo ""
echo ""
echo "Your system is now configured... Good Hunting...."
echo ""
echo "================================================================================="
