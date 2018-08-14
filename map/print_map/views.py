from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse,QueryDict
from django.template import loader
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from .models import User,Trip

from pyecharts import GeoLines,Style,Geo
from pyecharts.datasets.coordinates import get_coordinate
from time import strftime,gmtime
import json

# Create your views here.
def inde(request):
    return render(request, 'map.html')

@csrf_exempt
def get_map(request):
    REMOTE_HOST = "https://pyecharts.github.io/assets/js"
    # template = loader.get_template('myvis/show_map.html')
    
    if request.method == 'GET':
        map = print_map()
        
        if 'id' in request.session.keys():
            username = User.objects.get(id = request.session['id']).username
        else:
            username = ""
            
        context = dict(
            host = REMOTE_HOST,
            myecharts = map.render_embed(),
            script_list = map.get_js_dependencies(),
            username = username
        )
        
        return JsonResponse(context)
    elif request.method == 'POST':
        if 'id' in request.session.keys():
            username = User.objects.get(id = request.session['id']).username
        else:
            username = ""
            
        city = QueryDict(request.body)['city']
        city = city.split("+")
        print(city)
        print(type(city))
        map = print_map(trip=city)
        
        context = dict(
            host = REMOTE_HOST,
            myecharts = map.render_embed(),
            script_list = map.get_js_dependencies(),
            username = username
        )
        
        return JsonResponse(context)
        
    else:
        return HttpResponse("Your method must post or get")

# this functions is about app
def print_map(trip = []):
    '''
    this function to get Geolines
    :param trip: [list]list the site of this trip after
    :return: <pyecharts.GeoLines object> the trip have
    '''
    style = Style(
        title_color="#fff",
        title_pos="center",
        title_text_size=24,
        title_top=10,
        width=1600,
        height=800,
        background_color="#404a59"
    )
    
    date = strftime("%a, %d %b %Y",gmtime())
    
    if trip != [] :
        geolines = GeoLines(title="My trip",subtitle=date,**style.init_style)
        
        trip = handle_citys(trip)
        geolines.add(
            "one trip",
            data=trip,
            is_legend_show=False,
            is_geo_effect_show=False,
            symbol_size=0.1
        )
    else:
        geolines = Geo(title = "My trip", subtitle = date,**style.init_style)
        geolines.add("",[],[],maptype='china')
    
    return geolines

def handle_citys(citys):
    '''
    this function to handle city list to get a route from the city list
    :param city: [str]list city's liat
    :return:
    '''
    del_list = []
    for city in citys:
        if get_coordinate(city) == None:
            del_list.append(city)
    
    for city in del_list:
        citys.remove(city)
    
    res = [[citys[i],citys[i+1]] for i in range(len(citys)-1)]
    return res

# this functions is for login or register
@csrf_exempt
def login(request):
    '''
    this function for login
    :param request: HttpRequest for login
    :return: {response_data}dict message and code for login status
    '''
    response_data = {}
    if request.method == "POST":
        if 'id' in request.session.keys():
            response_data['status'] = 'error'
            response_data['message'] = 'you have log in'
            return JsonResponse(response_data)
        else:
            login_data = QueryDict(request.body)
            if 'username' not in login_data.keys() or login_data['username'] == "":
                response_data['status'] = 'error'
                response_data['message'] = 'username can\'t be void'
                return JsonResponse(response_data)
            else:
                username = login_data['username']
            if 'password' not in login_data.keys() or login_data['password'] == "":
                response_data['status'] = 'error'
                response_data['message'] = 'password can\'t be void'
                return JsonResponse(response_data)
            else:
                password = login_data['password']
                
            try:
                login_object = User.objects.get(username = username)
            except:
                response_data['status'] = "error"
                response_data['message'] = "no this username"
                return JsonResponse(response_data)
            if password == login_object.password :
                request.session['id'] = login_object.id
                response_data['status'] = 'success'
                response_data['message'] = 'success'
                return JsonResponse(response_data)
            else:
                response_data['status'] = 'error'
                response_data['message'] = 'password error'
                return JsonResponse(response_data)
    else:
        response_data['status'] = 'error'
        response_data['message'] = 'method error'
        return JsonResponse(response_data)

@csrf_exempt
def register(request):
    '''
    this function for register
    :param request: HttpRequest for register
    :return: {response_data}dict message and code for register status
    '''
    response_data = {}
    if request.method == "POST":
        if 'id' in request.session.keys():
            response_data['status'] = 'error'
            response_data['message'] = 'you have log in'
            return JsonResponse(response_data)
        else:
            register_data = QueryDict(request.body)
            if 'username' not in register_data.keys() or register_data['username'] == "":
                response_data['status'] = 'error'
                response_data['message'] = 'username can\'t be void'
                return JsonResponse(response_data)
            else:
                username = register_data['username']
            if 'password' not in register_data.keys() or register_data['password'] == "":
                response_data['status'] = 'error'
                response_data['message'] = 'password can\'t be void'
                return JsonResponse(response_data)
            else:
                password = register_data['password']
        
            try:
                User.objects.get(username=username)
                response_data['status'] = "error"
                response_data['message'] = "the username exist"
                return JsonResponse(response_data)
            except:
                pass
            user = User(username = username,password = password)
            user.save()
            
            request.session['id'] = user.id
            response_data['status'] = 'success'
            response_data['message'] = 'success'
            return JsonResponse(response_data)
            
    else:
        response_data['status'] = 'error'
        response_data['message'] = 'method error'
        return JsonResponse(response_data)

@csrf_exempt
def logout(request):
    """
    this function for logout
    :param request: HttpRequest for logout
    :return: {response_data}dict message and code for logout status
    """
    response_data = {}
    if 'id' in request.session.keys():
        request.session.clear()
        response_data['status'] = "success"
        response_data['message'] = "success"
        return JsonResponse(response_data)
    else:
        response_data['status'] = "error"
        response_data['message'] = "you have not login"
        return JsonResponse(response_data)