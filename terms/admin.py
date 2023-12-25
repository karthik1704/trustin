from django.contrib import admin
from django.db import models

from terms.models import TermsAndCondition
from mdeditor.widgets import MDEditorWidget

# Register your models here.

admin.site.register(TermsAndCondition)