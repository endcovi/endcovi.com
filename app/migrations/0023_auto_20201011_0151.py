# Generated by Django 3.1.2 on 2020-10-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20201011_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubeclip',
            name='mention_status',
            field=models.IntegerField(choices=[(0, 'Chưa kiểm tra'), (1, 'Trên tiêu đề'), (2, 'Trên nội dung')], default=0, verbose_name='Trạng thái Đề cập'),
        ),
        migrations.AddField(
            model_name='youtubeclip',
            name='mentions',
            field=models.ManyToManyField(to='app.VIP', verbose_name='Đề cập tới'),
        ),
        migrations.AlterField(
            model_name='youtubeclip',
            name='bad_content_status',
            field=models.IntegerField(choices=[(0, 'Chưa kiểm tra'), (1, 'Đã bóc băng'), (2, 'Kiểm tra đề cập lãnh đạo'), (3, 'Phân tích nội dung'), (4, 'Bình thường'), (5, 'Cần kiểm tra'), (6, 'Xấu độc')], default=0, verbose_name='Trạng thái Xấu độc'),
        ),
        migrations.AlterField(
            model_name='youtubeclip',
            name='live_status',
            field=models.IntegerField(choices=[(0, 'Chưa kiểm tra'), (1, 'Đang kiểm tra'), (2, 'Die-YT'), (3, 'Gov-YT'), (4, 'Live-YT'), (5, 'Bad Link')], default=0, verbose_name='Trạng thái Live'),
        ),
    ]