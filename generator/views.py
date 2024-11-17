from django.shortcuts import render

# Create your views here.
# generator/views.py
import string
import secrets
from django.shortcuts import render
from .forms import PasswordForm

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    # Define the basic character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Start with the lowercase letters (always included)
    characters = lowercase_letters

    # Add optional character sets based on user input
    if include_uppercase:
        characters += uppercase_letters
    if include_numbers:
        characters += digits
    if include_symbols:
        characters += symbols

    # Generate a random password
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    return password

def password_generator(request):
    password = ""
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            include_uppercase = form.cleaned_data['include_uppercase']
            include_numbers = form.cleaned_data['include_numbers']
            include_symbols = form.cleaned_data['include_symbols']
            
            # Generate password based on criteria
            password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    else:
        form = PasswordForm()

    return render(request, 'password_generator.html', {'form': form, 'password': password})
