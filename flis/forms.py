
from django import forms
from django_tools.middlewares import ThreadLocal
from flis import models


class CleanCountry(object):

    def clean_country(self):
        data = self.cleaned_data['country']
        request = ThreadLocal.get_current_request()
        if not request.country == data:
            raise forms.ValidationError('Country not valid')
        return data


class InterlinkForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Interlink


class SourceForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Source


class GMTForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.GMT


class FlisModelForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.FlisModel


class HorizonScanningForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.HorizonScanning


class MethodToolForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.MethodTool


class UncertaintyForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Uncertainty


class WildCardForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.WildCard


class EarlyWarningForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.EarlyWarning


class IndicatorForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Indicator


class TrendForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Trend


class ThematicCategoryForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.ThematicCategory


class GeographicalScaleForm(CleanCountry, forms.ModelForm):

   class Meta:
        model = models.GeographicalScale


class GeographicalCoverageForm(CleanCountry, forms.ModelForm):

   class Meta:
        model = models.GeographicalCoverage


class SteepCategoryForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.SteepCategory


class TimelineCreateForm(CleanCountry, forms.ModelForm):

    class Meta:
        model = models.Timeline
