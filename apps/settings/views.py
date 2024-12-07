from django.shortcuts import render,redirect
from apps.settings.models import BurgerMenu,SocialMedia,BurgerBigMenu
from django.http import HttpResponse
from apps.telegram.models import Review
from django.conf import settings
import telebot
# Create your views here.
def index(request):
    burgers = BurgerMenu.objects.all()
    return  render(request, 'index.html', locals())

def menu(request):
    burger = BurgerBigMenu.objects.all()
    social = SocialMedia.objects.latest('id')
    return  render(request, 'Menu.html', locals())

def about(request):
    return render(request, 'about.html', locals())
def contact(request):
    return render(request, 'contact.html', locals())
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_TOKEN)
ADMIN_CHAT_ID = settings.ADMIN_CHAT_ID

def submit_review(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        review = Review.objects.create(name=name, email=email, message=message)
        
        bot.send_message(ADMIN_CHAT_ID, f"New review from {name}:\n\n{message}")
        
        return HttpResponse("Thank you for your review!")
    return render(request, "submit_review.html")
