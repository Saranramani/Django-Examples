from .models import Item
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(requset):
    todo = Item.objects.all()
    serializer = ItemSerializer(todo, many=True)
    return Response(serializer.data,status=200)


@api_view(['GET'])
def getById(request,id):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item,many=False)
    return Response(serializer.data,status=200)

@api_view(['POST'])
def addData(request):
    serial = ItemSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
    return Response(serial.data,status=201)

@api_view(['PUT'])
def updateData(request,id):
    pk_id = Item.objects.get(id=id)
    datas = ItemSerializer(pk_id,data=request.data)
    if datas.is_valid():
        datas.save()
    return Response(datas.data,status=200)

@api_view(['DELETE'])
def deleteData(request,id):
    del_id = Item.objects.get(id=id)
    del_id.delete()
    return Response("Deleted successfully",status=204)