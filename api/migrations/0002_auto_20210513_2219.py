# Generated by Django 3.2 on 2021-05-13 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='pk_profileid',
            new_name='profile_id',
        ),
        migrations.RenameField(
            model_name='userlogs',
            old_name='fk_userid',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='userlogs',
            old_name='pk_user_logid',
            new_name='user_log_id',
        ),
    ]
