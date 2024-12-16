from django.contrib import admin
from apps.settings.models import BurgerMenu,SocialMedia,BurgerBigMenu,BurgerMenuDetail
# Register your models here.
@admin.register(BurgerMenu)
class BurgerMenuAdmin(admin.ModelAdmin):
    list_display = ('title','description','price')
@admin.register(SocialMedia)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('facebook','instagram','twitter','google_plus')
@admin.register(BurgerBigMenu)
class BurgerBigMenuAdmin(admin.ModelAdmin):
    list_display = ('title','description','price')
@admin.register(BurgerMenuDetail)
class BurgerMenuDetailAdmin(admin.ModelAdmin):
    list_display = ('title','description','price')
    search_fields = ['title','description','price']
    list_filter = ('title','description')
