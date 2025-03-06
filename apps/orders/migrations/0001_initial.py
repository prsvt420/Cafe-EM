# Generated by Django 5.1.6 on 2025-03-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dishes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "table_number",
                    models.PositiveSmallIntegerField(verbose_name="Номер столика"),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Общая стоимость",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PG", "В ожидании"),
                            ("RD", "Готово"),
                            ("PD", "Оплачено"),
                        ],
                        default="PG",
                        max_length=2,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "dishes",
                    models.ManyToManyField(to="dishes.dish", verbose_name="Блюда"),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "db_table": "orders",
                "db_table_comment": "Таблица содержит список заказов",
                "ordering": ("id",),
            },
        ),
    ]
