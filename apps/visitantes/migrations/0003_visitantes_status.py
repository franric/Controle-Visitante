# Generated by Django 3.0 on 2021-04-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_auto_20210409_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitantes',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'Visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]