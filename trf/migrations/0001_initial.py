# Generated by Django 4.2.7 on 2023-12-06 06:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
        ('customers', '0001_initial'),
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_name', models.CharField(max_length=255)),
                ('batch_or_lot_no', models.CharField(max_length=255)),
                ('manufactured_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('batch_size', models.IntegerField()),
                ('received_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TRF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trf_code', models.CharField(editable=False, max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=255)),
                ('customer_address_line1', models.CharField(blank=True, default='', max_length=255)),
                ('customer_address_line2', models.CharField(blank=True, default='', max_length=255)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode_no', models.CharField(max_length=100)),
                ('gst_no', models.CharField(max_length=100)),
                ('date_of_registration', models.DateField(default=django.utils.timezone.now)),
                ('date_of_recived', models.DateField(default=django.utils.timezone.now)),
                ('test_type', models.CharField(max_length=255)),
                ('test_method', models.CharField(max_length=255)),
                ('sample_id', models.CharField(max_length=255)),
                ('sample_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('manufactured_by', models.CharField(max_length=255)),
                ('batch_or_lot_no', models.CharField(max_length=255)),
                ('manufactured_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('batch_size', models.IntegerField()),
                ('received_quantity', models.IntegerField()),
                ('expectation_delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('format_name', models.CharField(max_length=255)),
                ('nabl_logo', models.BooleanField(default=False)),
                ('no_of_samples', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trf_branch', to='branches.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trf_customer', to='customers.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trf_product', to='samples.product')),
            ],
        ),
        migrations.CreateModel(
            name='TestingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_order', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trf_test', to='samples.testingparameter')),
                ('trf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trf_testing', to='trf.trf')),
            ],
        ),
    ]
