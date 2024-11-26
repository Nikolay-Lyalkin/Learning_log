from django.contrib.auth.models import Group, Permission
import pytest


@pytest.fixture
def create_group_edit_product():
    group_edit_product = Group.objects.create(name='edit_product_per')
    delete_permission = Permission.objects.get(codename='delete_product')
    can_unpublished_product_permission = Permission.objects.get(codename='can_unpublished_product')
    group_edit_product.permissions.add(delete_permission, can_unpublished_product_permission)
    return group_edit_product
