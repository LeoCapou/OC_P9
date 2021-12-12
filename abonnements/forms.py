from django import forms

class FollowForm(forms.Form):
    target_user = forms.CharField(label='',
            widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}),
            required=False,
        )