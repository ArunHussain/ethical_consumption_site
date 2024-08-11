from django.shortcuts import render
from django.shortcuts import redirect
from functools import wraps
from django.http import HttpResponseRedirect
from users.models import CustomUser #so that we can quesry the custom user model
from .forms import survey_form, comment_form
from .models import survey_answers, company, comments
from datetime import datetime
import requests
import http.client, urllib.parse
import json

api_key = 'MifU57uXXScAQAmBjCrcFXjxa85HejKPjJeWKHXi'

# Create your views here.
def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('/error/')

#decorators for various views
def must_be_logged_in(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/error/')
    return wrap

#helper functions
def matches_func(company_name, query):
    return (company_name[:len(query)].upper() == query.upper())
    
def toMonth(num):
    match num:
        case 1:
           return "Jan"
        case 2:
            return "Feb"
        case 3:
           return "Mar"
        case 4:
           return "Apr"
        case 5:
           return "May"
        case 6:
           return "Jun"
        case 7:
           return "Jul"
        case 8:
           return "Aug"
        case 9:
           return "Sep"
        case 10:
           return "Oct"
        case 11:
           return "Nov"
        case 12:
           return "Dec"

    

# Create your views here.


def home(request):
    query = request.GET.get('search')
    if (query):
        args = {'query':query} 
        #Next we get all the company models that match the search
        matches=[]
        ratings=[]
        completed_survey = False
        for each_company in company.objects.all():
            if matches_func(each_company.name,query):
                if (each_company.name == query): #if an exact match, we want it to have index 0 in dict so that we can display it first
                    matches.insert(0,each_company.name)
                    ratings.insert(0,each_company.rating)
                else:
                   matches.append(each_company.name) #so args will have search query and the NAMES of all matching companies (not the actual model)
                   ratings.append(each_company.rating)
        
        if request.user.is_authenticated: #product searching only possible if logged in
            if (survey_answers.objects.filter(user_id=request.user.id).count() == 1): #must have answered survey
                completed_survey=True
                product_matches=[]
                product_company_ratings=[]
                for each_company in company.objects.all():
                    if (query in each_company.products):
                        
                        fairtrade = survey_answers.objects.get(user_id=request.user.id).supports_fairtrade
                        nochildlabor = survey_answers.objects.get(user_id=request.user.id).supports_nochildlabor
                        lowcarbonemissions = survey_answers.objects.get(user_id=request.user.id).supports_lowcarbonemissions
                        noanimaltesting = survey_answers.objects.get(user_id=request.user.id).supports_noanimaltesting
                        
                        comp_fairtrade=each_company.fairtrade
                        comp_ncl=each_company.nochildlabor
                        comp_lce = each_company.bcorp
                        comp_peta = each_company.peta
                       
                        fairtrade_condition = (fairtrade and comp_fairtrade) or (fairtrade==False)
                        nochildlabor_condition = (nochildlabor and comp_ncl) or (nochildlabor==False)
                        lce_condition = (lowcarbonemissions and comp_lce) or (lowcarbonemissions==False)
                        noanimaltesting_conditon = (noanimaltesting and comp_peta) or (noanimaltesting==False)
                        if (fairtrade_condition and nochildlabor_condition and lce_condition and noanimaltesting_conditon):
                            product_matches.append(each_company.name)
                            product_company_ratings.append(each_company.rating)
                args = {'query':query,'matches':matches, 'ratings':ratings,'product_matches':product_matches,'product_company_ratings':product_company_ratings,'completed_survey':completed_survey}
            else:
                 args = {'query':query,'matches':matches, 'ratings':ratings}          
        else:
             args = {'query':query,'matches':matches, 'ratings':ratings}

           
        return render(request, 'webpages/results.html', args)
    else:
        if (survey_answers.objects.filter(user_id=request.user.id).count() == 1):
            survey_answered = True
        else:
            survey_answered = False    

        #api data
        if datetime.now().month-1 < 10:
            added="0"
        else:
            added = "" 
        date =  str(datetime.now().year)+"-"+added+str(datetime.now().month-1)+ "-" + str(datetime.now().day)
        conn = http.client.HTTPSConnection('api.thenewsapi.com')
        params = urllib.parse.urlencode({
            'api_token': api_key, #api key / token 
            'search': 'ethics',
            'limit': 3,
            'published_after':date, 
            'locale':'us',
            'language':'en'
            }) 
        conn.request('GET', '/v1/news/all?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        decoded = data.decode('utf-8')
        data = json.loads(decoded)         
        title1 = data['data'][0]['title']
        description1 = data['data'][0]['description']
        url1 = data['data'][0]['url']
        title2 = data['data'][1]['title']
        description2 = data['data'][1]['description']
        url2 = data['data'][1]['url']
        title3 = data['data'][2]['title']
        description3 = data['data'][2]['description']
        url3 = data['data'][2]['url']
        
        args={'survey_answered':survey_answered,'title1':title1,'title2':title2,'title3':title3,'description1':description1,
              'description2':description2,'description3':description3,'url1':url1,'url2':url2,'url3':url3,} 
        return render(request, 'webpages/home.html',args)



def energy(request):
    
    companies = company.objects.filter(comp_type="energy")
    
    
    companies_list=[]
    companies_rating = []
    max_rating = 0
    max_index = 0
    for c in range (0,len(companies)):
        if (companies[c].rating>max_rating):
            max_rating = companies[c].rating
            max_index = c 
        companies_list.append(companies[c].name)
        companies_rating.append(companies[c].rating)
    first_company = companies[max_index].name
    first_company_rating = max_rating
    companies_list.pop(max_index)
    companies_rating.pop(max_index)

    args={'first':first_company,'first_rating':first_company_rating,'companies':companies_list,'companies_ratings':companies_rating}
    return render(request, 'webpages/energy.html', args)

def tech(request):

    companies = company.objects.filter(comp_type="tech")
    
    
    companies_list=[]
    companies_rating = []
    max_rating = 0
    max_index = 0
    for c in range (0,len(companies)):
        if (companies[c].rating>max_rating):
            max_rating = companies[c].rating
            max_index = c 
        companies_list.append(companies[c].name)
        companies_rating.append(companies[c].rating)
    first_company = companies[max_index].name
    first_company_rating = max_rating
    companies_list.pop(max_index)
    companies_rating.pop(max_index)

    args={'first':first_company,'first_rating':first_company_rating,'companies':companies_list,'companies_ratings':companies_rating}
    return render(request, 'webpages/tech.html', args)

def food_drink(request): 

    companies = company.objects.filter(comp_type="food")
    
    
    companies_list=[]
    companies_rating = []
    max_rating = 0
    max_index = 0
    for c in range (0,len(companies)):
        if (companies[c].rating>max_rating):
            max_rating = companies[c].rating
            max_index = c 
        companies_list.append(companies[c].name)
        companies_rating.append(companies[c].rating)
    first_company = companies[max_index].name
    first_company_rating = max_rating
    companies_list.pop(max_index)
    companies_rating.pop(max_index)

    args={'first':first_company,'first_rating':first_company_rating,'companies':companies_list,'companies_ratings':companies_rating}
    return render(request, 'webpages/food_drink.html', args)

def fashion(request):
    companies = company.objects.filter(comp_type="fashion")
    
      
    companies_list=[]
    companies_rating = []
    max_rating = 0
    max_index = 0
    for c in range (0,len(companies)):
        if (companies[c].rating>max_rating):
            max_rating = companies[c].rating
            max_index = c 
        companies_list.append(companies[c].name)
        companies_rating.append(companies[c].rating)
    first_company = companies[max_index].name
    first_company_rating = max_rating
    companies_list.pop(max_index)
    companies_rating.pop(max_index)

    args={'first':first_company,'first_rating':first_company_rating,'companies':companies_list,'companies_ratings':companies_rating}
    return render(request, 'webpages/fashion.html', args)




def error(request):
    return render(request, 'webpages/error.html')

@must_be_logged_in
def survey(request): 
    if request.method != 'POST':
        form = survey_form()
    else:
        form = survey_form(data=request.POST)
        if form.is_valid():
            survey_answers.objects.filter(user_id=request.user.id).delete() #if you submit a survey for the second time the old one is deleted as its useless.
            user_survey_answers = form.save(commit=False)
            user_survey_answers.user_id = CustomUser.objects.get(id=request.user.id) # or should it just be request.user.id
            user_survey_answers.save()
            return redirect('/')
    args={'form':form}
    return render(request,'webpages/survey.html', args)
 

 
def company_page(request, company_name):
    if request.method != 'POST':
        form = comment_form()
    else:
        form = comment_form(data=request.POST)
        if form.is_valid():

            users_comments_on_this_company = comments.objects.filter(companyname=company_name, username=request.user.username)
            bodies = []
            for comment in users_comments_on_this_company:
                bodies.append(comment.body)
            if (request.POST.get("body","") in bodies):
                return HttpResponseRedirect(request.path_info) #they tried to leave the same comment twice
            
            new_comment = form.save(commit=False)
            new_comment.username = CustomUser.objects.get(id=request.user.id).username
            new_comment.companyname = company_name 
            new_comment.upvotes = 0
            new_comment.downvotes = 0
            new_comment.date = str(datetime.now().day) + " " + toMonth(datetime.now().month)[:3].title() + " " + str(datetime.now().year)
            new_comment.save()
            return HttpResponseRedirect(request.path_info) #refresh page after submitting new comment

    company_model = company.objects.get(name=company_name)
    comments_arg = [] 
    try:
        comment_list = comments.objects.filter(companyname=company_name).order_by('-id') 
    except: 
        comment_list=[]
    
    for comment in comment_list:
        comments_arg.append((comment.username, comment.date, comment.body, comment.upvotes, comment.downvotes))

    if datetime.now().month-1 < 10:
        added="0"
    else:
        added = "" 
    date =  str(datetime.now().year-1)+"-"+added+str(datetime.now().month)+ "-" + str(datetime.now().day)
    conn = http.client.HTTPSConnection('api.thenewsapi.com')
    params = urllib.parse.urlencode({
        'api_token': api_key, #api key / token 
        'search': company_name+'+'+'(esg|ethics|sustainability|emissions|human rights)',
        'limit': 3,
        'published_after':date, 
        'locale':'us',
        'language':'en'
        }) 
    conn.request('GET', '/v1/news/all?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode('utf-8')
    data = json.loads(decoded)         
    news1 = data['data'][0]['title']
    news1source = data['data'][0]['url']
    news2 = data['data'][1]['title']
    news2source = data['data'][1]['url']
    news3 = data['data'][2]['title']
    news3source = data['data'][2]['url'] 
    
     

    
    
    args={'form':form,'company_name':company_name,'fairtrade':company_model.fairtrade,'nochildlabor':company_model.nochildlabor,'bcorp':company_model.bcorp,'peta':company_model.peta,
          'point1':company_model.point1,'source1':company_model.source1,'rating':company_model.rating,'stat1':company_model.stat1,'stat2':company_model.stat2,
          'stat3':company_model.stat3,'stat4':company_model.stat4,'stat1source':company_model.stat1source,'stat2source':company_model.stat2source,'stat3source':company_model.stat3source,
          'stat4source':company_model.stat4source,
          'news1':news1,'news2':news2,'news3':news3,'news1source':news1source,'news2source':news2source,'news3source':news3source,'comments':comments_arg}
    if (company_model.point2):
        args['point2']=company_model.point2 
        args['source2']=company_model.source2
    if (company_model.point3):
        args['point3']=company_model.point3
        args['source3']=company_model.source3
    if (company_model.point4):
        args['point4']=company_model.point4
        args['source4']=company_model.source4
    if (company_model.point5):
        args['point5']=company_model.point5
        args['source5']=company_model.source5
    if (company_model.point6):
        args['point6']=company_model.point6
        args['source6']=company_model.source6
    args['company_png_name'] = company_name.lower().replace(' ','_')
    return render(request,'webpages/company.html', args)


