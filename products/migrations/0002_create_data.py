from django.db import migrations


def create_fish_data(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Category = apps.get_model('products', 'Category')

    products_data = [
        {'title': 'Macbook Air 2016', 'is_published': True, 'category_id': 1},
        {'title': 'Macbook Air 2018', 'is_published': False, 'category_id': 1},
        {'title': 'Iphone 10', 'is_published': True, 'category_id': 2},
        {'title': 'Iphone XXL', 'is_published': True, 'category_id': 2},
    ]

    categories_data = [
        {'title': 'Ноутбуки', 'id': 1},
        {'title': 'Телефоны', 'id': 2},
    ]

    for category_info in categories_data:
        Category(**category_info).save()
    for product_info in products_data:
        Product(**product_info).save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_fish_data),
    ]
