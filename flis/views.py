from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from flis import models, auth, forms


PER_PAGE = 25


class Interlinks(ListView):

    model = models.Interlink
    template_name = 'interlinks/interlinks.html'
    paginate_by = PER_PAGE


class Interlink(DetailView):

    model = models.Interlink
    template_name = 'interlinks/interlink.html'
    paginate_by = PER_PAGE


class InterlinkCreate(CreateView):

    model = models.Interlink
    template_name = 'interlinks/interlink_edit.html'
    form_class = forms.InterlinkForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(InterlinkCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('interlinks', kwargs={'country': country})
        return context


class InterlinkEdit(UpdateView):

    model = models.Interlink
    template_name = 'interlinks/interlink_edit.html'
    form_class = forms.InterlinkForm

    def get_context_data(self, *args, **kwargs):
        context = super(InterlinkEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class InterlinkDelete(DeleteView):

    model = models.Interlink

    def get_success_url(self):
        country = self.request.country
        return reverse('interlinks', kwargs={'country': country})


class Sources(ListView):

    model = models.Source
    template_name = 'sources/sources.html'
    paginate_by = PER_PAGE


class Source(DetailView):

    model = models.Source
    template_name = 'sources/source.html'


class SourceCreate(CreateView):

    template_name = 'sources/source_edit.html'
    model = models.Source
    form_class = forms.SourceForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(SourceCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('sources', kwargs={'country': country})
        return context


class SourceEdit(UpdateView):

    template_name = 'sources/source_edit.html'
    model = models.Source
    form_class = forms.SourceForm

    def get_context_data(self, *args, **kwargs):
        context = super(SourceEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SourceDelete(DeleteView):

    model = models.Source

    def get_success_url(self):
        country = self.request.country
        return reverse('sources', kwargs={'country': country})


class GMTs(ListView):

    model = models.GMT
    template_name = 'gmt/gmts.html'
    paginate_by = PER_PAGE


class GMT(DetailView):

    model = models.GMT
    template_name = 'gmt/gmt.html'


class GMTCreate(CreateView):

    model = models.GMT
    template_name = 'gmt/gmt_edit.html'
    form_class = forms.GMTForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(GMTCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('gmts', kwargs={'country': country})
        return context


class GMTEdit(UpdateView):

    model = models.GMT
    template_name = 'gmt/gmt_edit.html'
    form_class = forms.GMTForm

    def get_context_data(self, *args, **kwargs):
        context = super(GMTEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GMTDelete(DeleteView):

    model = models.GMT

    def get_success_url(self):
        country = self.request.country
        return reverse('gmts', kwargs={'country': country})


class Indicators(ListView):

    model = models.Indicator
    template_name = 'indicators/indicators.html'


class Indicator(DetailView):

    model = models.Indicator
    template_name = 'indicators/indicator.html'


class IndicatorCreate(CreateView):

    model = models.Indicator
    template_name = 'indicators/indicator_edit.html'
    form_class = forms.IndicatorForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(IndicatorCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('indicators', kwargs={'country': country})
        return context


class IndicatorEdit(UpdateView):

    model = models.Indicator
    template_name = 'indicators/indicator_edit.html'
    form_class = forms.IndicatorForm

    def get_context_data(self, *args, **kwargs):
        context = super(IndicatorEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class IndicatorDelete(DeleteView):

    model = models.Indicator

    def get_success_url(self):
        country = self.request.country
        return reverse('indicators', kwargs={'country': country})


class Trends(ListView):

    model = models.Trend
    template_name = 'trends/trends.html'
    paginate_by = PER_PAGE


class Trend(DetailView):

    model = models.Trend
    template_name = 'trends/trend.html'


class TrendCreate(CreateView):

    model = models.Trend
    template_name = 'trends/trend_edit.html'
    form_class = forms.TrendForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(TrendCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('trends', kwargs={'country': country})
        return context


class TrendEdit(UpdateView):

    model = models.Trend
    template_name = 'trends/trend_edit.html'
    form_class = forms.TrendForm

    def get_context_data(self, *args, **kwargs):
        context = super(TrendEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TrendDelete(DeleteView):

    model = models.Trend

    def get_success_url(self):
        country = self.request.country
        return reverse('trends', kwargs={'country': country})


class ThematicCategories(ListView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_categories.html'


class ThematicCategory(DetailView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category.html'

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(ThematicCategory, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('trends', kwargs={'country': country})
        return context


class ThematicCategoryCreate(CreateView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category_edit.html'
    form_class = forms.ThematicCategoryForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(ThematicCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('thematic_categories', kwargs={'country': country})
        return context


class ThematicCategoryEdit(UpdateView):

    model = models.ThematicCategory
    template_name = 'thematic_categories/thematic_category_edit.html'
    form_class = forms.ThematicCategoryForm

    def get_context_data(self, *args, **kwargs):
        context = super(ThematicCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class ThematicCategoryDelete(DeleteView):

    model = models.ThematicCategory

    def get_success_url(self):
        country = self.request.country
        return reverse('thematic_categories', kwargs={'country': country})


class GeographicalScales(ListView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scales.html'


class GeographicalScale(DetailView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale.html'


class GeographicalScaleCreate(CreateView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale_edit.html'
    form_class = forms.GeographicalScaleForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(GeographicalScaleCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('geographical_scales', kwargs={'country': country})
        return context


class GeographicalScaleEdit(UpdateView):

    model = models.GeographicalScale
    template_name = 'geographical_scales/geographical_scale_edit.html'
    form_class = forms.GeographicalScaleForm

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalScaleEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalScaleDelete(DeleteView):

    model = models.GeographicalScale

    def get_success_url(self):
        country = self.request.country
        return reverse('geographical_scales', kwargs={'country': country})


class GeographicalCoverages(ListView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverages.html'


class GeographicalCoverage(DetailView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage.html'


class GeographicalCoverageCreate(CreateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage_edit.html'
    form_class = forms.GeographicalCoverageForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(GeographicalCoverageCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('geographical_coverages', kwargs={'country': country})
        return context


class GeographicalCoverageEdit(UpdateView):

    model = models.GeographicalCoverage
    template_name = 'geographical_coverages/geographical_coverage_edit.html'
    form_class = forms.GeographicalCoverageForm

    def get_context_data(self, *args, **kwargs):
        context = super(GeographicalCoverageEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class GeographicalCoverageDelete(DeleteView):

    model = models.GeographicalCoverage

    def get_success_url(self):
        country = self.request.country
        return reverse('geographical_coverages', kwargs={'country': country})


class SteepCategories(ListView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_categories.html'


class SteepCategory(DetailView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category.html'


class SteepCategoryCreate(CreateView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category_edit.html'
    form_class = forms.SteepCategoryForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(SteepCategoryCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('steep_categories', kwargs={'country': country})
        return context


class SteepCategoryEdit(UpdateView):

    model = models.SteepCategory
    template_name = 'steep_categories/steep_category_edit.html'
    form_class = forms.SteepCategoryForm

    def get_context_data(self, *args, **kwargs):
        context = super(SteepCategoryEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class SteepCategoryDelete(DeleteView):

    model = models.SteepCategory

    def get_success_url(self):
        country = self.request.country
        return reverse('steep_categories', kwargs={'country': country})


class Timelines(ListView):

    model = models.Timeline
    template_name = 'timelines/timelines.html'


class Timeline(DetailView):

    model = models.Timeline
    template_name = 'timelines/timeline.html'


class TimelineCreate(CreateView):

    model = models.Timeline
    template_name = 'timelines/timeline_edit.html'
    form_class = forms.TimelineCreateForm

    def get_context_data(self, *args, **kwargs):
        country = self.request.country
        context = super(TimelineCreate, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = reverse('timelines', kwargs={'country': country})
        return context


class TimelineEdit(UpdateView):

    model = models.Timeline
    template_name = 'timelines/timeline_edit.html'
    form_class = forms.TimelineCreateForm

    def get_context_data(self, *args, **kwargs):
        context = super(TimelineEdit, self).get_context_data(*args, **kwargs)
        context['cancel_url'] = context['object'].get_absolute_url()
        return context


class TimelineDelete(DeleteView):

    model = models.Timeline
    def get_success_url(self):
        country = self.request.country
        return reverse('timelines', kwargs={'country': country})
