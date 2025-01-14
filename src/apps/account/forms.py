from django import forms

class LoginUser(forms.Form):
    def __init__(self,*args, **kwargs):
        super(LoginUser,self).__init__(*args, **kwargs)
        for item in LoginUser.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    email=forms.CharField(required=True,label="Email",widget=forms.EmailField)
    password=forms.CharField(required=True,label="Password",widget=forms.PasswordInput)

class RegisterUser(forms.Form):
    def __init__(self,*args, **kwargs):
        super(RegisterUser,self).__init__(*args, **kwargs)
        for item in RegisterUser.visible_fields(self):
            item.field.widget.attrs["class"] = "form-control"

    email=forms.CharField(required=True,label="Email",widget=forms.EmailField)
    username=forms.CharField(required=True,label="Username")
    password=forms.CharField(required=True,label="password",widget=forms.PasswordInput)
    confirm_password=forms.CharField(required=True,label="Confirm Password",widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data



