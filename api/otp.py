from django.conf import settings
import  random

def otp_phone(request):
    if request.method == "POST":
        phone = request.POST['phone']
        print("///////////OTP//////////////")
        print(phone)
        token = request.POST['token']
        if re.findall(r"^\+(?:[0-9]●?){6,14}[0-9]$", phone):
            otp = random.randint(1000, 9999)
            url = 'http://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone}/{otp}'
            response = requests.request("GET", url)
            data = {}
            data['error'] = False
            data['success_msg'] = 'Message sent Successfully'
            return JsonResponse(data)
        else:
            data = {}
            data['error'] = True
            data['error_msg'] = 'Enter a valid phone number'
            return JsonResponse(data)
    else:
        data = {}
        data['error'] = True
        data['error_msg'] = 'Method not supported'
        return JsonResponse(data)