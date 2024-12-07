from django.contrib import admin
from apps.settings.models import BurgerMenu,SocialMedia,BurgerBigMenu
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