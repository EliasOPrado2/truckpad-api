# Generated by Django 3.2.13 on 2022-09-06 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=512)),
                ("neighborhood", models.CharField(blank=True, max_length=256)),
                ("city", models.CharField(blank=True, max_length=256)),
                ("state", models.CharField(blank=True, max_length=120)),
                ("postcode", models.CharField(blank=True, max_length=10)),
                ("country", models.CharField(blank=True, max_length=30)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=16, max_digits=22, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=16, max_digits=22, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DestinationCoordinate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=512)),
                ("neighborhood", models.CharField(blank=True, max_length=256)),
                ("city", models.CharField(blank=True, max_length=256)),
                ("state", models.CharField(blank=True, max_length=120)),
                ("postcode", models.CharField(blank=True, max_length=10)),
                ("country", models.CharField(blank=True, max_length=30)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=16, max_digits=22, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=16, max_digits=22, null=True
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TruckDriver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("age", models.IntegerField()),
                (
                    "sex",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "MALE"),
                            (1, "FEMALE"),
                            (2, "TRANSGENDER"),
                            (3, "NO ANSWER"),
                        ],
                        null=True,
                    ),
                ),
                ("has_truck", models.BooleanField(default=False)),
                (
                    "cnh_type",
                    models.IntegerField(choices=[("1", "C"), ("2", "D"), ("3", "E")]),
                ),
                ("is_loaded", models.BooleanField(default=False)),
                (
                    "truck_type",
                    models.IntegerField(
                        choices=[
                            (1, "CARGO 3/4"),
                            (2, "TOCO"),
                            (3, "TRUCK"),
                            (4, "SIMPLE"),
                            (5, "EXTENDED AXLE"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Route",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("distance", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "destination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="destination",
                        to="core.address",
                    ),
                ),
                (
                    "origin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="origin",
                        to="core.address",
                    ),
                ),
                (
                    "truck_driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.truckdriver",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OriginCoordinate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=512)),
                ("neighborhood", models.CharField(blank=True, max_length=256)),
                ("city", models.CharField(blank=True, max_length=256)),
                ("state", models.CharField(blank=True, max_length=120)),
                ("postcode", models.CharField(blank=True, max_length=10)),
                ("country", models.CharField(blank=True, max_length=30)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=16, max_digits=22, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=16, max_digits=22, null=True
                    ),
                ),
                (
                    "destination",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.destinationcoordinate",
                    ),
                ),
                (
                    "truck_driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.truckdriver",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="destinationcoordinate",
            name="origin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="core.origincoordinate",
            ),
        ),
        migrations.AddField(
            model_name="destinationcoordinate",
            name="truck_driver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="core.truckdriver"
            ),
        ),
    ]
