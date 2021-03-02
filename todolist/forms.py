from django import forms

class TodoListForm (forms.Form):
    text = forms.CharField (max_length = 45,
    widget = forms.TextInput (
    attrs = {'class': 'input-text', 'placeholder': 'FORM Enter todo in e.g. Grocery Shopping'}))


#from index.html
#<input type=text" class="input-text" placeholder="Enter todo e.g. Wash my car">	