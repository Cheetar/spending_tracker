from django.contrib import admin

from tracker.models import Board, Category, Profile, Spending


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'board')


class SpendingAdmin(admin.ModelAdmin):
    list_display = ('name', 'board', 'category', 'cost', 'date', 'is_income')


admin.site.register(Profile)
admin.site.register(Board, BoardAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Spending, SpendingAdmin)
