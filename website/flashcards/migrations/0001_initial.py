# Generated by Django 2.0.4 on 2018-04-21 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=25)),
                ('question', models.CharField(max_length=25)),
                ('answer1', models.CharField(blank=True, max_length=25)),
                ('answer2', models.CharField(blank=True, max_length=25)),
                ('answer3', models.CharField(blank=True, max_length=25)),
                ('answer4', models.CharField(blank=True, max_length=25)),
                ('answer5', models.CharField(blank=True, max_length=25)),
                ('answer_a', models.CharField(blank=True, max_length=25)),
                ('answer_b', models.CharField(blank=True, max_length=25)),
                ('answer_c', models.CharField(blank=True, max_length=25)),
                ('answer_d', models.CharField(blank=True, max_length=25)),
                ('keywords', models.CharField(blank=True, max_length=100)),
                ('word_type', models.CharField(blank=True, max_length=10)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('uploads', models.PositiveIntegerField(default=1)),
                ('views', models.PositiveIntegerField(default=0)),
                ('difficulty', models.PositiveSmallIntegerField(default=50)),
            ],
        ),
    ]