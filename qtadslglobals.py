# -*- coding: utf-8 -*-
# QtAdsl easy adsl tool for GNU/Linux
 # Copyright (C) 2008, Oğuzhan Eroğlu <rohanrhu2@gmail.com>
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.

 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 
version = "0.1"
 
chap = '''# Secrets for authentication using CHAP
# client	server	secret			IP addresses
"***user***"	*	"***passwd***"'''

conf = '''#***********************************************************************
#
# pppoe.conf
#
# Configuration file for rp-pppoe.  Edit as appropriate and install in
# /etc/ppp/pppoe.conf
#
# NOTE: This file is used by the pppoe-start, pppoe-stop, pppoe-connect and
#       pppoe-status shell scripts.  It is *not* used in any way by the
#       "pppoe" executable.
#
# Copyright (C) 2000 Roaring Penguin Software Inc.
#
# This file may be distributed under the terms of the GNU General
# Public License.
#
# LIC: GPL
# $Id: pppoe.conf,v 1.11 2005/08/09 02:49:12 dfs Exp $
#***********************************************************************

# When you configure a variable, DO NOT leave spaces around the "=" sign.

# Ethernet card connected to DSL modem
ETH='nas0'

# PPPoE user name.  You may have to supply "@provider.com"  Sympatico
# users in Canada do need to include "@sympatico.ca"
# Sympatico uses PAP authentication.  Make sure /etc/ppp/pap-secrets
# contains the right username/password combination.
# For Magma, use xxyyzz@magma.ca
USER='***user***'

# Bring link up on demand?  Default is to leave link up all the time.
# If you want the link to come up on demand, set DEMAND to a number indicating
# the idle time after which the link is brought down.
DEMAND=no
#DEMAND=300

# DNS type: SERVER=obtain from server; SPECIFY=use DNS1 and DNS2;
# NOCHANGE=do not adjust.
DNSTYPE=NOCHANGE

# Obtain DNS server addresses from the peer (recent versions of pppd only)
# In old config files, this used to be called USEPEERDNS.  Changed to
# PEERDNS for better Red Hat compatibility
PEERDNS=no

DNS1=
DNS2=

# Make the PPPoE connection your default route.  Set to
# DEFAULTROUTE=no if you don't want this.
DEFAULTROUTE=yes

### ONLY TOUCH THE FOLLOWING SETTINGS IF YOU'RE AN EXPERT

# How long pppoe-start waits for a new PPP interface to appear before
# concluding something went wrong.  If you use 0, then pppoe-start
# exits immediately with a successful status and does not wait for the
# link to come up.  Time is in seconds.
#
# WARNING WARNING WARNING:
#
# If you are using rp-pppoe on a physically-inaccessible host, set
# CONNECT_TIMEOUT to 0.  This makes SURE that the machine keeps trying
# to connect forever after pppoe-start is called.  Otherwise, it will
# give out after CONNECT_TIMEOUT seconds and will not attempt to
# connect again, making it impossible to reach.
CONNECT_TIMEOUT=30

# How often in seconds pppoe-start polls to check if link is up
CONNECT_POLL=2

# Specific desired AC Name
ACNAME=

# Specific desired service name
SERVICENAME=

# Character to echo at each poll.  Use PING="" if you don't want
# anything echoed
PING="."

# File where the pppoe-connect script writes its process-ID.
# Three files are actually used:
#   $PIDFILE       contains PID of pppoe-connect script
#   $PIDFILE.pppoe contains PID of pppoe process
#   $PIDFILE.pppd  contains PID of pppd process
CF_BASE=`basename $CONFIG`
PIDFILE="/var/run/$CF_BASE-pppoe.pid"

# Do you want to use synchronous PPP?  "yes" or "no".  "yes" is much
# easier on CPU usage, but may not work for you.  It is safer to use
# "no", but you may want to experiment with "yes".  "yes" is generally
# safe on Linux machines with the n_hdlc line discipline; unsafe on others.
SYNCHRONOUS=no

# Do you want to clamp the MSS?  Here's how to decide:
# - If you have only a SINGLE computer connected to the DSL modem, choose
#   "no".
# - If you have a computer acting as a gateway for a LAN, choose "1412".
#   The setting of 1412 is safe for either setup, but uses slightly more
#   CPU power.
CLAMPMSS=1412
#CLAMPMSS=no

# LCP echo interval and failure count.
LCP_INTERVAL=20
LCP_FAILURE=3

# PPPOE_TIMEOUT should be about 4*LCP_INTERVAL
PPPOE_TIMEOUT=80

# Firewalling: One of NONE, STANDALONE or MASQUERADE
FIREWALL=STANDALONE

# Linux kernel-mode plugin for pppd.  If you want to try the kernel-mode
# plugin, use LINUX_PLUGIN=rp-pppoe.so
LINUX_PLUGIN=

# Any extra arguments to pass to pppoe.  Normally, use a blank string
# like this:
PPPOE_EXTRA=""

# Rumour has it that "Citizen's Communications" with a 3Com
# HomeConnect DSL Modem DualLink requires these extra options:
# PPPOE_EXTRA="-f 3c12:3c13 -S ISP"

# Any extra arguments to pass to pppd.  Normally, use a blank string
# like this:
PPPD_EXTRA=""


########## DON'T CHANGE BELOW UNLESS YOU KNOW WHAT YOU ARE DOING
# If you wish to COMPLETELY overrride the pppd invocation:
# Example:
# OVERRIDE_PPPD_COMMAND="pppd call dsl"

# If you want pppoe-connect to exit when connection drops:
# RETRY_ON_FAILURE=no'''

def setUser(user, passwd):
    userFile = open("/etc/ppp/pppoe.conf", "w")
    userFile.write(conf.replace("***user***", str(user)))
    userFile.close()

    passwdFile = open("/etc/ppp/chap-secrets", "w")
    passwdFile.write(chap.replace("***passwd***", str(passwd)).replace("***user***", str(user)))
    passwdFile.close()

def setAutomatic(isSet):
    automaticScript = "/usr/sbin/br2684ctl -c 0 -b -a 8.35\n/usr/sbin/adsl-start"

    if isSet:
	fileRead = open("/etc/conf.d/local.start", "r").read().lower()
	startFile = open("/etc/conf.d/local.start", "w")

	if "/usr/sbin/adsl-start" not in fileRead:
	    toWrite = "%(fileRead)s\n%(automaticScript)s" % vars()
	    startFile.write(toWrite)
	else:
	    toWrite = str("%(fileRead)s\n%(automaticScript)s" % vars()).replace("\n/usr/sbin/br2684ctl -c 0 -b -a 8.35", "").replace("\n/usr/sbin/adsl-start", "").replace("/usr/sbin/br2684ctl -c 0 -b -a 8.35", "").replace("/usr/sbin/adsl-start", "")
	    startFile.write(toWrite)

	startFile.close()