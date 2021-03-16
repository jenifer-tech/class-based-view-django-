from app.models import Peri
from app.serializers import BasicSerializer
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class Basic(APIView):
    authentication_classes=[TokenAuthentication]       
    permission_classes=[IsAuthenticated]
    def get_object(self, pk): 
        try:
            no=Peri.objects.get(pk=pk)
            return no
        except no.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):     
        no=self.get_object(pk)      
        serializer=BasicSerializer(no)
        return Response(serializer.data)
       
    def put(self, request, pk): 
        authentication_classes=[TokenAuthentication]       
        permission_classes=[IsAuthenticated]        
        data={}  
        no=self.get_object(pk)                    
        serializer=BasicSerializer(no,data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data['radius'] = account.radius            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, pk):
        no=self.get_object(pk)                              
        no.delete()
        return Response({'response':"Account deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        
class Super(APIView):
    authentication_classes=[TokenAuthentication]       
    permission_classes=[IsAuthenticated]
    def get(self, request):               
        nu=Peri.objects.all()
        serializer=BasicSerializer(nu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):        
        data={}          
        serializer=BasicSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            a = account.radius            
            data['Area of circle is:']=3.14*a*a
            data['Perimeter of circle is:']=2*3.14*a            
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 






    

    

    