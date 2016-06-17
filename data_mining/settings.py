"""
Django settings for data_mining project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-df6%_+18+w_x3cw*b5#8l9lw1u%69ym@xs#!=9cl_--m%qv#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'data_mining',
    'social_auth',
    'allauth',
    'allauth.account',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'data_mining.urls'

WSGI_APPLICATION = 'data_mining.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'data_mining/static',
)

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/accounts/login/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

TEMPLATE_DIRS = (
  'jaqpot_ui/templates',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.contrib.readability.ReadabilityBackend',
    'social_auth.backends.contrib.fedora.FedoraBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY         = 'm69DRR5qxEl8DDYzmNkOgI3dX'
TWITTER_CONSUMER_SECRET      = 'gHtJr6z7qlJxBI6XqWJ8NTi9kAQxpFJ0TKSlBSR0vnSMGSOYY4'
FACEBOOK_APP_ID              = '188714861496456'
FACEBOOK_API_SECRET          = '95071c9888bb7bbad4b695c9271feb61'
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = 'anonymous'
GOOGLE_CONSUMER_SECRET       = 'anonymous'
GOOGLE_OAUTH2_CLIENT_ID      = '627494330377-i453drmks3pp1hr78m3hb7bct0etpvja.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '4LqzCRH2x-m-kHaoiTqTEVE9'
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = ''
LIVE_CLIENT_SECRET           = ''
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = ''
YAHOO_CONSUMER_SECRET        = ''
READABILITY_CONSUMER_SECRET  = ''


SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

'''SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'myapp.pipeline.set_google_credentials'
    # more pipelines
)'''

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'user_friends',
    'friends_location',
    'picture'
]

FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_friends', 'user_likes', 'public_profile', 'user_about_me', 'user_likes',
                                 'user_photos', 'user_posts', 'user_relationships','user_relationship_details',
                                 'user_tagged_places', 'user_videos', 'user_website','user_work_history',
                                 'user_birthday', 'user_education_history', 'user_events', 'user_games_activity', 'user_hometown',
                                 'user_actions.books', 'user_actions.fitness','user_actions.music','user_actions.news',
                                'user_actions.video']