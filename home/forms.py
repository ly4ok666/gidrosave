from django import forms
# Модель формы обратной связи
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
#     sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
#     copy = forms.BooleanField(required=False)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"