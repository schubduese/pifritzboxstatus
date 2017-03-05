#!/usr/bin/python3
from pysimplesoap.client import SoapClient

location = 'http://fritz.box:49000/igdupnp/control/WANCommonIFC1'
namespace = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1'
action = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1#'

debug = False  # display http/soap requests and responses

client = SoapClient(location, action, namespace, trace=debug)

response = client.GetCommonLinkProperties()
upspeed = int(response.GetCommonLinkPropertiesResponse.NewLayer1UpstreamMaxBitRate)
downspeed = int(response.GetCommonLinkPropertiesResponse.NewLayer1DownstreamMaxBitRate)

response2 = client.GetAddonInfos()
newbytesendrate = int(response2.GetAddonInfosResponse.NewByteSendRate)
newbytereceiverate = int(response2.GetAddonInfosResponse.NewByteReceiveRate)

print(upspeed, downspeed, newbytesendrate, newbytereceiverate)
