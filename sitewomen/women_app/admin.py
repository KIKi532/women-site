from django.contrib import admin
from .models import *
from django.contrib import messages
from django.utils.safestring import mark_safe

class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус жінок'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Заміжня'),
            ('single', 'незаміжня')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_photo', 'time_create',
                    'is_published', 'cat')
    readonly_fields = ['post_photo']
    list_display_links = ('title', )
    list_editable = ('is_published',)
    ordering = ['time_create', 'title']
    search_fields = ['title', 'cat__name']
    actions = ['set_published']
    list_per_page = 5
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    prepopulated_fields = {'slug': ("title",)}
    fields = ['title', 'slug', 'photo', 'post_photo', 'content', 'cat', 'husband', 'tags']
    filter_horizontal = ['tags']
    save_on_top = True

    def post_photo(self, women: Women):
        """відображення фото в адмін-панелі"""
        if women.photo:
            return mark_safe(f'<img src="{women.photo.url}" width=50>')
        return 'Без фото'

    @admin.action(description="Опублікувати вибрані записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Змінено {count} записів")

    @admin.action(description='Зняти з публікації вибрані записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записи зняті з публикації!", messages.WARNING)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(UploadFiled)
class FileUploadAdmin(admin.ModelAdmin):
    pass

@admin.register(TagPost)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    prepopulated_fields = {'slug': ('tag',)}




# admin.site.register(Women, WomenAdmin)
# admin.site.register(Category)
admin.site.register(Husband)
