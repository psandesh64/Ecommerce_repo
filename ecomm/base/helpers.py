from io import BytesIO
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import uuid
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string

def save_pdf(params: dict,user):
    template = get_template("pdf/invoice.html")
    html = template.render(params)
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), response)
    file_name = uuid.uuid4() 

    try:
        with open(str(settings.BASE_DIR)+f"/public/static/{file_name}.pdf", 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), output)
        pdf_file_path = str(settings.BASE_DIR) + f"/public/static/{file_name}.pdf"
        send_purchase_mail(user.email, pdf_file_path)
        
    except Exception as e:
        print(e)

    if pdf.err:
        return '', False
    return file_name, True

def send_purchase_mail(email, pdf_file_path):
    subject = 'Item Purchased'
    message = f'YOu have purchased item from our ecommerce site'
    email_from = settings.EMAIL_HOST_USER
    
    # Create an EmailMessage object
    email = EmailMessage(subject, message, email_from, [email])

    with open(pdf_file_path, 'rb') as pdf_file:
        email.attach(f"{pdf_file_path}.pdf", pdf_file.read(), 'application/pdf')
    
    # Send the email
    email.send()