# Generated by Django 3.1 on 2020-10-11 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20201011_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='badtopic',
            options={'verbose_name': 'Giám sát Chủ đề xấu độc', 'verbose_name_plural': 'Giám sát Chủ đề xấu độc'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Giám sát Channel xấu độc', 'verbose_name_plural': 'Giám sát Channel xấu độc'},
        ),
        migrations.AddField(
            model_name='youtubeclip',
            name='bad_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.badtopic', verbose_name='Nhóm chủ đề'),
        ),
    ]