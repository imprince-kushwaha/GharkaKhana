from django.contrib import admin

# Register your models here.
from myApp.models import Food_Donation,Food_Section,Contact,Address,Payment,Order

admin.site.register(Food_Donation)
admin.site.register(Food_Section)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Order)




