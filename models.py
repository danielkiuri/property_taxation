# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MpesaMpesacallbacks(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'mpesa_mpesacallbacks'


class MpesaMpesacalls(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'mpesa_mpesacalls'


class MpesaMpesapayment(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'mpesa_mpesapayment'


class ParcelInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    plot_no = models.IntegerField(blank=True, null=True)
    owner = models.CharField(max_length=-1, blank=True, null=True)
    arrears = models.IntegerField(blank=True, null=True)
    id_number = models.IntegerField(blank=True, null=True)
    is_cleared = models.BooleanField(blank=True, null=True)
    phone_number = models.CharField(db_column='phone number', max_length=10)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'parcel_info'


class Parcels(models.Model):
    id = models.DecimalField(max_digits=65535, decimal_places=65535)
    geom = models.MultiPolygonField(srid=3857, blank=True, null=True)
    plot_no = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    owner = models.CharField(max_length=50, blank=True, null=True)
    zone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcels'


class PropertyTaxationhistory(models.Model):
    plot_no = models.BigIntegerField(blank=True, null=True)
    payed_on = models.DateTimeField()
    is_waived = models.BooleanField()
    payment_mode = models.CharField(max_length=50)
    amount = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField()
    transaction_id = models.CharField(max_length=50)
    id_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'property_taxationhistory'


class UserUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    id_number = models.BigIntegerField(unique=True)
    is_taxpayer = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user', 'group'),)


class UserUserUserPermissions(models.Model):
    user = models.ForeignKey(UserUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UserUserprofile(models.Model):
    image = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    user = models.OneToOneField(UserUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_userprofile'
