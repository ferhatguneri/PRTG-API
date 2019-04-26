#Creted By Ferhat Guneri
#Mail: guneriferhat21@gmail.com
#Written Python 2.7

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
import time


#Get All Probes from PRTG
def getprobes():
    res = requests.get("https://prtg.server.com/api/table.xml?content=probes&output=json&columns=objid,name&filter_parentid=1&username=prtgadmin&password=*****")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getprobes()


# Get Graphic by Sensor ID
def getgraphic(sensorID):
    res = requests.get("https://prtg.server.com/api/chartlegend.json?graphid=2&id="+str(sensorID)+"&username=prtgadmin&password=*****")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getgraphic("1111")


#Get all devices from PRTG
def getdevices():
    res = requests.get("https://prtg.server.com/api/table.xml?content=devices&output=json&columns=objid,probe,group,device,host&username=prtgadmin&password=*****")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getdevices()


#Get all sensors of device
def getsensors(deviceID):
    res = requests.get("https://prtg.server.com/api/table.xml?content=sensors&output=json&columns=objid,device,sensor,status&id="+str(deviceID)+"&username=prtgadmin&password=*****")
    print res
    res = res.json()
    res = json.dumps(res)
    res = json.loads(res)
    print res
#getsensors("1111")


#Insert Device and Resume - Cloning from template device
def adddevice(TempDeviceID,DeviceName,DeviceIP,GroupID):
# Bu komut ile template devide den yeni device oluşturma işlemi yapılır.
    try:
        resp = requests.get("https://prtg.server.com/api/duplicateobject.htm?id="+str(TempDeviceID)+"&name="+str(DeviceName)+"&host="+str(DeviceIP)+"&targetid="+str(GroupID)+"&username=prtgadmin&password=*****",verify=False)
        print resp
#Bu komutlar ile yeni eklenen cihaz paused eklendiği için aşağıda yeni cihazın id si pars edilerek elde edilir ve cihaz status u resume yapılır.
        for i in resp.history:
            id= i.url.partition("device.htm?id=")
            deviceid = id[2]
        respo = requests.get("https://prtg.server.com/api/pause.htm?id="+str(deviceid)+"&action=1&username=prtgadmin&password=*****", verify=False)
        print respo
    except:
        print ("Cihaz Eklenirken bir hata oluştu.")
#adddevice("8480","Ferhat Guneri","1.2.3.4","2037")


#Remove Object (Device, Sensor, Probe).
def removeObject(objectID):
    res = requests.get("https://prtg.server.com/api/deleteobject.htm?id="+str(objectID)+"&approve=1&username=prtgadmin&password=*****")
    print res
#removeObject("8481")

#Pause Object (Device, Sensor, Probe)
def pauseObject(objectID):
    res = requests.get("https://prtg.server.com/api/pause.htm?id="+str(objectID)+"&action=0&username=prtgadmin&password=*****")
    print res
#pauseObject("8330")

#Resume Object (Device, Sensor, Probe)
def resumeObject(objectID):
    res = requests.get("https://prtg.server.com/api/pause.htm?id="+str(objectID)+"&action=1&username=prtgadmin&password=*****")
    print res
resumeObject("2052")


#Insert Group and Resume - Cloning from Template
def addGroup(TempGroupID,NewGroupName,DestinationGroupID):
    res = requests.get("https://prtg.server.com/api/duplicateobject.htm?id="+str(TempGroupID)+"&name="+str(NewGroupName)+"&targetid="+str(DestinationGroupID)+"&username=prtgadmin&password=*****")
    print res
    for i in res.history:
        id= i.url.partition("group.htm?id=")
        newGroupID = id[2]
    respo = requests.get("https://prtg.server.com/api/pause.htm?id="+str(newGroupID)+"&action=1&username=prtgadmin&password=*****")
    print respo
#addGroup("8508","Customer","1")
