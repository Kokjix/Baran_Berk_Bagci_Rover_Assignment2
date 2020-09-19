#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/position/drive', String, queue_size= 10) #drive publisherı
pub2 = rospy.Publisher('/position/robotic_arm', String, queue_size= 10) #robot kol publisherı

def split(word): #stringi karakterlere ayrıp listeye koyan fonksiyon
  return list(word)

def callbackDrive(data):
    DataList = split(data.data)
    #print(DataList)
    #stri = str(DataList[0]) + str(DataList[-1])
    #for i in range(0,4):
    position_drive = ''

    if DataList[0] == 'A' and DataList[-1] == 'B': #String verisinin ilk ve son karakterine bakıp sade A ve B olan stringi değerlendirmeye alıyor
      
      position_drive = decoderDrive(DataList)

      pub.publish(position_drive)

def callbackRobot(data):
  DataList = split(data.data)
  position_robot = ''  

  if DataList[0] == 'A' and DataList[-1] == 'B':
      
    position_robot = decoderRobot(DataList)

    pub2.publish(position_robot)



def decoderDrive(DataList):

  #first = list(str(DataList[1]) +  str(DataList[2]) +  str(DataList[3]) +  str(DataList[4])) 
  #second =  list(str(DataList[5]) + str(DataList[6]) + str(DataList[7]) + str(DataList[8])) 
  #third =  list(str(DataList[9]) + str(DataList[10]) + str(DataList[11]) + str(DataList[12])) 
  #forth = list(str(DataList[13]) + str(DataList[14]) + str(DataList[15]) + str(DataList[16]))

  if int(DataList[1]) == 1:
    first = '-' +  str(DataList[2]) +  str(DataList[3]) +  str(DataList[4])

  elif int(DataList[1]) == 0:
    first = str(DataList[2]) +  str(DataList[3]) +  str(DataList[4])

  if int(DataList[5]) == 1:
    second = '-' + str(DataList[6]) + str(DataList[7]) + str(DataList[8])

  elif int(DataList[5]) == 0:
    second = str(DataList[6]) + str(DataList[7]) + str(DataList[8])

  if int(DataList[9]) == 1:
    third = '-' + str(DataList[10]) + str(DataList[11]) + str(DataList[12])

  elif int(DataList[9]) == 0:
    third =  str(DataList[10]) + str(DataList[11]) + str(DataList[12])

  if int(DataList[13]) == 1:
    forth = '-' + str(DataList[14]) + str(DataList[15]) + str(DataList[16])

  elif int(DataList[13]) == 0:
    forth = str(DataList[14]) + str(DataList[15]) + str(DataList[16])

  if int(first) < -255:
    first = '-255'

  elif int(first) > 255:
    first = '255'

  if int(second) < -255:
    second = '-255'

  elif int(second) > 255:
    second = '255'
  
  if int(third) < -255:
    third = '-255'

  elif int(third) > 255:
    third = '255'

  if int(forth) < -255:
    forth = '-255'

  elif int(forth) > 255:
    forth = '255'


  final = first + ' ' + second + ' ' + third + ' ' + forth

  return final


def decoderRobot(DataList): #verileri dekode eden fonksiyon
    
  #first = list(str(DataList[1]) +  str(DataList[2]) +  str(DataList[3]) +  str(DataList[4])) 
  #second =  list(str(DataList[5]) + str(DataList[6]) + str(DataList[7]) + str(DataList[8])) 
  #third =  list(str(DataList[9]) + str(DataList[10]) + str(DataList[11]) + str(DataList[12])) 
  #forth = list(str(DataList[13]) + str(DataList[14]) + str(DataList[15]) + str(DataList[16]))

  if int(DataList[1]) == 1:
    first = '-' +  str(DataList[2]) +  str(DataList[3]) +  str(DataList[4])

  elif int(DataList[1]) == 0:
    first = str(DataList[2]) +  str(DataList[3]) +  str(DataList[4])

  if int(DataList[5]) == 1:
    second = '-' + str(DataList[6]) + str(DataList[7]) + str(DataList[8])

  elif int(DataList[5]) == 0:
    second = str(DataList[6]) + str(DataList[7]) + str(DataList[8])

  if int(DataList[9]) == 1:
    third = '-' + str(DataList[10]) + str(DataList[11]) + str(DataList[12])

  elif int(DataList[9]) == 0:
    third =  str(DataList[10]) + str(DataList[11]) + str(DataList[12])

  if int(DataList[13]) == 1:
    forth = '-' + str(DataList[14]) + str(DataList[15]) + str(DataList[16])

  elif int(DataList[13]) == 0:
    forth = str(DataList[14]) + str(DataList[15]) + str(DataList[16])

  if int(DataList[17]) == 1:
    fifth = '-' +  str(DataList[18]) +  str(DataList[19]) +  str(DataList[20])

  elif int(DataList[17]) == 0:
    fifth = str(DataList[18]) +  str(DataList[19]) +  str(DataList[20])

  if int(DataList[21]) == 1:
    sixth = '-' + str(DataList[22]) +  str(DataList[23]) +  str(DataList[24])
  
  elif int(DataList[21]) == 0:
    sixth = str(DataList[22]) +  str(DataList[23]) +  str(DataList[24])

  if int(first) < -255:
    first = '-255'

  elif int(first) > 255:
    first = '255'

  if int(second) < -255:
    second = '-255'

  elif int(second) > 255:
    second = '255'
  
  if int(third) < -255:
    third = '-255'

  elif int(third) > 255:
    third = '255'

  if int(forth) < -255:
    forth = '-255'

  elif int(forth) > 255:
    forth = '255'
  
  if int(fifth) < -255:
    fifth = '-255'

  elif int(fifth) > 255:
    fifth = '255'

  if int(sixth) < -255:
    sixth = '-255'

  elif int(sixth) > 255:
    sixth = '255'

  final = first + ' ' + second + ' ' + third + ' ' + forth + ' ' + fifth + ' ' + sixth

  return final












     
def listener():
 
       # In ROS, nodes are uniquely named. If two nodes with the same
       # name are launched, the previous one is kicked off. The
       # anonymous=True flag means that rospy will choose a unique
       # name for our 'listener' node so that multiple listeners can
       # run simultaneously.
    rospy.init_node('listener', anonymous=True)
   
    rospy.Subscriber("/serial/drive", String, callbackDrive)

    rospy.Subscriber("/serial/robotic_arm", String,callbackRobot)
   
      # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
   
if __name__ == '__main__':
    listener()