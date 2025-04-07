from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

# Define session timeout duration (in minutes)
ALLOTTED_TIME = 0.5

def index(request):
    if 'owner_id' in request.session:
        current_time = datetime.datetime.now()

        # Ensure 'login_time' is set in session
        if 'login_time' not in request.session:
            request.session['login_time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")

        # Convert session login time to datetime object
        login_time = datetime.datetime.strptime(request.session['login_time'], "%Y-%m-%d %H:%M:%S")

        # Check if the session has expired
        if current_time - login_time < datetime.timedelta(minutes=ALLOTTED_TIME):
            request.session['login_time'] = current_time.strftime("%Y-%m-%d %H:%M:%S")  # Update login time
            return render(request, 'owner/index.html')
        else:
            request.session.flush()  # Clear session if timeout occurs
            param = {'m': 'Session timed out. Please log in again.'}
            return render(request, 'login.html', param)
    else:
        param = {'m': 'Please log in first.'}
        return render(request, 'login.html', param)


def logout(request):
    request.session.flush()  # Clear session data
    return redirect('/')  # Redirect to main index page
