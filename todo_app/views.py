from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from todo_app.forms import TaskForm
from todo_app.models import Tasks
from todo_app.serializer import TaskSerializer
from utils.util import get_edited_data


class HomeView(ListView):
    permission_classes = (AllowAny,)
    model = Tasks
    template_name = "home.html"

    def get_queryset(self):
        return Tasks.objects.filter(is_deleted=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["list"] = Tasks.objects.filter(is_deleted=False)
        print(context)
        context["forms"] = TaskForm()
        return context


class TaskListView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        all_tasks = Tasks.objects.filter(is_deleted=False)
        query_params = request.GET.dict()
        print(query_params)
        page = int(query_params.get('page', 1))
        limit = int(query_params.get('limit', 3))
        size = 3
        offset = (page - 1) * size
        if query_params and all_tasks and page > 0 and limit < size:
            all_tasks = all_tasks[offset: offset + limit]
        form = TaskForm()
        context = {'todo_list': all_tasks, "forms": form}
        return render(request, 'tasks.html', context)

    def post(self, request, *args, **kwargs):
        print('-----------')
        form = TaskForm(request.POST)
        try:
            print(form)
            print(form.cleaned_data)
            print(form.is_valid())
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            due_date = form.cleaned_data.get('due_date')
            new_task = Tasks(title=title, description=description, due_date=due_date)
            new_task.save()
            context = {
                'todo_list': Tasks.objects.filter(is_deleted=False),
                'title': 'Tasks'
            }
            return render(request, 'home.html', context)

        except Exception as e:
            print(e)
            return render(request, 'home.html', {})


class SingleTaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        if kwargs.get('func') == 1:
            return self.put(request, *args, **kwargs)
        if kwargs.get('func') == 2:
            return self.delete(request, *args, **kwargs)
        try:
            task = Tasks.objects.filter(is_deleted=False).get(id=kwargs.get('id'))
            return render(request, 'tasks.html', {'todo_list': [task]})
        except Exception as e:
            task = None
            form = TaskForm()
            return render(request, 'tasks.html', {'todo_list': task, 'forms': form})

    def put(self, request, *args, **kwargs):
        task = Tasks.objects.get(id=1)
        form = TaskForm(request.GET)
        if form.is_valid():
            print('*****************')
            print(request.GET)
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.due_date = form.cleaned_data.get('due_date')
            task.status = True if request.GET.get("status") else form.cleaned_data.get('status')
            print('----------------', task, form.cleaned_data)
            task.save()
            return render(request, 'home.html', {'task': task, 'forms': form})

        return render(request, 'form.html', {'task': task, 'forms': form})

    def delete(self, request, *args, **kwargs):
        print(request)
        task_id = kwargs.get('id')
        task = Tasks.objects.get(id=task_id)
        task.is_deleted = True
        task.save()
        return render(request, 'home.html', {'task': task})

    pass


class TaskFormView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        try:
            task_id = kwargs.get('id')
            task = Tasks.objects.get(id=task_id)
            task.due_date = str(task.due_date)
            return render(request, 'form.html', {'task': task})
        except:
            return render(request, 'form.html', {})


class AddTaskFormView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        return render(request, 'add_task_form.html', {})
