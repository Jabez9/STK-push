from django.shortcuts import render,redirect
import requests
from .credentials import MpesaAccessToken, MpesaPassword

# Create your views here.


def home(request):
    return render(request,'index.html')


#have to go through to get the meaning of this

def stk_push(request):
    if request.method == "POST":
        phone = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        access_token = MpesaAccessToken.validated_token

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        headers = {"Authorization": "Bearer %s" % access_token}

        payload = {   
                    "BusinessShortCode": MpesaPassword.shortcode,    
                    "Password": MpesaPassword.decoded_password,    
                    "Timestamp":MpesaPassword.timestamp,    
                    "TransactionType": "CustomerPayBillOnline",    
                    "Amount": amount,    
                    "PartyA":phone,    
                    "PartyB":MpesaPassword.shortcode,    
                    "PhoneNumber":phone,    
                    "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",   
                    "AccountReference":"ApartMateMe", 
                    "TransactionDesc":"ApartmateMe Payment"
                }
        # response = requests.post(api_url,json=payload,headers=headers)
        try:
            response = requests.post(api_url, json=payload, headers=headers)
            if response.status_code == 200:
                print("STK Push initiated successfully:", response.json())
                return redirect("thanks")
            else:
                print("Failed to initiate STK Push:", response.status_code, response.text)
                return redirect("error")
        except Exception as e:
            print("An error occurred:", str(e))
            return redirect("error")

    return redirect("thanks")
   #here i should have a fxn that after payment, redirect etc

def thank_you(request):
    return render(request, 'thanks.html')

def stk_error(request):
    return render(request, 'stkerror.html' )

