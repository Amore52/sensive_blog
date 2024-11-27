from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    raw_id_fields = ('author', 'tags')
    autocomplete_fields = ('likes',)
    def get_queryset(self, request):
        queryset = super().get_queryset(request).select_related('author').prefetch_related('tags', 'likes')
        return queryset


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'published_at', 'text')
    raw_id_fields = ('post', 'author')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
