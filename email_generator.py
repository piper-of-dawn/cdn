import os
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def generate_outlook_eml(path, recipients):
    # Create a multipart message container
    msg = MIMEMultipart()
    msg['Subject'] = 'Your Subject Here'
    msg['From'] = 'sender@example.com'
    msg['To'] = ', '.join(recipients)

    # Add body text
    body = "This is the body of your email. You can add any standard text here."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the document
    filename = os.path.basename(path)
    attachment = open(path, 'rb')
    mime_type, _ = mimetypes.guess_type(path)
    if mime_type is None:
        mime_type = 'application/octet-stream'
    part = MIMEBase(*mime_type.split('/'))
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
    msg.attach(part)

    # Save the message to an .eml file
    eml_filename = 'email_with_attachment.eml'
    with open(eml_filename, 'w') as eml_file:
        eml_file.write(msg.as_string())

    print(f"EML file '{eml_filename}' has been generated with attachment '{filename}'.")

# Example usage:
generate_outlook_eml('visualisation.py', ['recipient1@example.com', 'recipient2@example.com'])
