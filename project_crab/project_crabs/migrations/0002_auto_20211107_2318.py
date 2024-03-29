# Generated by Django 3.2.8 on 2021-11-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_crabs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailharga',
            name='id_material',
        ),
        migrations.RemoveField(
            model_name='detailharga',
            name='id_supplier',
        ),
        migrations.RemoveField(
            model_name='detailharga',
            name='status_aktif',
        ),
        migrations.CreateModel(
            name='ProdukSupplier',
            fields=[
                ('id_produk_supplier', models.AutoField(db_column='ID_PRODUK_SUPPLIER', primary_key=True, serialize=False)),
                ('status_aktif', models.IntegerField(db_column='STATUS_AKTIF')),
                ('id_material', models.ForeignKey(blank=True, db_column='ID_MATERIAL', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project_crabs.material')),
                ('id_supplier', models.ForeignKey(blank=True, db_column='ID_SUPPLIER', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project_crabs.supplier')),
            ],
            options={
                'db_table': 'produk_supplier',
            },
        ),
        migrations.AddField(
            model_name='detailharga',
            name='id_produk_supplier',
            field=models.ForeignKey(blank=True, db_column='ID_PRODUK_SUPPLIER', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project_crabs.produksupplier'),
        ),
    ]
