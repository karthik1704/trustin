# Generated by Django 4.2.7 on 2024-01-01 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternate_address', models.TextField(blank=True, default='')),
                ('mfg_license_number', models.CharField(blank=True, max_length=100, null=True)),
                ('po_or_ref_number', models.CharField(blank=True, max_length=100, null=True)),
                ('quotation_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sample_name', models.CharField(max_length=255)),
                ('sample_name2', models.CharField(blank=True, max_length=255, null=True)),
                ('sample_description', models.TextField(blank=True, default='')),
                ('batch_or_lot_number', models.DecimalField(decimal_places=3, max_digits=4)),
                ('batch_size', models.PositiveIntegerField(blank=True, null=True)),
                ('sterilization_batch_number', models.BigIntegerField(blank=True, null=True)),
                ('sample_quantity_sent', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_mfg', models.DateField()),
                ('date_of_exp', models.DateField()),
                ('sample_manufactured_by', models.CharField(max_length=255)),
                ('sample_storage_condition', models.CharField(blank=True, max_length=255, null=True)),
                ('sampling_by', models.CharField(choices=[('CUSTOMER', 'Customer'), ('LABORATORY', 'Laboratory')], max_length=50)),
                ('testing_process', models.CharField(choices=[('BATCH_ANALYSIS', 'Batch Analysis'), ('METHOD_DEVELOPMENT', 'Method Development'), ('METHOD_VALIDATION', 'Method Validation'), ('RD_RESEARCH', 'R&D / Research'), ('REGULATORY', 'Regulatory')], max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='requester', to='customers.customer')),
            ],
        ),
    ]
