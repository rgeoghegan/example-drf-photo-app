from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from photo.photo.models import Photo, PhotoUser


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo

class PhotoView(RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

class UserPhotosView(ListCreateAPIView):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        user = get_object_or_404(
            PhotoUser.objects,
            pk=self.kwargs['user_id']
        )
        return Photo.objects.filter(user=user)



