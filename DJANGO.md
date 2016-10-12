
# Command lines
    django-admin startproject mysite
    cd mysite
    ./manage.py startapp itaiching
    
    ./manage.py makemirgrations
    ./manage.py migrate
    ./manage.py runserver $IP:$PORT
    
    
    
# mysite settings

    INSTALLED_APPS = [
        'itaijing',
    
    TIME_ZONE = 'Asia/Taipei'