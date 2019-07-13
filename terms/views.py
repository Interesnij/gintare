from django.shortcuts import render
from generic.mixins import CategoryListMixin
from django.views.generic.base import TemplateView

class TermsView(TemplateView,CategoryListMixin):
    template_name="terms.html"
