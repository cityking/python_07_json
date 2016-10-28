# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Poem
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

# Create your views here.
def add(request):
	if request.is_ajax():
		a = request.GET['a']
		b = request.GET['b']

		a = int(a)
		b = int(b)
		return HttpResponse(str(a+b))

def add2(request,a,b):
	if request.is_ajax():
		ajax_string = "ajax request:"	
	else:
		ajax_string = "not ajax request:"
	
	c = int(a) + int(b)
	return HttpResponse(ajax_string+str(c))

def home(request):
	return render(request, 'home.html')

import json

def ajax_list(request):
	a = range(100)
	#return HttpResponse(json.dumps(a), content_type="application/json")
	return JsonResponse(a)

def ajax_dict(request):
	dict_addr = {'cityking':'china sicuan langzhong', 'chenhai':'sichuan guangan'}
	#return HttpResponse(json.dumps(dict_addr), content_type="application/json")
	return JsonResponse(dict_addr)

def ajax_complex(request):
	dict_list = [
		{"name":"xiaoming", "age":20},
	        {"name":"tuweizhong", "age":24},
		{"name":"xiaoli", "age":33},
	]
	return JsonResponse(dict_list)

class JsonResponse(HttpResponse):
	def __init__(self, content={}, content_type = 'application/json'):
		super(JsonResponse, self).__init__(content=json.dumps(content), content_type=content_type)
		




def more_poems(request):
	if request.is_ajax():
		objects = Poem.objects.all()
		data = get_json_objects(objects, Poem)
		return HttpResponse(data, content_type="application/json")
	else:
		return Http404()

def json_field(field_data):
	if isinstance(field_data, str):
		return "\""+field_data+"\""
	if isinstance(field_data, bool):
		if field_data:
			return 'true'
		else:
			return 'false'
	return "\""+str(field_data)+"\""

def json_encode_dict(dict_data):


	json_data = "{"
	for(k, v) in dict_data.items():
		json_data = json_data + json_field(k) + ":" + json_field(v) + ", "
	json_data = json_data[:-2] + "}"
	return json_data

def json_encode_list(list_data):
	json_data = "["
	for item in list_data:
		json_data = json_data + json_encode_dict(item) + ", "

	return json_data[:-2]+"]"

def get_json_objects(objects, model_meta):
	concrete_model = model_meta._meta.concrete_model
	list_data = []
	for obj in objects:
		dict_data = {}
		for field in concrete_model._meta.local_fields:
			key = field.name
			if key == 'id':
				continue
			value = field.value_from_object(obj)
			dict_data[key]=value
		list_data.append(dict_data)

	data = json_encode_list(list_data)
	return data


import ast
def add_poems(request):
	if request.is_ajax() and request.POST:
		json_str = request.POST.get("poems")
		data = "post success"
		json_list = ast.literal_eval(json_str)
		for item in json_list:
			new_obj = Poem()
			for field in item:
				setattr(new_obj, field, item[field])
			print(new_obj.author, new_obj.title)
			new_obj.save()
		return HttpResponse(data, content_type="application/text")
	else:
		return Http404

