from django.contrib import admin
from django.apps import apps

# post_models = apps.get_app_config("mysite").get_models()
# process_models = apps.get_app_config("processes").get_models()
to_do_models = apps.get_app_config("todo").get_models()

for model in to_do_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# for model in process_models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# for model in user_models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass