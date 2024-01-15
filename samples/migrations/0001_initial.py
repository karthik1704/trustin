# Generated by Django 4.2.7 on 2024-01-01 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(editable=False, max_length=255)),
                ('product_name', models.CharField(max_length=255, verbose_name='Product/Sample Name')),
                ('description', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_branch', to='branches.branch')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestingParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_code', models.CharField(max_length=255)),
                ('testing_parameters', models.CharField(max_length=255)),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='Amount')),
                ('method_or_spec', models.CharField(blank=True, max_length=255, null=True, verbose_name='Method / Specification')),
                ('group_of_test_parameters', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter_branch', to='branches.branch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='para_product', to='samples.product')),
                ('test_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='parameter_test_type', to='samples.testtype')),
            ],
        ),
    ]
