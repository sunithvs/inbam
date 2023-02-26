from datetime import datetime

from django.contrib import admin, messages

# Register your models here.
# from .models import Order


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date', 'price', 'status', 'file', 'delivery_date', 'delivery_address')
#     list_filter = ('status', 'date')
#     search_fields = ('name', 'description', 'status', 'file')
#     ordering = ('-date',)
#     date_hierarchy = 'date'
#     filter_horizontal = ()
#     list_per_page = 25
#     #     actions to change the status of the order
#     actions = ['make_pending', 'make_in_progress', 'make_completed']
#
#     # redirect to address admin page when clicking on the delivery address
#     def get_delivery_address(self, obj):
#         return '<a href="/admin/home/address/%s/">%s</a>' % (obj.delivery_address.id, obj.delivery_address)
#
#     def make_pending(self, request, queryset):
#         queryset.update(status='pending')
#         messages.success(request, "The status of the selected orders has been changed to pending")
#
#     make_pending.short_description = "Mark selected orders as pending"
#
#     def make_in_progress(self, request, queryset):
#         queryset.update(status='in progress')
#         messages.success(request, "The status of the selected orders has been changed to in progress")
#
#     make_in_progress.short_description = "Mark selected orders as in progress"
#
#     def make_completed(self, request, queryset):
#         queryset.update(status='completed')
#         messages.success(request, "The status of the selected orders has been changed to completed")
#
#     make_completed.short_description = "Mark selected orders as completed"
#
#     class Meta:
#         verbose_name_plural = "Orders"
#         proxy = True


#  upcoming orders

# class UpOrderAdmin(admin.ModelAdmin):
#
#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(delivery_date__gte=datetime.now())
#
#     def has_add_permission(self, request):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#     def has_module_permission(self, request):
#         return True
#
#     class Meta:
#         verbose_name_plural = "Upcoming Orders"
#
# #
# # admin.site.register(Order, UpOrderAdmin)
