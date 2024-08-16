#Se importa el módulo de formularios de Django
from django import forms
#Se importa varios formularios prediseñados de autenticación de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, SetPasswordForm, PasswordResetForm
#Se importa el modelo de usuario predeterminado de Django
from django.contrib.auth.models import User
#Se importa el modelo "Perfil" (tabla) del modulo
from .models import Perfil


"""
Se hereda de "AuthenticationForm" para el inicio de sesión.
Personalice los campos "username" y "password" con etiquetas y widgets
específicos para agregar clases CSS.
"""

class LoginForm(AuthenticationForm):
    username = UsernameField(label= 'Usuario', widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    

"""
Se hereda de "UserCreationForm" para el registro de nuevos usuarios.
Personalice los campos "username", "email", "password1" y "password2".
La clase "Meta" define el modelo "User" y los campos a incluir en el formulario.

"""

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label= 'Usuario', widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

""" 
Se hereda "SetPasswordForm" para cambiar la contraseña actual.
Personalice los campos de "password1" y "password2" para el ingreso de contraseña.
"""

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


""" 
Se hereda de "PasswordChangeForm" para cambiar la contraseña actual.
Personalice los campos "old_password" y "new_password1" - "new_password2".
"""

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Antigua Contraseña', widget=forms.PasswordInput(attrs={'autofocus':'True', 'autocomplete':'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


""" 
Se hereda de "PasswordResetForm" para establecer la contraseña a través del
correo dado.
"""

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


""" 
Se hereda de "forms.ModelForm" para actualizar el perfil del usuario.
La clase "Meta" define el modelo "Perfil" y los campos a incluir en el formulario.
Personaliza los campos con los widgets.
"""

    
class PerfilProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'localidad', 'ciudad', 'telefono', 'departamento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'departamento': forms.Select(attrs={'class':'form-control'}),
        }
        

""" 
Estos formularios me permitirán manejar la autenticación y el perfil del usuario en 
VLADI STORE. Con campos personalizados en español y su apariencia con CSS.
"""

""" 
Los "widgets" se encargan de renderizar HTML para representar un campo de formulario en la
interfaz de la página. 

1. TextInput: Representa un campo de entrada de texto.
2. PasswordInput: Representa un campo de entrada de contraseña.
3. EmailInput: Representa un campo de entrada de correo electrónico.
4. NumberInput: Representa un campo de entrada de número.
5. Select: Representa un menú desplegable.

"""

""" 
Los "attrs" son diccionarios de atributos HTML que se aplican en los formularios
para personalizar su apariencia y comportamientos. Se pueden incluir CSS y JS.

1. Los "attrs" se pasa como un argumento al "widget" de un campo de un formulario.
2. "autofocus": Indica que el campo debería recibir automáticamente el foco cuando la página se cargue.
3. "class": Define una clase CSS (form-control) para el campo de entrada. 
"""