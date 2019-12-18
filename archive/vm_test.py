from pyVim.connect import SmartConnect
import ssl
s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#s.verify_mode=ssl.CERT_NONE
si= SmartConnectNoSSL(host="192.168.1.202", user="hhakeem@hhden.lan", pwd="Tajw33d1!") #sslContext=s
aboutInfo=si.content.about
 
print ("Product Name:",aboutInfo.fullName)
print("Product Build:",aboutInfo.build)
print("Product Unique Id:",aboutInfo.instanceUuid)
print("Product Version:",aboutInfo.version)
print("Product Base OS:",aboutInfo.osType)
print("Product vendor:",aboutInfo.vendor)
