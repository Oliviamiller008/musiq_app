from django import forms

QUESTION1_CHOICES = [
    ('q1op1','Its great to be alive'),
    ('q1op2','Today I swear Im not doing anything'),
    ('q1op3','Im over this'),
    ('q1op4','I cant wait to see my friends'),
]


class CHOICES(forms.Form):
    question1_phrase = forms.CharField(widget = forms.RadioSelect(choices=QUESTION1_CHOICES))

class OPTIONS(forms.Form):
    question1 = forms.MultipleChoiceField(
        required = True,
        widget = forms.RadioSelect,
        choices=QUESTION1_CHOICES,
    )
