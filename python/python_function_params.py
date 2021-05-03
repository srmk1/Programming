import os

#Sending dictionary as function params
def send_dictionary_as_param(personal_details):
    print("Name :%s"%personal_details['Name'])
    print("DOB :%s"%personal_details['DOB'])
    print("Gender :%s"%personal_details['Gender'])
    print("Subjects :%s,%s,%s"%(personal_details['Subject_list'][0],personal_details['Subject_list'][1],personal_details['Subject_list'][2]))
    print("Is employed:%d"%personal_details['Is_employed'])
#usage
send_dictionary_as_param({'Name':"Srikanth",
                          'DOB':"20-04-1918",
                          'Gender':'Male',
                          'Subject_list': ['Science','Maths','Astronomy'],
                          'Is_employed': True
                          })

#Sending list as function params
def send_list_as_param(fruits):
    for fruit in fruits:
        print("%s "%fruit)
#usage
send_list_as_param(['apple', 'orange', 'mango'])

