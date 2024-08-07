# Generated by Django 5.0.6 on 2024-07-18 06:58

import django.db.models.deletion
import django.db.models.functions.text
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_language'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.RemoveConstraint(
            model_name='language',
            name='language_name_case_insensitive_unique',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Language the book is written in', to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Enter the language the book is written in.', max_length=200, unique=True),
        ),
        migrations.AddConstraint(
            model_name='language',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='language_name_case_insensitive_unique', violation_error_message='Language already exists (case insensitive match)'),
        ),
    ]
