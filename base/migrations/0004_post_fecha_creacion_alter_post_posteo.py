# Generated by Django 4.1.2 on 2024-08-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_nombre_post_autor_post_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posteo',
            field=models.TextField(),
        ),
    ]
