from django.contrib import admin

from tracker.models import Board, Profile, Spending


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


class SpendingAdmin(admin.ModelAdmin):
    list_display = ('name', 'board', 'category', 'cost', 'date', 'is_income')


admin.site.register(Profile)
admin.site.register(Board, BoardAdmin)
admin.site.register(Spending, SpendingAdmin)
