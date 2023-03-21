# Imort the AppConfig class from django.apps
from django.apps import AppConfig

# Define a custom BookstoreConfig class, that extends AppConfig
class BookstoreConfig(AppConfig):
# Specify default primary key field type for any models in this app as BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
# Specify the name of the app
    name = 'bookstore'
