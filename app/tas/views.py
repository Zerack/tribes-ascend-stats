# Library Imports
from django.shortcuts import render

def index(request):        
    return render(request, 'index.html')

# Additional views to handle errors.
'''def error_400(request):
    td = {'header_text': 'Bad Request (400)',
          'body_text': 'The request could not be understood by the server.'}
    return render(request,'zoll_me/error.html', td, status=400)

def error_403(request):
    td = {'header_text': 'Forbidden (403)',
          'body_text': 'You do not have permission to access {0} on this server.'.format(request.path)}
    return render(request,'zoll_me/error.html', td, status=403)

def error_404(request):
    td = {'header_text': 'Page Not Found (404)',
          'body_text': 'The path {0} was not found on the server.'.format(request.path)}
    return render(request,'zoll_me/error.html', td, status=404)

def error_500(request):
    td = {'header_text': 'Internal Server Error (500)',
          'body_text': 'The server encountered an unexpected condition which prevented it from fulfilling your request.'}
    return render(request,'zoll_me/error.html', td, status=500)'''