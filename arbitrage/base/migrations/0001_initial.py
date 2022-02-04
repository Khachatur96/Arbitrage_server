# Generated by Django 4.0.1 on 2022-02-03 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('decimals', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('abi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_pair', models.CharField(max_length=255)),
                ('price_difference', models.CharField(max_length=255)),
                ('dex_pair', models.CharField(max_length=255)),
                ('percentage', models.FloatField()),
                ('date', models.TextField(blank=True, null=True)),
                ('dexes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DexPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dex_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dex_1', to='base.dex')),
                ('dex_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dex_2', to='base.dex')),
            ],
        ),
        migrations.CreateModel(
            name='CoinPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coin_1', to='base.coin')),
                ('coin_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coin_2', to='base.coin')),
            ],
        ),
    ]
