from django.db import models


# Create your models here.
class Career(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre carrera', unique=True)
    DICT_CODE = [
        ('IINF', 'IINF'), ('IGEM', 'IGEM'), ('ISIC', 'ISIC'), ('IMCT','IMCT'), ('IIND','IIND'), ('IIAL', 'IIAL')
    ]
    code = models.CharField(choices=DICT_CODE, default='INGF', max_length=5)

    def __str__(self):
        return "Carrera: {0}- {1}".format(self.code, self.name)

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'


class Organizations(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre organización')
    entidad = models.CharField(verbose_name='Entidad', max_length=100)
    localidad = models.CharField(verbose_name='Localidad', max_length=100)
    municipio = models.CharField(verbose_name='Municipio', max_length=100)
    domicilio = models.CharField(verbose_name='Domicilio', max_length=100)
    cp = models.CharField(verbose_name='Código Postal', max_length=10)
    email = models.CharField(verbose_name='Correo electronico', max_length=100)
    telefono = models.CharField(verbose_name='Telefono', max_length=10)

    def __str__(self):
        return "Organización: {0}".format(self.name)

    class Meta:
        verbose_name = 'Organización'
        verbose_name_plural = 'Organizaciones'


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre Contacto')
    DICT_PARENTS = [
        ('Padre', 'Padre'), ('Madre', 'Madre'), ('Hermano', 'Hermano'), ('Hermana', 'Hermana'),
        ('Tio', 'Tio'), ('Tia', 'Tia'), ('Abuelo', 'Abuelo'), ('Abuela', 'Abuela'), ('Otro', 'Otro')
    ]
    parents = models.CharField(verbose_name='Parentesco', choices=DICT_PARENTS, default='Madre', max_length=20)
    entidad = models.CharField(verbose_name='Entidad', max_length=100)
    localidad = models.CharField(verbose_name='Localidad', max_length=100)
    municipio = models.CharField(verbose_name='Municipio', max_length=100)
    domicilio = models.CharField(verbose_name='Domicilio', max_length=100)
    cp = models.CharField(verbose_name='Código Postal', max_length=10)
    email = models.CharField(verbose_name='Correo electronico', max_length=100)
    telefono = models.CharField(verbose_name='Telefono', max_length=10)

    def __str__(self):
        return "Contacto: {0}".format(self.name)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


class Students(models.Model):
    N_control = models.CharField(verbose_name='Número de control', max_length=10, unique=True)
    name = models.CharField(verbose_name='Nombre',max_length=100)
    career_id = models.ForeignKey(Career, on_delete=models.DO_NOTHING, verbose_name='Carrera')

    def __str__(self):
        return "Alumno: {0}".format(self.name)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'


class Teachers(models.Model):
    huella = models.CharField(verbose_name='Identificación', max_length=10, unique=True)
    name = models.CharField(verbose_name='Nombre', max_length=100)
    career_id = models.ForeignKey(Career, on_delete=models.DO_NOTHING, verbose_name='Carrera')

    def __str__(self):
        return "Docente: {0}".format(self.name)

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'


class Residences(models.Model):
    Students_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING, verbose_name='Alumno')
    Teachers_id = models.ForeignKey(Teachers, on_delete=models.DO_NOTHING, verbose_name='Docente')
    Organizations_id = models.ForeignKey(Organizations, on_delete=models.DO_NOTHING, verbose_name='Organización')
    clave = models.CharField(verbose_name='Clave', max_length=10)
    name = models.CharField(verbose_name='Nombre del proyecto', max_length=100)
    status = models.CharField(verbose_name='Estado del proyecto', max_length=50)
    qualification = models.DecimalField(verbose_name='Calificación', max_digits=10, decimal_places=2)
    period = models.CharField(verbose_name='Periodo', max_length=50)

    def __str__(self):
        return "Residencia: {0} ".format(self.name)

    class Meta:
        verbose_name = 'Residencia'
        verbose_name_plural = 'Residencias'
