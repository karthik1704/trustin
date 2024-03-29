# Generated by Django 4.2.7 on 2024-01-01 14:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notes', '0001_initial'),
        ('customers', '0001_initial'),
        ('samples', '0001_initial'),
        ('terms', '0001_initial'),
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_type', models.CharField(choices=[('SINGLE', 'Single Page'), ('DOUBLE', 'Double Page')], default='SINGLE', max_length=50)),
                ('quotation_id', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('sample_name', models.CharField(max_length=255)),
                ('required_quantity', models.CharField(max_length=255)),
                ('turn_around_time', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(default='')),
                ('charges_per', models.CharField(choices=[('BATCH', 'Batch'), ('SIZE', 'Size')], max_length=50)),
                ('no_of_test', models.PositiveIntegerField()),
                ('total_amount', models.DecimalField(decimal_places=4, max_digits=19)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('discount_amount', models.DecimalField(decimal_places=4, max_digits=19)),
                ('total_amount_before_tax', models.DecimalField(decimal_places=4, max_digits=19)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_branch', to='branches.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotation_customer', to='customers.customer')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='quotation_note', to='notes.note')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='quotation_product', to='samples.product')),
                ('terms_and_condition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='quotation_terms', to='terms.termsandcondition')),
            ],
        ),
    ]
