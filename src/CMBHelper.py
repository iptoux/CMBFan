#!/bin/env python3.10
#
#   Raspberry Pi
#   Compute Module (CM) 4 I/O Board Fan control Program.
#   
#   With this program, you'r be able to full control your case fan in
#   addition with an CM I/O Board. Please see in Projects on github 
#   https://github.com/iptoux/CMBFan/projects?type=beta 
#
#   @class: CMBFan helper class -> CMBHelper()
#   @version: 0.1.0
#   @license: MIT   ->   https://github.com/iptoux/CMBFan/blob/main/LICENSE
#   @author: Maik Roland <iptoux> Damm  |   https://github.com/iptoux/CMBFan
#
#################################################################################

# Import needed modules for program 
import os, subprocess
from hashlib import new
from pickle import FALSE, TRUE
import logging

# Begining class
class CMBHelper():

    # Init Class/Obj
    def __init__(self):
        self.version = "0.1.0"
        return
    
    # Logging function, more explaination about this function you can find in the
    # main program or wiki (github online)
    def logging(self,loglvl,file = FALSE):
        self.logger = logging
        match loglvl:
            case 0:
                #print("INFO:root::INFO -> Logging deactiavted")
                self.level = 0
                self.logger.disable()
            case 1:
                self.level = logging.INFO
            case 2:
                self.level = logging.WARN
            case 3:
                self.level = logging.ERROR
            case 4:
                self.level = logging.DEBUG

        if(file != FALSE):
            LOGFILE=file
            self.logger.basicConfig(filename=LOGFILE,format='%(asctime)s %(message)s',level=self.level)
            self.logger.info(":LOG::    -> Start logging with level %s, into File: %s" % (self.logger.getLevelName(self.logger.root.level),LOGFILE))
            return(self.logger)
        else:
            LOGFILE=FALSE
            self.logger.basicConfig(level=self.level)
            self.logger.info(":LOG::    -> Start logging with level %s, Logfile disabled" % self.logger.getLevelName(self.logger.root.level))
            return(self.logger)

    # Check if user had given args
    def checkArgs(self,argslst):
        if(len(argslst[1:]) == 0):
            return(FALSE)
        else:
            self.args = argslst[1:]
            return(self.args)

    # Simple submod from checkPrivs, to check if user is root
    def checkRoot(self):
        if os.geteuid() != 0:
            return(FALSE)
        else:
            return(TRUE)

    # Submod to check if user is sudo, user will be asked if je wanna
    # start the sudo prompt
    def checkSudo(self):
        msg = "[sudo] password for %u:"
        if(subprocess.check_call("sudo -v -p '%s'" % msg, shell=True) != 0):
            return(FALSE)
        else:
            return(TRUE)

    # function to check if user is root or sudo. Because we had logging outputs here
    # no more documentation is needed at this part.
    def checkPrivs(self):
        # Check if User is root or can run sudo
        if(self.checkRoot() == TRUE):
            self.logger.info(":CMBFan:: -> User has root, contitune...")
            return(TRUE)
        else:
            self.logger.error(":CMBFan:: -> User has NO root, checking for sudo.")
            self.input = input("The program need root, do you want to run sudo? (y/n): ")
            if(self.input == "y"):
                if(self.checkSudo() == TRUE):
                    self.logger.info(":CMBFan:: -> User has sudo, contitune...")
                    return(TRUE)
                else:
                    self.logger.error(":CMBFan:: -> User had no root or sudo, exit program!")
                    return(FALSE)
            else:
                self.logger.error(":CMBFan:: -> User had no root or sudo, exit program!")
                return(FALSE)
