# Generated by Django 4.0.5 on 2022-06-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_eror404_img_eror404_img1_eror404_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='Checkout about')),
                ('img1', models.ImageField(upload_to='media', verbose_name='Checkout img1')),
                ('img2', models.ImageField(upload_to='media', verbose_name='Checkout img2')),
                ('img3', models.ImageField(upload_to='media', verbose_name='Checkout img3')),
            ],
            options={
                'verbose_name': 'Chekcout',
                'verbose_name_plural': 'Chekcouts',
            },
        ),
    ]
