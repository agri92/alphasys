from django import forms
from django.forms import ChoiceField

from student_management_app.models import Courses, SessionYearModel, Subjects, Students

class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class StudentModelForm(forms.ModelForm):
        
        class Meta:
            model = Students
            fields = '__all__'

class AddCourseForm(forms.Form):
    course_name=forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre"}))
    duracion_choices =(
    ("0", "Ninguno"),
    ("1", "1 mes"),
    ("3", "3 meses"),
    ("6", "6 meses"),
    ("12", "12 meses")
    )
    duracion=forms.ChoiceField(label="Duración", choices=duracion_choices, widget=forms.Select(attrs={"class":"form-control", "placeholder":"Duración"}))
    costo_ins=forms.DecimalField(label="Costo Inscripción",max_digits=7, decimal_places=2, widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"0"}))
    costo_mat=forms.DecimalField(label="Costo Material",max_digits=7, decimal_places=2, widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"0"}))
    costo_mes=forms.DecimalField(label="Costo Mensualidad",max_digits=7, decimal_places=2, widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"0"}))
    descuento_pp=forms.DecimalField(label="Descuento",max_digits=7, decimal_places=2, widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"0"}))
    detalles=forms.CharField(label="Detalles",max_length=255, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Detalles"}))

class AddStudentForm(forms.Form):
    first_name=forms.CharField(label="Nombre",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre"}))
    last_name=forms.CharField(label="Apellido",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Apellido"}))
    username=forms.CharField(label="Usuario",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off","placeholder":"Usuario"}))
    email=forms.EmailField(label="E-mail",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control","autocomplete":"off","placeholder":"E-mail"}))
    password=forms.CharField(label="Contraseña",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Contraseña"}))
    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )    
    sex=forms.ChoiceField(label="Sexo",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    cell_phone=forms.CharField(label="Celular",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Celular"}))
    address=forms.CharField(label="Dirección",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Dirección"}))
    course_list=[]
    course_list=[]
    try:
        courses=Courses.objects.all()
        for course in courses:
            small_course=(course.id,course.course_name)
            course_list.append(small_course)
    except:
        course_list=[]
    course=forms.ChoiceField(label="Curso", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    start_date=forms.DateField(widget=DateInput(attrs={"class":"form-control"}))
    end_date=forms.DateField(widget=DateInput(attrs={"class":"form-control"}))
    status_choices =(
    ("0", "Baja"),
    ("1", "Activo"),
    ("2", "Inactivo")
    )
    status=forms.ChoiceField(label="Estatus", choices = status_choices, widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))
    details=forms.CharField(label="Detalles",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Detalles"}), required=False)

class EditStudentForm(forms.Form):
    first_name=forms.CharField(label="Nombre",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre"}))
    last_name=forms.CharField(label="Apellido",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Apellido"}))
    username=forms.CharField(label="Usuario",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","autocomplete":"off","placeholder":"Usuario"}))
    email=forms.EmailField(label="E-mail",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control","autocomplete":"off","placeholder":"E-mail"}))
    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )    
    sex=forms.ChoiceField(label="Sexo",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    cell_phone=forms.CharField(label="Celular",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Celular"}))
    address=forms.CharField(label="Dirección",max_length=50,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Dirección"}))
    #course_list=[]
    #course_list=[]
    #try:
    #    courses=Courses.objects.all()
    #    for course in courses:
    #        small_course=(course.id,course.course_name)
    #        course_list.append(small_course)
    #except:
    #    course_list=[]
    course=forms.ModelChoiceField(label="Curso", queryset=Courses.objects.all(), empty_label="- Selecciona un curso -",widget=forms.Select(attrs={"class":"form-control"}))
    start_date=forms.DateField(widget=DateInput(attrs={"class":"form-control"}))
    end_date=forms.DateField(widget=DateInput(attrs={"class":"form-control"}))
    status_choices =(
    ("0", "Baja"),
    ("1", "Activo"),
    ("2", "Inactivo")
    )
    status=forms.ChoiceField(label="Estatus", choices = status_choices, widget=forms.Select(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}), required=False)
    details=forms.CharField(label="Detalles",max_length=255,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Detalles"}))

class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.staff_id=kwargs.pop("staff_id")
        super(EditResultForm,self).__init__(*args,**kwargs)
        subject_list=[]
        try:
            subjects=Subjects.objects.filter(staff_id=self.staff_id)
            for subject in subjects:
                subject_single=(subject.id,subject.subject_name)
                subject_list.append(subject_single)
        except:
            subject_list=[]
        self.fields['subject_id'].choices=subject_list

    session_list=[]
    try:
        sessions=SessionYearModel.object.all()
        for session in sessions:
            session_single=(session.id,str(session.session_start_year)+" TO "+str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list=[]

    subject_id=forms.ChoiceField(label="Subject",widget=forms.Select(attrs={"class":"form-control"}))
    session_ids=forms.ChoiceField(label="Session Year",choices=session_list,widget=forms.Select(attrs={"class":"form-control"}))
    student_ids=ChoiceNoValidation(label="Student",widget=forms.Select(attrs={"class":"form-control"}))
    assignment_marks=forms.CharField(label="Assignment Marks",widget=forms.TextInput(attrs={"class":"form-control"}))
    exam_marks=forms.CharField(label="Exam Marks",widget=forms.TextInput(attrs={"class":"form-control"}))


    
    
    