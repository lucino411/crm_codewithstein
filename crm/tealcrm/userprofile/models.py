from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    user = models.OneToOneField(
        User, related_name='userprofile', on_delete=models.CASCADE)


'''
En el shell de django:

>>> from django.contrib.auth.models import User
>>> from userprofile.models import Userprofile
>>> superuser = User.objects.get(pk=1)
>>> superuser
<User: admin>
>>> Userprofile.objects.create(user=superuser)
<Userprofile: Userprofile object (1)>

En el shell de Django, estás interactuando con tu base de datos y probando la funcionalidad de tu modelo Userprofile. Aquí hay un desglose de los comandos que usaste:

User.objects.get(pk=1): Este comando busca un usuario con la clave principal (id) igual a 1 en la base de datos y te devuelve el objeto de usuario correspondiente. En este caso, encontraste el superusuario con el nombre de usuario "admin".
Userprofile.objects.create(user=superuser): Aquí estás creando una instancia de Userprofile y vinculándola al superusuario que encontraste anteriormente. Esta línea de código crea una nueva entrada en la tabla userprofile_userprofile de la base de datos, con el campo user vinculado al superusuario que pasaste como argumento. El "(1)" al final indica que se ha creado un objeto Userprofile con el ID 1.

Estos comandos te permiten probar la funcionalidad de tu modelo Userprofile y verificar que está funcionando como se espera al vincularse con instancias de la clase User.

Tener en cuenta que a través de una relación de uno a uno definida por el campo OneToOneField() garantiza que cada instancia de User tenga solo una instancia correspondiente de Userprofile y viceversa. Por lo tanto, el usuario "admin" ya debe existir en la tabla auth_user de tu base de datos, y al crear la instancia de Userprofile, se establece la relación entre el usuario "admin" y el perfil de usuario reflejada en la base de datos en la tabla userprofile_userprofile.

Cuando utilizas un campo OneToOneField() en un modelo de Django, se crea una relación uno a uno entre dos modelos, lo que genera una nueva tabla en la base de datos con las dos columnas, id y user_id. La columna id es el identificador único de la relación y user_id es la clave externa que referencia al usuario en la tabla auth_user. Este comportamiento es estándar para el campo OneToOneField en Django.

NOTA: se esta usando models.py del app : userprofile
'''
