from django.db.models import fields
from rest_framework import serializers
from .models import Good, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ("id", "category_id", "name", "price")
    