# Generated by Django 3.2.3 on 2021-05-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_rename_membertype_membershiptype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField(help_text='Numeric code field', unique=True)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_taxable', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]