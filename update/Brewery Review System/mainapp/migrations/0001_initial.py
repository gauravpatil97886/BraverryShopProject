# Generated by Django 4.2.7 on 2023-12-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('brewery_id', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
