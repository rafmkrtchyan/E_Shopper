# Generated by Django 4.0.5 on 2022-06-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_blogsingle2_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Cart name')),
                ('img', models.ImageField(upload_to='media', verbose_name='Cart img')),
                ('about', models.TextField(verbose_name='Cart about')),
                ('price', models.IntegerField(verbose_name='Cart  price')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
    ]