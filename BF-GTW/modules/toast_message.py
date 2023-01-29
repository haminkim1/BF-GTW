from flask import make_response, redirect, render_template

def send_toastMessage(message, link):
    response = make_response(redirect(link))
    response.set_cookie("toastMessage", message)
    return response
