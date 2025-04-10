# Generated by Django 5.0.3 on 2024-04-23 01:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyReserveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2099)], verbose_name='年份')),
                ('province', models.CharField(choices=[('北京', '北京'), ('天津', '天津'), ('河北', '河北'), ('山西', '山西'), ('内蒙古', '内蒙古'), ('辽宁', '辽宁'), ('吉林', '吉林'), ('黑龙江', '黑龙江'), ('上海', '上海'), ('江苏', '江苏'), ('浙江', '浙江'), ('安徽', '安徽'), ('福建', '福建'), ('江西', '江西'), ('山东', '山东'), ('河南', '河南'), ('湖北', '湖北'), ('湖南', '湖南'), ('广东', '广东'), ('广西', '广西'), ('海南', '海南'), ('重庆', '重庆'), ('四川', '四川'), ('贵州', '贵州'), ('云南', '云南'), ('西藏', '西藏'), ('陕西', '陕西'), ('甘肃', '甘肃'), ('青海', '青海'), ('宁夏', '宁夏'), ('新疆', '新疆')], default='安徽', max_length=10, verbose_name='省份')),
                ('petroleum_pro', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（产量）', max_digits=10, verbose_name='石油')),
                ('natural_gas_pro', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（产量）', max_digits=10, verbose_name='天然气')),
                ('coal_pro', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（产量）', max_digits=10, verbose_name='煤炭')),
                ('nuclear_pro', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（产量）', max_digits=10, verbose_name='核能')),
                ('other_pro', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（产量）', max_digits=10, verbose_name='其他')),
                ('petroleum_res', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（储量）', max_digits=10, verbose_name='石油')),
                ('natural_gas_res', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（储量）', max_digits=10, verbose_name='天然气')),
                ('coal_res', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（储量）', max_digits=10, verbose_name='煤炭')),
                ('nuclear_res', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（储量）', max_digits=10, verbose_name='核能')),
                ('other_res', models.DecimalField(decimal_places=2, default=1.0, help_text='亿千瓦时（储量）', max_digits=10, verbose_name='其他')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '地区不可再生能源储量/产量统计',
            },
        ),
        migrations.CreateModel(
            name='ExtractionEfficiencyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2099)], verbose_name='年份')),
                ('province', models.CharField(choices=[('北京', '北京'), ('天津', '天津'), ('河北', '河北'), ('山西', '山西'), ('内蒙古', '内蒙古'), ('辽宁', '辽宁'), ('吉林', '吉林'), ('黑龙江', '黑龙江'), ('上海', '上海'), ('江苏', '江苏'), ('浙江', '浙江'), ('安徽', '安徽'), ('福建', '福建'), ('江西', '江西'), ('山东', '山东'), ('河南', '河南'), ('湖北', '湖北'), ('湖南', '湖南'), ('广东', '广东'), ('广西', '广西'), ('海南', '海南'), ('重庆', '重庆'), ('四川', '四川'), ('贵州', '贵州'), ('云南', '云南'), ('西藏', '西藏'), ('陕西', '陕西'), ('甘肃', '甘肃'), ('青海', '青海'), ('宁夏', '宁夏'), ('新疆', '新疆')], default='安徽', max_length=10, verbose_name='省份')),
                ('cost', models.DecimalField(decimal_places=2, default=1.0, help_text='亿元', max_digits=10, verbose_name='开采耗费')),
                ('get', models.DecimalField(decimal_places=2, default=1.0, help_text='亿吨', max_digits=10, verbose_name='获取能源')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '地区不可再生能源开采效率',
            },
        ),
        migrations.CreateModel(
            name='MarketInvestmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2000, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2099)], verbose_name='年份')),
                ('province', models.CharField(choices=[('北京', '北京'), ('天津', '天津'), ('河北', '河北'), ('山西', '山西'), ('内蒙古', '内蒙古'), ('辽宁', '辽宁'), ('吉林', '吉林'), ('黑龙江', '黑龙江'), ('上海', '上海'), ('江苏', '江苏'), ('浙江', '浙江'), ('安徽', '安徽'), ('福建', '福建'), ('江西', '江西'), ('山东', '山东'), ('河南', '河南'), ('湖北', '湖北'), ('湖南', '湖南'), ('广东', '广东'), ('广西', '广西'), ('海南', '海南'), ('重庆', '重庆'), ('四川', '四川'), ('贵州', '贵州'), ('云南', '云南'), ('西藏', '西藏'), ('陕西', '陕西'), ('甘肃', '甘肃'), ('青海', '青海'), ('宁夏', '宁夏'), ('新疆', '新疆')], default='安徽', max_length=20, verbose_name='省份')),
                ('natural_gas', models.DecimalField(decimal_places=2, default=1.0, help_text='亿立方米', max_digits=10, verbose_name='天然气累计消费量')),
                ('coal', models.DecimalField(decimal_places=2, default=1.0, help_text='千万吨', max_digits=10, verbose_name='原煤产量')),
                ('coal_methane', models.DecimalField(decimal_places=2, default=1.0, help_text='亿立方米', max_digits=10, verbose_name='煤层气产量')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '地区市场交易及投资建设',
            },
        ),
    ]
