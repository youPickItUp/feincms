# Generated by Django 3.0.2 on 2020-01-21 15:21

import django.db.models.deletion
from django.db import migrations, models

import feincms.contrib.fields
import feincms.extensions.base
import feincms.extensions.datepublisher
import feincms.module.medialibrary.fields
import feincms.module.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sites", "0001_initial"),
        ("medialibrary", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("active", models.BooleanField(default=True, verbose_name="active")),
                (
                    "title",
                    models.CharField(
                        help_text="This title is also used for navigation menu items.",
                        max_length=200,
                        verbose_name="title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="This is used to build the URL for this page",
                        max_length=150,
                        verbose_name="slug",
                    ),
                ),
                (
                    "in_navigation",
                    models.BooleanField(default=False, verbose_name="in navigation"),
                ),
                (
                    "override_url",
                    models.CharField(
                        blank=True,
                        help_text="Override the target URL. Be sure to include slashes at the beginning and at the end if it is a local URL. This affects both the navigation and subpages' URLs.",
                        max_length=255,
                        verbose_name="override URL",
                    ),
                ),
                (
                    "redirect_to",
                    models.CharField(
                        blank=True,
                        help_text="Target URL for automatic redirects or the primary key of a page.",
                        max_length=255,
                        verbose_name="redirect to",
                    ),
                ),
                (
                    "_cached_url",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default="",
                        editable=False,
                        max_length=255,
                        verbose_name="Cached URL",
                    ),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "template_key",
                    models.CharField(
                        choices=[("base", "Base Template")],
                        default="base",
                        max_length=255,
                        verbose_name="template",
                    ),
                ),
                (
                    "navigation_extension",
                    models.CharField(
                        blank=True,
                        choices=[],
                        help_text="Select the module providing subpages for this page if you need to customize the navigation.",
                        max_length=200,
                        null=True,
                        verbose_name="navigation extension",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("de", "German")],
                        default="en",
                        max_length=10,
                        verbose_name="language",
                    ),
                ),
                (
                    "publication_date",
                    models.DateTimeField(
                        default=feincms.extensions.datepublisher.granular_now,
                        verbose_name="publication date",
                    ),
                ),
                (
                    "publication_end_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Leave empty if the entry should stay active forever.",
                        null=True,
                        verbose_name="publication end date",
                    ),
                ),
                (
                    "_ct_inventory",
                    feincms.contrib.fields.JSONField(
                        blank=True,
                        editable=False,
                        null=True,
                        verbose_name="content types",
                    ),
                ),
                (
                    "meta_keywords",
                    models.TextField(
                        blank=True,
                        help_text="Keywords are ignored by most search engines.",
                        verbose_name="meta keywords",
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        blank=True,
                        help_text="This text is displayed on the search results page. It is however not used for the SEO ranking. Text longer than 140 characters is truncated.",
                        verbose_name="meta description",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="creation date"
                    ),
                ),
                (
                    "modification_date",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="modification date"
                    ),
                ),
                (
                    "_content_title",
                    models.TextField(
                        blank=True,
                        help_text="The first line is the main title, the following lines are subtitles.",
                        verbose_name="content title",
                    ),
                ),
                (
                    "_page_title",
                    models.CharField(
                        blank=True,
                        help_text="Page title for browser window. Same as title by default. Must be 69 characters or fewer.",
                        max_length=69,
                        verbose_name="page title",
                    ),
                ),
                (
                    "navigation_group",
                    models.CharField(
                        blank=True,
                        choices=[("default", "Default"), ("footer", "Footer")],
                        db_index=True,
                        default="default",
                        max_length=20,
                        verbose_name="navigation group",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="page.Page",
                        verbose_name="Parent",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sites.Site",
                        verbose_name="Site",
                    ),
                ),
                (
                    "symlinked_page",
                    models.ForeignKey(
                        blank=True,
                        help_text="All content is inherited from this page if given.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="page_page_symlinks",
                        to="page.Page",
                        verbose_name="symlinked page",
                    ),
                ),
                (
                    "translation_of",
                    models.ForeignKey(
                        blank=True,
                        help_text="Leave this empty for entries in the primary language.",
                        limit_choices_to={"language": "en"},
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="page.Page",
                        verbose_name="translation of",
                    ),
                ),
            ],
            options={
                "verbose_name": "page",
                "verbose_name_plural": "pages",
                "ordering": ["tree_id", "lft"],
            },
            bases=(
                models.Model,
                feincms.extensions.base.ExtensionsMixin,
                feincms.module.mixins.ContentModelMixin,
            ),
        ),
        migrations.CreateModel(
            name="TemplateContent",
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
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0, verbose_name="ordering")),
                (
                    "template",
                    models.CharField(
                        choices=[("templatecontent_1.html", "template 1")],
                        max_length=100,
                        verbose_name="template",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="templatecontent_set",
                        to="page.Page",
                    ),
                ),
            ],
            options={
                "verbose_name": "template content",
                "verbose_name_plural": "template contents",
                "db_table": "page_page_templatecontent",
                "ordering": ["ordering"],
                "permissions": [],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RawContent",
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
                ("text", models.TextField(blank=True, verbose_name="content")),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0, verbose_name="ordering")),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rawcontent_set",
                        to="page.Page",
                    ),
                ),
            ],
            options={
                "verbose_name": "raw content",
                "verbose_name_plural": "raw contents",
                "db_table": "page_page_rawcontent",
                "ordering": ["ordering"],
                "permissions": [],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MediaFileContent",
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
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0, verbose_name="ordering")),
                (
                    "type",
                    models.CharField(
                        choices=[("default", "Default position")],
                        default="default",
                        max_length=20,
                        verbose_name="type",
                    ),
                ),
                (
                    "mediafile",
                    feincms.module.medialibrary.fields.MediaFileForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="medialibrary.MediaFile",
                        verbose_name="media file",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mediafilecontent_set",
                        to="page.Page",
                    ),
                ),
            ],
            options={
                "verbose_name": "media file",
                "verbose_name_plural": "media files",
                "db_table": "page_page_mediafilecontent",
                "ordering": ["ordering"],
                "permissions": [],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ApplicationContent",
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
                    "parameters",
                    feincms.contrib.fields.JSONField(editable=False, null=True),
                ),
                ("region", models.CharField(max_length=255)),
                ("ordering", models.IntegerField(default=0, verbose_name="ordering")),
                (
                    "urlconf_path",
                    models.CharField(
                        choices=[("whatever", "Test Urls")],
                        max_length=100,
                        verbose_name="application",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applicationcontent_set",
                        to="page.Page",
                    ),
                ),
            ],
            options={
                "verbose_name": "application content",
                "verbose_name_plural": "application contents",
                "db_table": "page_page_applicationcontent",
                "ordering": ["ordering"],
                "permissions": [],
                "abstract": False,
            },
        ),
    ]
