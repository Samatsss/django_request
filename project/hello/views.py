from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    user_ip = request.META["REMOTE_ADDR"]
    path = request.path

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
        <p>user_ip: {user_ip}</p>
    """)

def error(request):
    return HttpResponse('К сожалению произошла ошибка', status=400, reason="Incorrect data")

def user(request, name):
    return HttpResponse(f"<h2>Имя: {name}</h2>")