from django.db import models
from django.conf import settings
from django.utils.encoding import smart_unicode
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
from path import path
from flis import markup


class BaseModel():

    def as_table(self):

        source = None

        page = markup.page()
        page.table(class_='table table-bordered table-condensed')
        page.tbody()

        for field in self._meta.fields:
            if field.name == 'id':
                continue
            field_name = field.verbose_name
            field_id = field.name
            field_value = getattr(self, field.name, None)

            page.tr()
            page.th(field_name, class_='span2')

            if field_name == 'Source':
                source = field_value

            if field_id == 'file_id' and field_value:
                page.td('<a href="{host}{url}">{name}</a>'.format(
                  host=settings.HOSTNAME, url=field_value.url,
                  name=path(field_value.name).basename()))
                continue

            if not isinstance(field_value, basestring):
                page.td(str(field_value))
            else:
                page.td(field_value.encode('utf-8'))

            page.tr.close()

        if source:
           page.tr()
           page.th('URL', class_='span2')
           page.td(page.td('<a href="{url}">{url}</a>'.format(url=source.url)))
           page.tr.close()

        page.tbody.close()
        page.table.close()
        return mark_safe(page)


class Country(models.Model):

  iso = models.CharField(max_length=128, primary_key=True)
  name = models.CharField(max_length=256)

  def __unicode__(self):
    return self.iso


class Source(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    short_name = models.CharField(max_length=512, verbose_name='Short name')
    long_name = models.CharField(max_length=512, verbose_name='Long name')
    year_of_publication = models.CharField(max_length=512,
                                           verbose_name='Year of publication')
    author = models.CharField(max_length=512)
    url = models.URLField(max_length=512)
    summary = models.TextField(null=True, blank=True, default='')

    def __unicode__(self):
        return self.short_name

    def get_absolute_url(self):
        return reverse('source_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class Trend(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='trends',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('trend_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class ThematicCategory(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    description = models.CharField(max_length=512, verbose_name='Description')

    def __unicode__(self):
        return '%s (%s)' % (self.code, self.description)

    def get_absolute_url(self):
        return reverse('thematic_category_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class GeographicalScale(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    description = models.CharField(max_length=512, verbose_name='Description')

    def __unicode__(self):
        return '%s (%s)' % (self.code, self.description)

    def get_absolute_url(self):
        return reverse('geographical_scale_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class GeographicalCoverage(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    description = models.CharField(max_length=512, verbose_name='Description')

    def __unicode__(self):
        return '%s (%s)' % (self.code, self.description)

    def get_absolute_url(self):
        return reverse('geographical_coverage_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class SteepCategory(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    description = models.CharField(max_length=512, verbose_name='Description')

    def __unicode__(self):
        return '%s (%s)' % (self.code, self.description)

    def get_absolute_url(self):
        return reverse('steep_category_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class Timeline(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    title = models.CharField(max_length=512, verbose_name='Title')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('timeline_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class Indicator(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    description = models.CharField(max_length=512, verbose_name='Description')

    thematic_category = models.ForeignKey(ThematicCategory,
                                          related_name='Indicators',
                                          verbose_name='Thematic category',
                                          on_delete=models.PROTECT)
    geographical_scale = models.ForeignKey(GeographicalScale,
                                           related_name='Indicators',
                                           verbose_name='Geographical scale',
                                           null=True, blank=True,
                                           on_delete=models.PROTECT)
    geographical_coverage = models.ForeignKey(GeographicalCoverage,
                                            related_name='Indicators',
                                            verbose_name='Geographical coverage',
                                            null=True, blank=True,
                                            on_delete=models.PROTECT)
    timeline = models.ForeignKey(Timeline, related_name='timeline',
                                 verbose_name='Timeline',
                                 on_delete=models.PROTECT)
    source = models.ForeignKey(Source, related_name='sources_indicator',
                               verbose_name='Source',
                               on_delete=models.PROTECT)

    base_year = models.CharField(max_length=256, verbose_name='Base year')
    end_year = models.CharField(max_length=256, verbose_name='End year')
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('indicator_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


class GMT(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='gmts',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='gmts',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('gmt_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class FlisModel(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='flismodels',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='flismodels',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('flismodel_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class HorizonScanning(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='horizonscannings',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='horizonscannings',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('horizonscanning_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class MethodTool(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='methodstools',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='methodstools',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('methodtool_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class Uncertainty(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='uncertainties',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='uncertainties',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('uncertainty_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class WildCard(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='wildcards',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='wildcards',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('wildcard_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class EarlyWarning(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    code = models.CharField(max_length=256, verbose_name='Code')
    steep_category = models.ForeignKey(SteepCategory,
                                       related_name='earlywarnings',
                                       verbose_name='Steep Category',
                                       null=True, blank=True,
                                       on_delete=models.PROTECT)
    description = models.CharField(max_length=512, verbose_name='Description')
    source = models.ForeignKey(Source, related_name='earlywarnings',
                               verbose_name='Source',
                               on_delete=models.PROTECT)
    # url = models.URLField(max_length=512, verbose_name='URL')
    ownership = models.CharField(max_length=512, verbose_name='Ownership')
    summary = models.TextField(null=True, blank=True, default='',
                               verbose_name='Summary')
    file_id = models.FileField(upload_to='files', max_length=256,
                               null=True, blank=True, default='',
                               verbose_name='File')

    def __unicode__(self):
        return self.code

    def get_absolute_url(self):

      return reverse('earlywarning_view', kwargs={
        'pk': self.pk,
        'country': self.country
      })


class Interlink(models.Model, BaseModel):

    country = models.ForeignKey(Country)
    gmt = models.ForeignKey(GMT, related_name='interlinks', verbose_name='GMT')
    trend = models.ForeignKey(Trend, related_name='interlinks',
                              verbose_name='Trend',
                              on_delete=models.PROTECT)
    indicator_1 = models.ForeignKey(Indicator, related_name='interlinks_indicator_1',
                                    verbose_name='Indicator',
                                    on_delete=models.PROTECT)
    indicator_2 = models.ForeignKey(Indicator, related_name='interlinks_indicator_2',
                                    verbose_name='Indicator',
                                    null=True, blank=True,
                                    on_delete=models.PROTECT)
    indicator_3 = models.ForeignKey(Indicator, related_name='interlinks_indicator_3',
                                    verbose_name='Indicator',
                                    null=True, blank=True,
                                    on_delete=models.PROTECT)
    indicator_4 = models.ForeignKey(Indicator, related_name='interlinks_indicator_4',
                                    verbose_name='Indicator',
                                    null=True, blank=True,
                                    on_delete=models.PROTECT)

    def __unicode__(self):
        return self.gmt.code

    def get_absolute_url(self):
        return reverse('interlink_view', kwargs={
          'pk': self.pk,
          'country': self.country,
        })


