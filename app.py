from flask import Flask, request
import azure.functions as func

app = Flask(__name__)

@app.route('/home')
def home():
    return "Hello, ritesh123"

# Azure Functions Entry Point
def main(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Function entry point"""
    return func.WsgiMiddleware(app.wsgi_app).handle(req)
