# Generated by Django 3.2.7 on 2021-09-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicine', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('medicine_details', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.bill')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]