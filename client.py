from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor
import base64
from suds.plugin import MessagePlugin
from datetime import date

class NovaPhoshtaWayBill():

    

    def WayBill(self, id, total, receiver_name, receiver_city_id, receiver_address, receiver_phone, weight, product_description, comment, order_id, is_express):
        imp1 = Import('http://v8.1c.ru/8.1/data/core')
        doctor = ImportDoctor(imp1)


        client = Client('http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws?WSDL',
                        location='http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws',
                        username='testuser', password='123456789', doctor=doctor, timeout=5)

        sender_id = '' #GUID for sender 
        sender_address = 'თბილისი'
        sender_city_id = '5f955257-132f-11e5-80d3-00155d3cd455'
        sender_address_id = 'c2fafd7d-b853-11e9-80cf-00155d5fea08'
        sender_contact_name = 'ონლაინ მაღაზია'
        sender_phone = "599123123"

        WayBill = client.factory.create('ns1:WayBillRef')

        WayBill.GUID = id
        WayBill.Barcode = ''
        WayBill.Date = '2019-06-16T14:59:33'
        WayBill.Total = 0

        Receiver = client.factory.create('ns1:Reference')
        Receiver.GUID = '00000000-0000-0000-0000-000000000000'
        Receiver.Name = receiver_name
        WayBill.Receiver = Receiver


        SenderCity = client.factory.create('ns1:Reference')
        SenderCity.GUID = sender_city_id
        WayBill.SenderCity = SenderCity


        ReceiverCity = client.factory.create('ns1:Reference')
        ReceiverCity.GUID = receiver_city_id
        
        WayBill.ReceiverCity = ReceiverCity


        WayBill.SenderPhone = sender_phone
        WayBill.ReceiverPhone = receiver_phone

        #ReferenceList = client.factory.create('tns:Reference')
        Sender = client.factory.create('ns1:Reference')
        Sender.GUID = sender_id
        #Sender.Name = 'სს თიბისი ბანკი'
        WayBill.Sender = Sender


        #KindOfPayer = self.client.factory.create('tns:KindOfPayer')
        KindOfPayer = 1 # fixed
        WayBill.KindOfPayer = KindOfPayer

        WayBill.Weight = weight

        #KindOfCargo = self.client.factory.create('tns:KindOfPayer')
        KindOfCargo = 7 # fixed
        WayBill.KindOfCargo = KindOfCargo



        SenderAddress = client.factory.create('ns1:Reference')
        SenderAddress.GUID = sender_address_id
        #SenderAddress.Name = sender_address

        WayBill.SenderAddress = SenderAddress

        ReceiverAddress = client.factory.create('ns1:Reference')
        ReceiverAddress.GUID = '00000000-0000-0000-0000-000000000000'
        ReceiverAddress.Name = receiver_address
        WayBill.ReceiverAddress = ReceiverAddress

        WayBill.Places = 1
        WayBill.Comment = comment
        WayBill.CargoCost = total


        #KindOfService = self.client.factory.create('tns:KindOfService')
        KindOfService = 0 # door to door
        WayBill.KindOfService = KindOfService

        WayBill.CargoDescription = product_description

        #PayForm = self.client.factory.create('tns:KindOfPay')
        PayForm = 0 # fixed
        WayBill.PayForm = PayForm

        WayBill.SenderContact = sender_contact_name
        WayBill.ReceiverContact = receiver_name


        WayBill.KindOfRedelivery = -1
        WayBill.KindOfCargoOfRedelivery = -1
        WayBill.RedeliveryDescription = ''
        WayBill.Volume = 0
        print(order_id)
        WayBill.OrderNumber = order_id
        WayBill.DayToDay = False
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        WayBill.PickUpDate = d1
        WayBill.Postpayment = 0.0
        WayBill.CGD = ""
        print(WayBill)
        SaveWayBill = client.service.SaveWayBill(WayBill=WayBill,Post=True)
        
        return SaveWayBill


    def PrintWayBillByBarcode(self, barcode):
        imp1 = Import('http://v8.1c.ru/8.1/data/core')
        doctor = ImportDoctor(imp1)


        client = Client('http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws?WSDL',
                        location='http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws',
                        username='testuser', password='123456789', doctor=doctor, timeout=5)
        PrintWayBillByBarcode = client.service.PrintWayBillByBarcode(Barcode=barcode,Format='PDF')
        return PrintWayBillByBarcode

    def PrintWayBillByID(self, WayBillID):
        imp1 = Import('http://v8.1c.ru/8.1/data/core')
        doctor = ImportDoctor(imp1)


        client = Client('http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws?WSDL',
                        location='http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws',
                        username='testuser', password='123456789', doctor=doctor, timeout=5)
        PrintWayBill = client.service.PrintWayBill(ID=WayBillID,Format='PDF')
        return PrintWayBill

    def NewWayBill(self):
        imp1 = Import('http://v8.1c.ru/8.1/data/core')
        doctor = ImportDoctor(imp1)


        client = Client('http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws?WSDL',
                        location='http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws',
                        username='testuser', password='123456789', doctor=doctor, timeout=5)
        NewWayBill = client.service.NewWayBill()
        return NewWayBill
    
    def WayBillInfo(self,WayBillID):
        imp1 = Import('http://v8.1c.ru/8.1/data/core')
        doctor = ImportDoctor(imp1)


        client = Client('http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws?WSDL',
                        location='http://188.93.95.234:8081/CabinetAPI/ws/cabinetAPI1_1.1cws',
                        username='testuser', password='123456789', doctor=doctor, timeout=5)
        WayBill = client.service.WayBill(ID=WayBillID)
        return WayBill
