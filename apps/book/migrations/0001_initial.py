# Generated by Django 4.1.6 on 2023-02-11 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('categories', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='accounts.user')),
                ('book_tags', models.ManyToManyField(related_name='book_tags', to='categories.tag')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='categories.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['-id'],
            },
        ),
    ]