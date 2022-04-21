# Generated by Django 4.0.4 on 2022-04-21 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField()),
                ('time_changed', models.DateTimeField()),
                ('name', models.CharField(max_length=150)),
                ('group', models.CharField(max_length=50)),
                ('member_gz_2021_2022', models.CharField(max_length=10, null=True)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=20)),
                ('living', models.CharField(max_length=50)),
                ('children', models.CharField(max_length=20)),
                ('work_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_reader.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csv_reader.user')),
            ],
        ),
    ]
