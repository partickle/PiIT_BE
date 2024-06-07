from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .serializers import NewsSerializer


class NewsListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailView(APIView):
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        news = self.get_object(pk)
        if news is None:
            return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        news = self.get_object(pk)
        if news is None:
            return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        news = self.get_object(pk)
        if news is None:
            return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
