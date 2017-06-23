from django import forms

from .models import Action

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('title',
                  'description',
                  'date',
                  'context',
                  'contexts',
                  'tags',
                  'oneNoteReference',
                  'outlookReference',
                  'source',
                  'status',
                  'tags',
                  'lists',
                  'project',
                  'horizon',
                  'delegatedTo',
                )

        widgets = {'horizon' : forms.RadioSelect,
                   'contexts' : forms.CheckboxSelectMultiple,}
    
    
    
    
    
    
    
    
    