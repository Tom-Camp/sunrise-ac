#!/usr/bin/python

#
#
#

from ledStrip import ledstrip
import time
import argparse
import datetime
from datetime import date 
import logging
import ConfigParser

def main():


    while True:
        day = time.strftime('%A')
        start_time = Config.get('StartTimes', day)
        
        if (start_time == 'None'):
            continue
        else:
            start_day = time.strftime('%Y-%m-%d')
            start = ' ' . join([start_day, start_time])
            now = time.time()
            start_now = time.mktime(datetime.datetime.strptime(start, '%Y-%m-%d %H:%M').timetuple())

            if now > start_now and now < start_now + 10:
                #start_alarm()
                print 'starting'


def set_configuration():
    # Open the config file
    Config = ConfigParser.RawConfigParser()
    Config.readfp(open('config.ini'))

    # Define app description and optional parameters
    parser = argparse.ArgumentParser(description = 'Example sketch that controls an LED strip via Spacesb. It uses the 	LED Strip Python library for Adafruit\'s LPD8806 LED strips.')
    # Define the led strip length optional parameter
    parser.add_argument('-l', '--leds', '--pixels', 
            nargs = 1, type = int, default = 32,
            help = 'Length of led strip leds or pixels')
    # Read all command line parameters
    args = parser.parse_args()    

    # Set up logging
    logging.basicConfig(filename='alarm.log', level=logging.INFO, format='%(asctime)s %(message)s')
    

if __name__ == "__main__":
    set_configuration()
    main()
