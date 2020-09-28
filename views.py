from django.shortcuts import render
import mysql.connector


def index(request):
    flag = 0
    return render(request, 'index.html', {"flag": flag})


def submit(request):
    firstName = request.POST.get('First_Name')
    lastName = request.POST.get('Last_Name')
    studentID = request.POST.get('Student_ID')
    email_Id = request.POST.get('Email_Id')
    address = request.POST.get('Address')
    gpa = request.POST.get('gpa')
    print("DATA RECEVIED")
    conn = mysql.connector.connect(host='35.232.248.17', database='project_1', user='root', password='toor')
    cursor = conn.cursor()
    query = "Insert into project_1.student (StudentID, firstname, lastname, email, address, GPA) VALUES " \
            "('%s', '%s', '%s', '%s', '%s', '%s')"\
            % (studentID, firstName, lastName, email_Id, address, gpa)
    cursor.execute(query)
    conn.commit()
    flag = 1
    return render(request, 'index.html', {"flag": flag})


def search(request):
    searchParameter = request.POST.get('search')
    conn = mysql.connector.connect(host='35.232.248.17', database='project_1', user='root', password='toor')
    cursor = conn.cursor()
    query = "select * from project_1.student where '%s' in (StudentID, firstname, lastname)" % searchParameter
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'showStudents.html', {'rows': rows})


def showStudents(request):
    conn = mysql.connector.connect(host='35.232.248.17', database='project_1', user='root', password='toor')
    cursor = conn.cursor()
    query = "select * from project_1.student"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(rows)
    return render(request, 'showStudents.html', {'rows': rows})
