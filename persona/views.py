from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa

from django.shortcuts import render

def home(request):
    return render(request,'persona/index.html')

def generate_pdf(request):
    personas = [
        {"id": 1, "nombre": "Juan Pérez", "edad": 30},
        {"id": 2, "nombre": "María López", "edad": 25},
        {"id": 3, "nombre": "Carlos Ruiz", "edad": 35},
    ]
    
    context = {'personas': personas}
    html = render_to_string('persona/template.html', context)
    
    buffer = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=buffer)
    buffer.seek(0)
    
    # Aquí usamos el 'inline' para que se abra en una ventana/pestaña nueva
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="output.pdf"'
    
    return response
