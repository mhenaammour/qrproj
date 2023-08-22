from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import qrcode
from .models import QRCode

def generate_qr(request):
    if request.method == 'POST':
        data = request.POST['data']
        
        # Create a QRCode instance and save it to the database
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img_path = 'qrcode_app/static/qrcode.png'
        qr_img.save(qr_img_path)
        
        # Save the QRCode object in the database
        qrcode_obj = QRCode.objects.create(data=data)
        
        return render(request, 'generate_qr.html', {'data': data, 'qrcode_obj': qrcode_obj})
    
    return render(request, 'generate_qr.html')


def scan_qr(request):
    return render(request, 'scan_qr.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
