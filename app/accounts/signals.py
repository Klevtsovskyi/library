from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    librarian, _ = Group.objects.get_or_create(name='Librarian')
    reader, _ = Group.objects.get_or_create(name='Reader')

    add_bookinstance = Permission.objects.get(codename='add_bookinstance')
    change_bookinstance = Permission.objects.get(codename='change_bookinstance')
    delete_bookinstance = Permission.objects.get(codename='delete_bookinstance')

    librarian.permissions.add(add_bookinstance, change_bookinstance, delete_bookinstance)
