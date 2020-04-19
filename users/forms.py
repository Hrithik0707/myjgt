from django import forms
from .models import Form
class Detail_form(forms.ModelForm):
    class Meta:
        model = Form
        fields = [
            'Name',
            'Date',
            'Reports', 
            'Team_lead',
            'No_of_hours',
            'Todays_progress',
            'Todays_documents',
            'Concern',
            'Next_document', 
            'Next_plan',
        ]