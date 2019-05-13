# Generated by Django 2.0.2 on 2019-05-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
