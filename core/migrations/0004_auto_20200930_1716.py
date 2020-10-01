# Generated by Django 3.1.1 on 2020-09-30 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20200930_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
    ]