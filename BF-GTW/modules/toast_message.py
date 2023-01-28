from flask import make_response, redirect

def send_toastMessage(message, link):
    response = make_response(redirect(link))
    response.set_cookie("toastMessage", message)
    return response