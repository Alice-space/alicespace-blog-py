# Generated by Django 2.2.6 on 2019-11-05 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=150, verbose_name='标题')),
                ('article_content', models.TextField(verbose_name='正文')),
                ('article_auth', models.CharField(max_length=20, verbose_name='作者')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('article_picurl', models.CharField(max_length=1500, verbose_name='标题图片')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('article_column', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.ArticleColumn')),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
    ]