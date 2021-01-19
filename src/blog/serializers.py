from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id"
            "category_name"
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "comment_content",
            "comment_added_date"
        )

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = (
            "id",
            "post_title",
            "post_content",
            "comment_count",
            "view_count",
            "like_count",
            "comments"
        )