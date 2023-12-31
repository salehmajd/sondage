# Generated by Django 4.2.6 on 2023-10-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sondage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choix_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondage.question')),
            ],
        ),
    ]
