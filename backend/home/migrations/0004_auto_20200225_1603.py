# Generated by Django 2.2.10 on 2020-02-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_customtext_testing'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='password',
            field=models.TextField(blank=True, null=True),
        ),
    ]
