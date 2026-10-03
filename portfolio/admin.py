from django.contrib import admin

from .models import Project, Skill, Service, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "technology",
        "featured",
        "created_at",
    )

    list_filter = (
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "technology",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "order",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "order",
        "name",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "order",
        "title",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "is_read",
    )