#!/bin/env python3.10
#
#   Raspberry Pi
#   Compute Module (CM) 4 I/O Board Fan control Program.
#   
#   With this program, you'r be able to full control your case fan in
#   addition with an CM I/O Board. Please see in Projects on github 
#   https://github.com/iptoux/CMBFan/projects
#
#   @version: 0.1-a
#   @license: MIT   ->  https://github.com/iptoux/CMBFan/blob/main/LICENSE
#   @author: Maik Roland <iptoux> Damm  |   https://github.com/iptoux/CMBFan
#   @help: https://github.com/iptoux/CMBFan/discussions
#
#################################################################################

from pickle import FALSE, TRUE
import sys

# Build my own class, to put things together and hold program clean.
from CMBHelper import CMBHelper

# Main function, here will the program be initiated
def main():
    CMB = CMBHelper()
    
    # Enable/Disable logging. You can also log to File (If log to File, now output to console)
    # 0 = Off // 1 = Info // 2 = Warning // 3 = Error // 4 = Critical
    # Second arg = "mylogfile.log". If none given, logging to file disable
    CMB.logging(0)

    # Checking privileges of current user. Actually root/sudo is needed. If not available
    # Program will exit with Msg.
    if(CMB.checkPrivs() == FALSE):
        sys.exit("Error: None root privileges. You need at least sudo to run this program. Please see log/logfile.")

    ## Next step is to check if args are given, if not exit else, parse args and run subfunction

    if(CMB.checkArgs(sys.argv) == FALSE):
        CMB.logger.error(":ARGS::  -> No arguments given.")
        CMB.logger.info(":ARGS::   -> \"CMBFan -h\" for help")
        sys.exit("You have to give at least one argument.\n\"CMBFan -h\" for help")
    
    print("Until now running fine...\nArguments: %s" % sys.argv[1:] + "\nTODO: All other next steps.")    


# initiate Program / load main function.
if __name__ == "__main__":
    main()
