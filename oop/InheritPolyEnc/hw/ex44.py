class Notification:
    def notify(self):
        raise NotImplementedError
    

class SMSNotification(Notification):
    def __init__(self, phone_number, code):
        self.phone_number = phone_number
        self.code = code
        super().__init__()
    
    def notify(self):
        print("Sending SMS notification...")


class EmailNotification(Notification):
    def __init__(self, email, code):
        self.email = email
        self.code = code
        super().__init__()
    
    def notify(self):
        print("Sending Email notification...")
        

class PushNotification(Notification):
    def __init__(self, device_id, code):
        self.device_id = device_id
        self.code = code
        super().__init__()
    
    def notify(self):
        print("Sending push notification...")
        
import random
import uuid

# User Udemydan kurs sotib oldi, endi quyidagi notificationlar borishi kerak
notifs = [
    SMSNotification(phone_number="+998901231122", code=random.randrange(1000,9999)),
    EmailNotification(email="eshmat@gmail.com", code=random.randrange(1000,9999)),
    PushNotification(device_id=uuid.uuid4(), code=random.randrange(1000,9999))
]

for notif in notifs:
    notif.notify()