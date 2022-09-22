from django import forms
from .models import Publisher, Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("contributor", "Contributor")
                                  ))
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Search"))

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ("book", "date_edited")

    rating = forms.IntegerField(min_value=0, max_value=5)

class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["cover", "sample"]
