from django.shortcuts import render
import logging


def index(request):
    return render(request, 'home/index.html')


logger = logging.getLogger(__name__)


def custom_404(request, exception):
    logger.error(f"404 error: {exception}")
    return render(request, '404.html', status=404)
