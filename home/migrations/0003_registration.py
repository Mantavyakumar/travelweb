# Generated by Django 5.1.7 on 2025-04-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('departure_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('destination', models.CharField(choices=[('Kashmir', 'Kashmir'), ('Istanbul', 'Istanbul'), ('Paris', 'Paris'), ('Bali', 'Bali'), ('Dubai', 'Dubai'), ('Geneva', 'Geneva'), ('Port Blair', 'Port Blair'), ('Rome', 'Rome')], max_length=100)),
                ('package', models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=8)),
                ('tnc', models.BooleanField(default=False)),
            ],
        ),
    ]
