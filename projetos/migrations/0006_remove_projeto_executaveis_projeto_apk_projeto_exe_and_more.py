# Generated by Django 5.0.7 on 2024-12-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0005_projeto_capa_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='executaveis',
        ),
        migrations.AddField(
            model_name='projeto',
            name='apk',
            field=models.FileField(blank=True, null=True, upload_to='apk/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='exe',
            field=models.FileField(blank=True, null=True, upload_to='exe/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='linux',
            field=models.FileField(blank=True, null=True, upload_to='linux/%Y/%m/%d/'),
        ),
    ]
