# Generated by Django 3.1.3 on 2021-03-12 08:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import musicapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicapp', '0011_auto_20210218_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(13)]),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to=musicapp.models.upload_path),
        ),
        migrations.CreateModel(
            name='UserRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_from_user', models.FloatField(default=0, verbose_name='distance_from_user')),
                ('score', models.FloatField(default=0, verbose_name='rec_score')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thisuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'recommendation')},
                'index_together': {('user', 'recommendation')},
            },
        ),
    ]
