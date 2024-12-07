from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReviewForm
import telebot
from django.conf import settings

# Инициализация бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_TOKEN)
ADMIN_CHAT_ID = settings.ADMIN_CHAT_ID

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()  # Сохраняем отзыв в базе данных
            # Отправляем отзыв в Telegram
            bot.send_message(ADMIN_CHAT_ID, f"Новый отзыв\n имя: {review.name}\n почта: ({review.email})\n сообщение: {review.message}")
            return HttpResponse("Thank you for your review!")
    else:
        form = ReviewForm()

    return render(request, 'submit_review.html', {'form': form})
