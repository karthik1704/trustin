# Generated by Django 4.2.7 on 2024-01-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.myuser',),
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_analyst',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_hod',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_management',
        ),
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('HOD', 'HOD'), ('MARKETING', 'Marketing'), ('ADMIN', 'Admin'), ('MANAGEMENT', 'Management'), ('ANALYST', 'Analyst')], default='ADMIN', verbose_name='Role'),
        ),
    ]