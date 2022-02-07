from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Brand)
admin.site.register(UpdateProfileImage)
admin.site.register(Contact)
admin.site.register(Wishlist)

# Register your models here.
