from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class HomeView(ListView):
    model = Student
    template_name = 'students/home.html'
    context_object_name = 'students'
    ordering = ['-created_at']

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    ordering = ['-created_at']

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, 'Student added successfully!')
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully!')
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Student deleted successfully!')
        return super().delete(request, *args, **kwargs)

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'