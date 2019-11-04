import graphene
from graphene_django.types import DjangoObjectType

from .models import Category, Product
from graphene_django.filter import DjangoFilterConnectionField


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['title', 'products']
        interfaces = (graphene.relay.Node,)


class Query(object):
    category = graphene.relay.Node.Field(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)

    product = graphene.relay.Node.Field(ProductType)
    all_products = DjangoFilterConnectionField(ProductType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, title):
        Category(title=title).save()
        return CreateCategory(ok=True)
