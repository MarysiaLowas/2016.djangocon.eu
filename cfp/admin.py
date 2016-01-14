from django.contrib import admin

from .models import Proposal


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    exclude = ['name', 'email', 'speaker_information']
    list_per_page = 200
