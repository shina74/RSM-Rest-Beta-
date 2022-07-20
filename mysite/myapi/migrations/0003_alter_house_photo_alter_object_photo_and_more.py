# Generated by Django 4.0.6 on 2022-07-17 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapi', '0002_category_house_object_objectcategory_place_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='photo',
            field=models.FilePathField(null=True, path='/'),
        ),
        migrations.AlterField(
            model_name='object',
            name='photo',
            field=models.FilePathField(null=True, path='/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.FilePathField(null=True, path='/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.FilePathField(null=True, path='/'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.userprofile'),
        ),
    ]