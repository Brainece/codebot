#from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render
import openai;

# Create your views here.

def home(request):
     #API_KEY = "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"

    lang_list = ['c','clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java','python']

    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        # check to make sure they picked a lang
        if lang == "Select Programming Language":
            messages.success(request, "Hey! you forgot to pick a programming language")

            return render(request, 'home.html', {'lang_list':lang_list, 'code': code, 'lang':lang })

        else:
            # return render(request, 'home.html', {'lang_list':lang_list, 'code': code, 'lang':lang })

            # OpenAI !!!
            openai.api_key = "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"
            # Create OpenAI instance
            openai.Model.list()
            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-002',
                    prompt = f"Respond only with code. Fix this {lang} code: {code}",
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0,
                )

                # Parse the response
                response = (response["choices"][0]["text"]).strip()

                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
            
            except Exception as e:     
                return render(request, 'home.html', {'lang_list': lang_list, 'code': e, 'lang': lang})   

    return render(request, 'home.html', {'lang_list': lang_list})





def suggest(request):

    lang_list = ['c','clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java','python']

    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        # check to make sure they picked a lang
        if lang == "Select Programming Language":
            messages.success(request, "Hey! you forgot to pick a programming language")

            return render(request, 'suggest.html', {'lang_list':lang_list, 'code': code, 'lang':lang })

        else:
            # return render(request, 'home.html', {'lang_list':lang_list, 'code': code, 'lang':lang })

            # OpenAI !!!
            openai.api_key = "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"
            # Create OpenAI instance
            openai.Model.list()
            # Make an OpenAI Request
            try:
                response = openai.Completion.create(
                    engine = 'text-davinci-002',
                    prompt = f"Respond only with code. {code}",
                    temperature = 0,
                    max_tokens = 1000,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0,
                )

                # Parse the response
                response = (response["choices"][0]["text"]).strip()

                return render(request, 'suggest.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
            
            except Exception as e:     
                return render(request, 'suggest.html', {'lang_list': lang_list, 'code': e, 'lang': lang})   

    return render(request, 'suggest.html', {'lang_list': lang_list})


    



    
