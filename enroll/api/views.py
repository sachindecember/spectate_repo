from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import snippetserializer
from enroll.models import snippet


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        '/api/snippet_list/',
        '/api/snippet-detail/<str:pk>/',
        '/api/snippet-create/',
        '/api/snippet-update/<str:pk>/',
        '/api/snippet-delete/<str:pk>/',
    ]
    return Response(routes)


# def overviewapis(request):
#     apiurls = {
#         'list':'/api/snippet_list/',

#     }
@api_view(['GET'])
def snippetlist(request):
    snippets = snippet.objects.all()
    serializer = snippetserializer(snippets,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def snippetdetail(request,pk):
    snippets = snippet.objects.get(id=pk)
    serializer = snippetserializer(snippets,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def snippetcreate(request):
    serializer = snippetserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def snippetupdate(request,pk):
    snippets = snippet.objects.get(id=pk)
    serializer = snippetserializer(instance=snippets,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def snippetdelete(request,pk):
    snippets = snippet.objects.get(id=pk)
    tasks.delete()
    return Response('successfully deleted')