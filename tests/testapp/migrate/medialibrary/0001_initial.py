# Generated by Django 3.0.2 on 2020-01-21 15:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import feincms.extensions.base
import feincms.translations


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="title")),
                ("slug", models.SlugField(max_length=150, verbose_name="slug")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"parent__isnull": True},
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="medialibrary.Category",
                        verbose_name="parent",
                    ),
                ),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ["parent__title", "title"],
            },
        ),
        migrations.CreateModel(
            name="MediaFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        max_length=255,
                        upload_to="medialibrary/%Y/%m/",
                        verbose_name="file",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("video", "Video"),
                            ("audio", "Audio"),
                            ("pdf", "PDF document"),
                            ("swf", "Flash"),
                            ("txt", "Text"),
                            ("rtf", "Rich Text"),
                            ("zip", "Zip archive"),
                            ("doc", "Microsoft Word"),
                            ("xls", "Microsoft Excel"),
                            ("ppt", "Microsoft PowerPoint"),
                            ("other", "Binary"),
                        ],
                        editable=False,
                        max_length=12,
                        verbose_name="file type",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "copyright",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="copyright"
                    ),
                ),
                (
                    "file_size",
                    models.IntegerField(
                        blank=True, editable=False, null=True, verbose_name="file size"
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        to="medialibrary.Category",
                        verbose_name="categories",
                    ),
                ),
            ],
            bases=(
                models.Model,
                feincms.extensions.base.ExtensionsMixin,
                feincms.translations.TranslatedObjectMixin,
            ),
        ),
        migrations.CreateModel(
            name="MediaFileTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        choices=[("en", "English"), ("de", "German")],
                        default="en",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                ("caption", models.CharField(max_length=1000, verbose_name="caption")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="medialibrary.MediaFile",
                    ),
                ),
            ],
            options={
                "verbose_name": "media file translation",
                "verbose_name_plural": "media file translations",
                "unique_together": {("parent", "language_code")},
            },
        ),
    ]
