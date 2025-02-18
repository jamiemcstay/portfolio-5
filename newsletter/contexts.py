from .forms import NewsLetterForm


def newsletter_form(request):
    """Make newsletter form available across all templates"""
    newsletter_form = NewsLetterForm()
    return {'newsletter_form': newsletter_form}
