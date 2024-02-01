import uiautomator2 as ut
from time import sleep


device_serial_number="192.168.2.57:5555"

# creating an object for device
reciever_device=ut.connect(device_serial_number)

#opening gmail
#testcase GML_01 and GML_02
reciever_device.xpath("//*[@text='Gmail']").click()
print("gamil is opened and testcase GML_01 and GML_02")

#---------------------------------composing mail and attaching multiple files------------------------------------------------------------------------
#clicking on compose button
reciever_device(resourceId="com.google.android.gm:id/compose_button").click()
print("compose button is clickedad Gml_03")

#entring the senders emailId
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/peoplekit_autocomplete_chip_group']/android.widget.EditText[1]").set_text("Lavaup5g@gmail.com")
sleep(2)
#clicking on senders id
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/peoplekit_listview_flattened_row']/android.widget.RelativeLayout[2]").click()

# adding subject 
reciever_device(resourceId="com.google.android.gm:id/subject").set_text("checking the automation work")
sleep(1)
# writing email body
body=reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/wc_body_layout']/android.webkit.WebView[1]")
body.set_text("this is the body of mail that i want to send")

#clicking on attachment icon
reciever_device(resourceId='com.google.android.gm:id/add_attachment').click()

# clicking on attach file option
reciever_device.xpath("//android.widget.ListView/android.widget.LinearLayout[1]").click()
sleep(2)

#adding file in attachment
reciever_device.xpath("//*[@resource-id='com.google.android.documentsui:id/item_root']/android.widget.LinearLayout[1]").click()
print("single attachment is added")

#adding another attachment
reciever_device(resourceId='com.google.android.gm:id/add_attachment').click()
reciever_device.xpath("//android.widget.ListView/android.widget.LinearLayout[1]").click()
reciever_device.xpath("//*[@text='Images']").click()
sleep(2)
reciever_device.xpath("//*[@resource-id='com.google.android.documentsui:id/item_root']/android.widget.LinearLayout[1]").click()



#clicking on send button
reciever_device(resourceId="com.google.android.gm:id/send").click()
print("Email has been send")
print("Gml_04-Gml_06 and  passed ")


#-------------------------adding msg in draft and checking whether msg in draft or not-------------------------------------------------------
# codes for saving the msg in draft GML_07and GML_08
reciever_device(resourceId="com.google.android.gm:id/compose_button").click()
print("compose button is clicked")
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/peoplekit_autocomplete_chip_group']/android.widget.EditText[1]").set_text("Lavaup5g@gmail.com")
sleep(2)
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/peoplekit_listview_flattened_row']/android.widget.RelativeLayout[2]").click()
reciever_device(resourceId="com.google.android.gm:id/subject").set_text("checking the automation work")
sleep(1)
body=reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/wc_body_layout']/android.webkit.WebView[1]")
body.set_text("this is the body of mail that i want to send")
reciever_device(resourceId='com.google.android.gm:id/add_attachment').click()
reciever_device.xpath("//android.widget.ListView/android.widget.LinearLayout[1]").click()
sleep(2)


#adding file in attachment
reciever_device.xpath("//*[@resource-id='com.google.android.documentsui:id/item_root']/android.widget.LinearLayout[1]").click()
print("single attachment is added")
sleep(1)
# clicking on back button
reciever_device(resourceId="com.android.systemui:id/back").click()
sleep(2)

# clicking on three line icon for getting into menu
reciever_device.xpath("//*[@content-desc='Open navigation drawer']").click()
sleep(2)

# checking if msg is saved in draft
if reciever_device(resourceId="com.google.android.gm:id/count").exists():
    print("msg is saved into draft")
    print("testcase GML_07 and GML_08 passed")
else:
    print("msg is not saved in draft")


# clicking on back button
reciever_device(resourceId="com.android.systemui:id/back").click()
sleep(2)

# -----------------------------------------------------clicking on mail and clicking on reply--------------------------------------------
reciever_device(resourceId="com.google.android.gm:id/viewified_conversation_item_view").click()
sleep(2)
#clicking on reply button
reciever_device(resourceId="com.google.android.gm:id/reply").click()
sleep(1)
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/wc_body_layout']/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.EditText[1]").set_text("Hi sir how are you")
#clicking on send button
reciever_device(resourceId="com.google.android.gm:id/send").click()
print("testcase GML_09 is passed-->reply")
# clicking on back button
reciever_device(resourceId="com.android.systemui:id/back").click()


#-------------------------------------------------------------clicking on Replyall----------------------------------------------------
#opening mail
reciever_device(resourceId="com.google.android.gm:id/viewified_conversation_item_view").click()
#clicking on 3 dot and click on replyall
reciever_device(resourceId="com.google.android.gm:id/overflow").click()
sleep(2)
reciever_device.xpath("//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/wc_body_layout']/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.EditText[1]").set_text("Hi replying all")
#clicking on send button
reciever_device(resourceId="com.google.android.gm:id/send").click()
print("testcase GML_10 is passed-->replyall")
# clicking on back button
reciever_device(resourceId="com.android.systemui:id/back").click()

#------------------------------------ forwarding the mail------------------------------------------------------------------------
#opening mail
reciever_device(resourceId="com.google.android.gm:id/viewified_conversation_item_view").click()
#clicking on 3 dot and click on replyall
reciever_device(resourceId="com.google.android.gm:id/overflow").click()
reciever_device.xpath("//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
# adding mailid for forward
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/peoplekit_autocomplete_chip_group']/android.widget.EditText[1]").set_text("lava2022nhq@gmail.com")
sleep(1)
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/peoplekit_listview_flattened_row']/android.widget.RelativeLayout[2]").click()
sleep(2)
reciever_device.xpath("//*[@resource-id='com.google.android.gm:id/wc_body_layout']/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.EditText[1]").set_text("Hi forwarding all")
#clicking on send button
reciever_device(resourceId="com.google.android.gm:id/send").click()
print("testcase GML_11,12,13 is passed-->forwarding")
# clicking on back button
reciever_device(resourceId="com.android.systemui:id/back").click()

#---------------------------------------------------move to folder---------------------------------------------------------------
#selecting multiple email
reciever_device(resourceId="com.google.android.gm:id/contact_image").long_click()
#clicking on three dot on top
reciever_device.xpath("//*[@content-desc='More options']").click()
#clicking on move to option
reciever_device.xpath("//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
#clicking on promotion
reciever_device(resourceId="com.google.android.gm:id/folder_name").click()
print("mail is moved to other folder")
print('testcase 14 passed')

#----------------------------------------gml15..search---------------------------------------------------------------------
#clicking on search box

search=reciever_device(text="Search in emails")
search.click()
sleep(2)
search.set_text("google")
# clicking on back button
sleep(2)
reciever_device(resourceId="com.android.systemui:id/back").click()
reciever_device(resourceId="com.android.systemui:id/back").click()
print('gml15 is passed')

#--------------------------------------------GML_18-change notification tone-----------------------------------------------------------
# clicking on three line icon for getting into menu
reciever_device.xpath("//*[@content-desc='Open navigation drawer']").click()
reciever_device(text="Settings").click()
#clicking on mailid
reciever_device(text="testingwithlava@gmail.com").click()
#clicking on notificaton sound

reciever_device(text="Notification sounds").click()
sleep(1)
reciever_device.xpath("//*[@text='Notification sound']").click()
sleep(1)
#clicking on sound to change tone
reciever_device(text="Default notification sound").click()
sleep(2)

#select any tone and click on okk
reciever_device.xpath("//*[@resource-id='android:id/select_dialog_listview']/android.widget.RelativeLayout[4]").click()
sleep(2)
reciever_device(resourceId="android:id/button1").click()
sleep(1)
reciever_device(resourceId="com.android.settings:id/done").click()
for i in range(3):
    reciever_device(resourceId="com.android.systemui:id/back").click()
print("testcase Gml_18 passed")

#------------------------------------------adding signature-----------------------------------------------------
# clicking on three line icon for getting into menu
reciever_device.xpath("//*[@content-desc='Open navigation drawer']").click()
reciever_device(text="Settings").click()
#clicking on mailid
reciever_device(text="testingwithlava@gmail.com").click()
sleep(1)
# scrolling to mob_sing option and clicking on it
reciever_device.swipe(28,592,217,44)
reciever_device.xpath("//*[@text='Mobile signature']").click()
sleep(1)
# writing the signature adn clicking ok
sign=reciever_device.xpath("//*[@resource-id='android:id/edit']")
sign.click()
sign.set_text("Lava_international")
reciever_device.xpath("//*[@resource-id='android:id/button1']").click()
print("signature is added")
print("testcase GML_19 passed")

#------------------------------------------------Deleting mailId----------------------------------------------------
# clicking on three line icon for getting into menu
reciever_device(resourceId="com.google.android.gm:id/viewified_conversation_item_view").click()
sleep(2)
#clicking on delete Icon
reciever_device.xpath(resourecId="com.google.android.gm:id/delete").click()
print("testcase GML21 is passed")
print("email is deleted")









