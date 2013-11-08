
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


class SourceForm(forms.ModelForm):

    class Meta:
        model = models.Source


class GMTForm(forms.ModelForm):

    class Meta:
        model = models.GMT


class FlisModelForm(forms.ModelForm):

    class Meta:
        model = models.FlisModel


class HorizonScanningForm(forms.ModelForm):

    class Meta:
        model = models.HorizonScanning


class MethodToolForm(forms.ModelForm):

    class Meta:
        model = models.MethodTool


class UncertaintyForm(forms.ModelForm):

    class Meta:
        model = models.Uncertainty


class WildCardForm(forms.ModelForm):

    class Meta:
        model = models.WildCard


class EarlyWarningForm(forms.ModelForm):

    class Meta:
        model = models.EarlyWarning


class IndicatorForm(forms.ModelForm):

    class Meta:
        model = models.Indicator


class TrendForm(forms.ModelForm):

    class Meta:
        model = models.Trend


class BlossomForm(forms.ModelForm):

    class Meta:
        model = models.Blossom

    def __init__(self, *args, **kwargs):
         super(BlossomForm, self).__init__(*args, **kwargs)
         self.fields['date_of_conclusion_planned'].input_formats = ['%d/%m/%Y']
         self.fields['date_of_conclusion_final'].input_formats = ['%d/%m/%Y']


class ThematicCategoryForm(forms.ModelForm):

    class Meta:
        model = models.ThematicCategory


class GeographicalScaleForm(forms.ModelForm):

   class Meta:
        model = models.GeographicalScale


class ScenarioForm(forms.ModelForm):

   class Meta:
        model = models.Scenario


class GeographicalCoverageForm(forms.ModelForm):

   class Meta:
        model = models.GeographicalCoverage


class SteepCategoryForm(forms.ModelForm):

    class Meta:
        model = models.SteepCategory


class TimelineCreateForm(forms.ModelForm):

    class Meta:
        model = models.Timeline
