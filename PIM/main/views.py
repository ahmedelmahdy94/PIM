from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from .pagination import Pagination

class ProductView(APIView):
    #Create new product
    def post(self, request):
        product = request.data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "Status": "200",
                "product": serializer.data,
                "message": "Product created successfully!"
            })
        else:
            return Response({
                "Status": "400",
                "message": "Invalid Request!"
            })

    """
    {
      "ProductCode": "code5",
      "ProductCategoryID": ["UUID",
    						"UUID2"
      ],
      "ProductName": "alien",
      "ProductPrice": 212,
      "ProductAvailableQuantity": 1,
      "ProductActive": true
      }
    """

class Productqu(APIView):
    # update specific product by product id
    def put(self, request, prod_id):
        db_prod = get_object_or_404(Product, pk=prod_id)
        if db_prod or db_prod is not None:
            new_prod = request.data
            serializer = ProductSerializer(instance=db_prod, data=new_prod, partial=True)
            if serializer.is_valid():
                product_updated = serializer.save()
                return Response({
                    "Status": "202",
                    "product": serializer.data,
                    "Message": "Product " + serializer.data.get('ProductCode') + " has been updated!"
                })
            else:
                return Response({
                    "Status": "400",
                    "Message": "Invalid ID supplied"
                })
        else:
            return Response({
                "Status": "404",
                "Message": "product not found"
    })
    # get specific product by product id
    def get(self, request, prod_id):
        db_prod = get_object_or_404(Product, pk=prod_id)
        if db_prod or db_prod is not None:
            serializer = ProductSerializer(db_prod)
            return Response({
                "Status": "200",
                "product": serializer.data
            })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
            })

    # # get specific product by product name
    # def get(self, request, product_name):
    #     product = get_object_or_404(Product, ProductName=product_name)
    #     if product or product is not None:
    #         serializer = ProductSerializer(product)
    #         return Response({'status': "200", 'product': serializer.data})
    #     else:
    #         return Response({'status': "404", 'message':"Product not found"})

    # suspend product by product id
    def delete(self, request, prod_id):
        product = get_object_or_404(Product, pk=prod_id)
        if product or product is not None:
            product.ProductActive = False
            product.save()
            return Response({'status': "200", 'message': "Product successfuly suspend"})
        else:
            return Response({'status': "404", 'message': "Not found."})

# get all actice products from database sperate in pages in each page 5 product
class ProductGetAllActice(APIView):
    def get(self, request, page_num):
        page = int(page_num)
        products = Product.objects.filter(ProductActive=True)
        page_number = request.GET.get('page', page)
        paginate_result = Pagination.do_paginate(products, page_number)
        products = paginate_result[0]
        serializer = ProductSerializer(products, many=True)
        return Response({
            "Status": "200",
            "products": serializer.data
        })

        """
        {
      "ProductCode": "code1",
      "ProductCategoryID": "UUID",
      "ProductName": "name",
      "ProductPrice": 12,
      "ProductAvailableQuantity": 1,
      "ProductActive": true,
      }
        """

# get all products from database sperate in pages in each page 5 product
class ProductGetAll(APIView):
    def get(self, request, page_num):
        page = int(page_num)
        product = Product.objects.all()
        print(len(list(product)))

        page_number = request.GET.get('page', page)
        paginate_result = Pagination.do_paginate(product, page_number)
        product = paginate_result[0]

        serializer = ProductSerializer(product, many=True)
        return Response({
            "Status": "200",
            "message": "All Products",
            "Product": serializer.data

        })

class CategoryViewCreate(APIView):
    #Create new category
    def post(self, request):
        category = request.data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "Status": "200",
                "category": serializer.data,
                "message": "Category created successfully!"
            })
        else:
            return Response({
                "Status": "400",
                "message": "Invalid Request!"
            })

    """
    {
      "CategoryName": "name",
      "CategoryActive": true
      }
    """

class CategoryView(APIView):
    # update specific category by category id
    def put(self, request, cate_id):
        db_cate = get_object_or_404(Category, pk=cate_id)
        if db_cate or db_cate is not None:
            new_cate = request.data
            serializer = CategorySerializer(instance=db_cate, data=new_cate, partial=True)
            if serializer.is_valid():
                category_updated = serializer.save()
                return Response({
                    "Status": "202",
                    "category": serializer.data,
                    "Message": "Category " + serializer.data.get('CategoryName') + " has been updated!"
                })
            else:
                return Response({
                    "Status": "400",
                    "Message": "Invalid Request!"
                })
        else:
            return Response({
                "Status": "404",
                "Message": "Invalid Request!"
    })

    # get specific category by category id
    def get(self, request, cate_id):
        db_cate = get_object_or_404(Category, pk=cate_id)
        if db_cate or db_cate is not None:
            serializer = CategorySerializer(db_cate)
            return Response({
                "Status": "200",
                "category": serializer.data
            })
        else:
            return Response({
                "Status": "404",
                "Message": "Not found."
            })

    # suspend category by category id
    def delete(self, request, cate_id):
        category = get_object_or_404(Category, pk=cate_id)
        if category or category is not None:
            category.CategoryActive = False
            category.save()
            return Response({'status': "200", 'message': "Category successfuly suspend"})
        else:
            return Response({'status': "404", 'message': "Not found."})

# get all actice categories from database sperate in pages in each page 5 category
class CategoryGetAllActice(APIView):
    def get(self, request, page_num):
        page = int(page_num)
        category = Category.objects.filter(CategoryActive=True)
        page_number = request.GET.get('page', page)
        paginate_result = Pagination.do_paginate(category, page_number)
        category = paginate_result[0]
        serializer = CategorySerializer(category, many=True)
        return Response({
            "Status": "200",
            "categories": serializer.data
        })


# get all categories from database sperate in pages in each page 5 category
class CategoryGetAll(APIView):
    def get(self, request, page_num):
        page = int(page_num)
        category = Category.objects.all()

        page_number = request.GET.get('page', page)
        paginate_result = Pagination.do_paginate(category, page_number)
        category = paginate_result[0]

        serializer = CategorySerializer(category, many=True)
        return Response({
            "Status": "200",
            "message": "All categories",
            "categories": serializer.data

        })
