# Generated by Django 4.2.2 on 2023-06-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_requestlostitem_sub_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestlostitem',
            old_name='discription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='founditem',
            name='status',
            field=models.CharField(choices=[('T', 'TRAKING'), ('M', 'MATCHED'), ('F', 'FOUND'), ('N', 'NOMATCH')], default='F', max_length=100),
        ),
    ]
