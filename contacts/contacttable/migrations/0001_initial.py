# Generated by Django 3.2.8 on 2021-10-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Surname', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('Town', models.CharField(max_length=255)),
                ('Street', models.CharField(max_length=255)),
                ('Url', models.CharField(max_length=255)),
                ('Photo', models.CharField(max_length=255)),
            ],
        ),
    ]
