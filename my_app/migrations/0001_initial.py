# Generated by Django 4.0.5 on 2022-07-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=200)),
                ('news_compound', models.TextField()),
                ('news_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
