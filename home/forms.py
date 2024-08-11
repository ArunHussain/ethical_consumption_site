from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from .models import survey_answers, comments



#the below is extending Django's default UserCreationForm as currently...
#...it only allows the user to input username and password...
#... but with the custom user model they have to be able to...
#... input for the user type field as well.
class UserCreationForm(UserCreationForm):
    
    user_email=forms.CharField(max_length=30, required=False)   
    #^Required=True makes it so that users have to choose their type.
    
#Inside the "class Meta:" part, the model which the form takes data for is chosen.
#Additionally, the particular fields of that model which the form is going to be ...
#...taking user inputs for are chosen.
    class Meta: 
        model = CustomUser 
        fields = ('username', 'user_email', 'password1', 'password2')
#^username, password1 and password2 are fields of Django's default user model.

#The default UserCreationForm's save function has to be overriden...
#...to make sure the user_type input is also saved to the user model.
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.user_email = self.cleaned_data["user_email"] 
        if commit:
            user.save()
        return user

class survey_form(forms.ModelForm):
    class Meta: 
        model = survey_answers
        fields=['supports_fairtrade', 'supports_nochildlabor', 'supports_lowcarbonemissions','supports_noanimaltesting','placeholder']
        labels={'supports_fairtrade':'Is only buying fairtrade products important to you when shopping?',
        'supports_nochildlabor':'Does the use of child labor by a company mean you don\'t purchase from them?',
        'supports_lowcarbonemissions':'Do you care about the carbon emissions of a company you purchase form being reasonable?',
        'supports_noanimaltesting':'Does the use of animal testing deter you from a company?'}
 
class comment_form(forms.ModelForm):
    class Meta:
        model = comments
        fields=['body']
        labels={'body':'body'}
        
