from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from checkout.webhook_handler import StripeWH_Handler
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    logger = logging.getLogger(__name__)

    logger.debug(f"Using webhook secret: {wh_secret}")

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    if not sig_header:
        return HttpResponse("Missing Stripe signature", status=400)

    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
        logger.info(f"Webhook event received: {json.dumps(event, indent=4)}")
    except ValueError as e:
        logger.error(f"Invalid payload: {e}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"Invalid signature: {e}")
        return HttpResponse(status=400)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return HttpResponse(content=e, status=400)

    handler = StripeWH_Handler(request)

    # Map webohook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
            handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook from Stripe

    event_type = event['type']
    # logger.info(f"Processing webhook event type: {event_type}")

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response
