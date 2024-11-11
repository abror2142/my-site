# Generated by Django 5.1.2 on 2024-11-11 07:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productcoloroption_productimage_color_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_character_name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('code', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMemory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
                ('roman_label', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='color_option',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='added_at',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='produced_at',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='produced_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimage',
            name='alt_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='CompanyBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.company')),
            ],
            options={
                'verbose_name_plural': 'BrandCompany',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.companybrand'),
        ),
        migrations.CreateModel(
            name='CustomCharacterOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=150)),
                ('custom_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.customcharacter')),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productcolor'),
        ),
        migrations.CreateModel(
            name='ProductImageSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('product_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productimage')),
            ],
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productimageset'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productmemory'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productsize'),
        ),
        migrations.CreateModel(
            name='ProductVariantCustomCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.customcharacter')),
                ('product_variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.productvariant')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductColorOption',
        ),
    ]
