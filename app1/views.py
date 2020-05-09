from django.shortcuts import render, redirect
import recomm

def index(request):
    s=''
    c_d={}
    try:   
        with open('recent.txt','r') as f1:
            s=''
            for line in f1:
                s+=line
    except:
        print("NO FILE FOUND")
    s=s.strip().split('\n')[::-1]
    c_d['recent']=s[0:5]
    
    if request.method=='POST':
        mov=request.POST['movie']
        
        
        a=recomm.give_rec(mov)
        if a==False:
            c_d['nomov']='No Movie Found'
        else:
            c_d['movies']=a
            c_d['movName']=mov
            s.insert(0,mov)
            c_d['recent']=s[0:5]
            with open('recent.txt','a+') as f:
                f.seek(0,2)
                f.write(mov+'\n')

    return render(request,'app1/index.html',c_d)

# Create your views here.

