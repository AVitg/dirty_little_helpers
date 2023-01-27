#!/usr/bin/python
import requests
import json
import logging
import csv

'''
provided as is - might harm your Smartconnectors - don't blame me. Think before you act.

connector_scanner is used to scan for default username/password usage on ArcSight Smart Connector's remote management port
The script takes "config.csv" as a an input list for hosts to scan

Provide username and password, you knwe where to find it... i wont tell you.
change port_start and port_end, if you use different ports.

https_timeout parameterizes the connection timeout for the request, if you have a big list, this might influence the runtime of the script, however
  don't put it too low, as your network might not react fast enough, and you would miss the host/port
  
'''


requests.packages.urllib3.disable_warnings()

port_start=9000
port_end=9008
https_timeout=3

### init logger 
logger = logging.getLogger('connector_scanner')  # Create a logger for this class
logger.setLevel(logging.INFO)  # Set the logging level

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

# Read the config file
with open("config.csv") as config_file:
    config = csv.reader(config_file)
    next(config) # skipping the headers    
    for server in config:        
        try: 
            host = server[0]        
            outx='-'*60
            logger.debug(outx) 
            out="{} - Scanning host.".format(host)
            logger.debug(out)
            logger.debug(outx)            
            for port in range (port_start,port_end+1):
                # Set the URL of the ArcSight Smart Connector's remote management API
                url = "https://{}:{}/cwsapi/services/v1?wsdl".format(host, port)

                # Set the default username and password
                username = ""
                password = ""

                # Create the SOAP body
                body = """
                <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://v1.soap.loadable.arcsight.com">
                    <soapenv:Header/>
                    <soapenv:Body>
                        <v1:login soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
                            <in0 xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">{}</in0>
                            <in1 xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">{}</in1>
                        </v1:login>
                    </soapenv:Body>
                </soapenv:Envelope>
                """.format(username, password)

                # Set the headers for the request
                headers = {'content-type': 'text/xml' , 'SOAPAction':''}

                try:
                    # Send a request to the API using the default username and password
                    response = requests.post(url, data=body, headers=headers,  verify=False, timeout=https_timeout)

                    # Check if the response contains the 'success' element
                    if "true" in response.text:
                        out="{}:{} - The default password is being used.".format(host,port)
                        logger.info(out) 
                        
                    elif 'false' in response.text:
                        out="{}:{} - The default password is not being used.".format(host,port)
                        logger.debug(out)
                        
                    else:
                        out="{}:{} - Unknown State".format(host,port)
                        logger.info(out)                        
  
                except requests.exceptions.RequestException as e:                    
                    out="{}:{} - Unable to connect to Server or port".format(host,port)
                    logger.debug(out)            
        except:
            out="Unable to read line from csv '{}', skipping".format(server)
            logger.debug(outx)
            logger.error(out)
