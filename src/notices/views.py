from django.shortcuts import render, redirect

from .models import Notice

# def noticeList(request):
# 	qs = Notice.objects.all().order_by('-date_created')[:5]
# 	return render(request, 'index.html', {'qs':qs})

def noticeDetail(request,id):
	print("========>",id)
	print("------------------->", request.GET.get('id'))
	# updateObject = Notice.objects.get(pk=pk)
	# print(updateObject)
	return render(request, 'index.html')

def allNotices(request):
    notices = Notice.objects.all().order_by('-date_created')
    # paginator = Paginator(notices, 2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request,'notices.html',{'notices':notices})
