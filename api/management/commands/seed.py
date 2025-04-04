from django.core.management.base import BaseCommand

from api.models import Column, Todo


class Command(BaseCommand):
    help = 'Seed the database with initial data'


    def handle(self, *args, **kwargs):
        if(Column.objects.all().__len__() == 0):
            col1 = Column.objects.create(name='Backlog')
            col2 = Column.objects.create(name='En Proceso')

            Todo.objects.create(column=col1, name='Estudiar Vue')
            Todo.objects.create(column=col1, name='Estudiar Net Core')
            Todo.objects.create(column=col2, name='Estudiar Python')
            self.stdout.write(self.style.SUCCESS('Database seeded!'))