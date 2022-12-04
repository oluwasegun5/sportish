# Generated by Django 4.1.3 on 2022-11-30 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_name', models.CharField(max_length=255)),
                ('minutes', models.SmallIntegerField()),
                ('venue', models.CharField(max_length=255)),
                ('competition_info', models.TextField()),
                ('competition_logo', models.ImageField(upload_to='sport_app/images')),
                ('date_created', models.DateField(auto_now=True)),
                ('organization', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=255, null=True)),
                ('profile_picture', models.ImageField(upload_to='sport_app/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('teamName', models.CharField(max_length=255)),
                ('teamLogo', models.ImageField(upload_to='sport_app/images')),
                ('organization', models.CharField(max_length=255, null=True)),
                ('competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='football.competition')),
                ('manager', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='football.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('COA', 'Coach'), ('GK', 'Goal-Keeper'), ('DF', 'Defender'), ('MF', 'Midfielder'), ('FWD', 'Forward')], max_length=11)),
                ('strong_foot', models.CharField(choices=[('RGT', 'Right'), ('LFT', 'Left'), ('BTH', 'Both')], max_length=5, null=True)),
                ('country', models.CharField(default='Nigeria', max_length=255)),
                ('organization', models.CharField(max_length=255, null=True)),
                ('picture', models.ImageField(upload_to='sport_app/images')),
                ('height', models.DecimalField(decimal_places=1, max_digits=3)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='football.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('profile_picture', models.ImageField(upload_to='sport_app/images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='football.host'),
        ),
    ]
