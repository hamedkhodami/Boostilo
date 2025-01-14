from django import forms


class ContactUsForms(forms.Form):
    def __init__(self,*args, **kwargs):
        super(ContactUsForms,self).__init__(*args, **kwargs)
        for item in ContactUsForms.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    fullname = forms.CharField(required=True,label='FullName',max_length=100,)
    email = forms.CharField(required=True,label='Email Address',widget=forms.EmailField)
