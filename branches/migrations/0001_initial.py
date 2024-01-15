# Generated by Django 4.2.7 on 2024-01-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=255, unique=True)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile_number', models.PositiveBigIntegerField()),
                ('landline_number', models.CharField(blank=True, max_length=19, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('pan_no', models.CharField(blank=True, max_length=20, null=True)),
                ('cin', models.CharField(blank=True, max_length=50, null=True)),
                ('gstin', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_details', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
