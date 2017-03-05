#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from pysimplesoap.client import SoapClient

GPIO.setmode(GPIO.BOARD)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

location = 'http://fritz.box:49000/igdupnp/control/WANCommonIFC1'
namespace = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1'
action = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#'

def getReceiverate():
	client = SoapClient(location, action, namespace, trace=False)
	response = client.GetCommonLinkProperties()
	response2 = client.GetAddonInfos()
	return int(response2.GetAddonInfosResponse.NewByteReceiveRate)

i=0
while i < 1000:
	time.sleep(1)
	receiveRate = getReceiverate()
	print (receiveRate)
	if receiveRate < 50000:
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(22, GPIO.LOW)
	elif receiveRate < 5000000:	
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(22, GPIO.LOW)
	else:	
		GPIO.output(26, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(22, GPIO.HIGH)
	i +=1
	
GPIO.cleanup()
