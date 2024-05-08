import logging
import azure.functions as func
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    email_subject = req_body.get('subject')
    email_message = req_body.get('message')

    if not email_subject or not email_message:
        return func.HttpResponse(
            "Please provide both 'subject' and 'message' in the request body.",
            status_code=400
        )

    try:
        send_email(email_subject, email_message)
        return func.HttpResponse("Email sent successfully.")
    except Exception as e:
        logging.error(f"Error sending email: {str(e)}")
        return func.HttpResponse("Failed to send email.", status_code=500)

def send_email(subject, message):
    sender_email = "<SENDER_EMAIL>"
    recipient_email = "<RECIPIENT_EMAIL>"
    api_key = "<SENDGRID_API_KEY>"

    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=message
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")
