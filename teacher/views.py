from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from teacher.serializers import TeacherSerializer
from teacher.models import Teachers

@csrf_exempt
def teacher_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = Teachers.objects.all()
        serializer = TeacherSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("serializer.data", status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def teacher_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = Teachers.objects.get(pk=pk)
    except Teachers.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TeacherSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)





