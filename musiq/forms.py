from django import forms

QUESTION1_CHOICES = [
    ('q1_op1','Its great to be alive'),
    ('q1_op2','Today I swear Im not doing anything'),
    ('q1_op3','Im over this'),
    ('q1_op4','I cant wait to see them'),
]




class CHOICES(forms.Form):
    question1_phrase = forms.CharField(widget = forms.RadioSelect(choices=QUESTION1_CHOICES))