from rest_framework import serializers
from blogapp.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields= ['user','title','blogpost','id','created']