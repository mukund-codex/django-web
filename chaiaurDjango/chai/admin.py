from django.contrib import admin
from .models import ChaiVarity, ChaiReview, ChaiStore, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    # filter_horizontal = ('chai_varities',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date')

admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(ChaiStore, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)