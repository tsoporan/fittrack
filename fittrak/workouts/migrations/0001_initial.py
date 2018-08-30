# Generated by Django 2.0.4 on 2018-05-06 23:18

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
            name='Exercise',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_started', models.DateTimeField(blank=True, null=True)),
                ('date_ended', models.DateTimeField(blank=True, null=True)),
                ('slug',
                 models.CharField(
                     blank=True,
                     help_text='A human easy to read/share name for exercise',
                     max_length=15,
                     null=True,
                     unique=True)),
            ],
            options={
                'ordering': ('-id', ),
            },
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('user',
                 models.ForeignKey(
                     blank=True,
                     null=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_started', models.DateTimeField(blank=True, null=True)),
                ('date_ended', models.DateTimeField(blank=True, null=True)),
                ('repetitions', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('unit',
                 models.CharField(
                     choices=[('KG', 'Kilograms'), ('LB', 'Pounds')],
                     max_length=32)),
                ('exercise',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='sets',
                     to='workouts.Exercise')),
            ],
            options={
                'ordering': ('-id', ),
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_started', models.DateTimeField(blank=True, null=True)),
                ('date_ended', models.DateTimeField(blank=True, null=True)),
                ('slug',
                 models.CharField(
                     blank=True,
                     help_text='A human easy to read/share name for workout',
                     max_length=15,
                     null=True,
                     unique=True)),
            ],
            options={
                'ordering': ('-id', ),
            },
        ),
        migrations.CreateModel(
            name='WorkoutStatus',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='workout',
            name='status',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='workouts.WorkoutStatus'),
        ),
        migrations.AddField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='workouts.ExerciseType'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='exercises',
                to='workouts.Workout'),
        ),
    ]
