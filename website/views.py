from blog.models import Post
from .form import ContactForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.utils.http import urlunquote
from meta.views import Meta
from paginator.utils import paginate

# root page
def index(request):
    meta = Meta(
        title="کنترل ارتباطات هوشمند آریا",
        description='آموزش های مبتنی بر اینترنت اشیا و هوش مصنوعی به زبان پایتون و طراحی سایت های مبتنی بر Django',
        keywords=['طراحی سایت', 'هوش مصنوعی', 'اینترنت اشیا','آموزش'],
        locale= 'fa_IR',
        url = request.build_absolute_uri() ,
        twitter_site= "icc-aria",
        schemaorg_title = "کنترل ارتباطات هوشمند آریا",
        
    )

    return render(request, "website/index.html",{"meta":meta})


def contact_view(request):
    meta = Meta(
        title="ارتباط با ما",
        description='راتباط با ما و مشاوره در حوزه های مختلف فناوری',
        keywords=['طراحی سایت', 'هوش مصنوعی', 'اینترنت اشیا','مشاوره'],
        locale= 'fa_IR',
        url = request.build_absolute_uri() ,
        twitter_site= "icc-aria"
    )
    
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your ticket has been recieved')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'wew have got an error')
            return HttpResponse(status=400)
            #return HttpResponseRedirect(request.path_info)
    else:
        contactform = ContactForm()
        context = {"form": contactform,"meta":meta}
        return render(request, "website/contact.html", context)
    


def about_view(request):
    meta = Meta(
        title="درباره ما",
        description='ما پایتون، هوش مصنوعی و هوش تجاری را در کنار هم به کار بردیم تا یک پلتفرم شگفت انگیز اینترنت اشیا بسازیم، امیدواریم که لذت ببرید',
        keywords=['طراحی سایت', 'هوش مصنوعی', 'اینترنت اشیا','آموزش'],
        locale= 'fa_IR',
        url = request.build_absolute_uri() ,
        twitter_site= "icc-aria"
    )
    return render(request, "website/about.html",{"meta":meta})


def privacy(request):
    meta = Meta(
        title="حریم خصوصی",
        description='کنترل ارتباطات هوشمند آریا در راستای حفظ امنیت و حریم خصوصی کاربران خود اعلام می کند که از هرگونه اطلاعات وارد شده توسط کاربران اعم از ایمیل، پیام هاو هرگونه اطلاعات شخصی، محافظت کرده و به هیچ عنوان این اطلاعات را در اختیار سازمان ها و مراکز دیگر به منظور تبلیغات با خدمات دیگر ارائه ندهد',
        keywords=['نحوه استفاده', 'استفاده', 'قوانین'],
        locale= 'fa_IR',
        url = request.build_absolute_uri() ,
        twitter_site= "icc-aria"
    )
    return render(request, "website/privacy.html",{"meta":meta})


def rules(request):
    meta = Meta(
        title="شرایط استفاده",
        description='دانشجویان و برنامه نویسان عزیز، لطفا به هنگام شرکت در دوره ها و استفاده از مطالب، موارد زیر را رعایت فرمایید .',
        keywords=['شرایط استفاده','قوانین'],
        locale= 'fa_IR',
        url = request.build_absolute_uri() ,
        twitter_site= "icc-aria"
    )
    return render(request, "website/rules.html",{"meta":meta})

def error_400(request, exception):
    context = {'exeption': exception}
    response = render(request, "errors/400.html", context=context)
    response.status_code = 400
    return response


def error_403(request, exception):
    context = {'exeption': exception}
    response = render(request, "errors/403.html", context=context)
    response.status_code = 403
    return response


def error_404(request, exception):
    context = {'exeption': exception}
    response = render(request, "errors/404.html", context=context)
    response.status_code = 404
    return response


def error_500(request):
    context = {}
    response = render(request, "errors/500.html", context=context)
    response.status_code = 500
    return response

