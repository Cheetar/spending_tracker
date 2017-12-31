# Generated by Django 2.0 on 2017-12-30 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20171230_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='board',
        ),
        migrations.AlterField(
            model_name='spending',
            name='category',
            field=models.CharField(choices=[('Home', 'Home'), ('Groceries', 'Groceries'), ('Gifts', 'Gifts'), ('Kids', 'Kids'), ('Fuel', 'Fuel'), ('Transport', 'Transport'), ('Eating out', 'Eating out'), ('Other', 'Other')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]