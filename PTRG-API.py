#AddDevice
def adddevice(devicename,deviceip,devicetempID,probeID):
# This fonction is inserting device or probe from template to PRTG and resume it to monitoring
    try:
        resp = requests.get("https://ServerIPorNAME/api/duplicateobject.htm?id="+str(devicetempID)+"&name="+str(devicename)+"&host="+str(deviceip)+"&targetid="+str(probeID)+"&username=prtgadmin&password=Password",verify=False)
        print resp

        for i in resp.history:
            id= i.url.partition("device.htm?id=")
            deviceid = id[2]
        respo = requests.get("https://ServerIPorNAME/api/pause.htm?id="+str(deviceid)+"&action=1&username=prtgadmin&password=Password", verify=False)
        print respo
    except:
        print ("Error.")
#adddevice(devicename,deviceip,devicetempID,probeID)

# Print all probes in PTRG
def getprobes():
    res = requests.get("https://ServerIPorNAME/api/table.xml?content=probes&output=json&columns=objid,name&filter_parentid=1&username=prtgadmin&password=Password")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
getprobes()

#print all devices in PRTG
def getdevices():
    res = requests.get("https://ServerIPorNAME/api/table.xml?content=devices&output=json&columns=objid,probe,group,device,host&username=prtgadmin&password=Password")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getdevices()

#Print all sensors by device ID
def getsensors(deviceID):
    res = requests.get("https://ServerIPorNAME/api/table.xml?content=sensors&output=json&columns=objid,device,sensor,status&id=8297&username=prtgadmin&password=Password")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getsensors(deviceID)

# get graphic by sensorID for last 2 hour
def getgraphic(sensorID):
    res = requests.get("https://ServerIPorNAME/api/chartlegend.json?graphid=2&id="+sensorID+"&username=prtgadmin&password=Password")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getgraphic(sensorID)
