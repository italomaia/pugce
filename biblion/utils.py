from django.conf import settings

try:
    import twitter
except ImportError:
    twitter = None


def can_tweet():
    creds_available = (getattr(settings, "TWITTER_USERNAME", False) and
                       getattr(settings, "TWITTER_PASSWORD", False))
    return twitter and creds_available
