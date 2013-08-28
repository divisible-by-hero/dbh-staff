from django.contrib import admin
from staff.models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'published')
    prepopulated_fields = {'slug': ('first_name','last_name')}
    fieldsets = (
        (None, {
            'fields': (('user', 'published'), ('first_name', 'last_name'), 'slug',)
        }),
        (None, {
            'fields': ('position', 'description', 'email', 'profile_picture',)
        }),
    )
    save_on_top = True
    list_filter = ('published',)
    actions = ['publish', 'unpublish']

    def publish(self, request, queryset):
        rows = queryset.update(published=True)
        if rows == 1:
            message_bit = "1 staff member was"
        else:
            message_bit = "%s staff members were" % rows
        self.message_user(request, "%s successfully published." % message_bit)

    def unpublish(self, request, queryset):
        rows = queryset.update(published=False)
        if rows == 1:
            message_bit = "1 staff member was"
        else:
            message_bit = "%s staff members were" % rows
        self.message_user(request, "%s successfully un-published." % message_bit)

admin.site.register(Staff, StaffAdmin)
