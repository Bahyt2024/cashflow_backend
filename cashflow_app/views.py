from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CashFlow, Type, Status, Category, Subcategory
from .serializers import (
    CashFlowSerializer, TypeSerializer,
    StatusSerializer, CategorySerializer, SubcategorySerializer
)

from accounts.permissions import IsAdmin
from rest_framework.exceptions import ValidationError

# --------------------
# CashFlow views
# --------------------

class CashFlowListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cashflows = CashFlow.objects.all()
        serializer = CashFlowSerializer(cashflows, many=True)
        return Response(serializer.data)

class CashFlowCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Раскомментируй при необходимости

    def post(self, request):
        serializer = CashFlowSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                # Возвращаем ошибку валидации (например, недостаточно средств)
                return Response({'detail': e.detail if hasattr(e, 'detail') else str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                # Обработка других исключений
                return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CashFlowUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        cashflow = get_object_or_404(CashFlow, pk=pk)
        serializer = CashFlowSerializer(cashflow, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CashFlowDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        cashflow = get_object_or_404(CashFlow, pk=pk)
        cashflow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------
# Type views
# --------------------

class TypeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        types = Type.objects.all()
        serializer = TypeSerializer(types, many=True)
        return Response(serializer.data)

class TypeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        type_obj = get_object_or_404(Type, pk=pk)
        serializer = TypeSerializer(type_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        type_obj = get_object_or_404(Type, pk=pk)
        type_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------
# Status views
# --------------------

class StatusListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response(serializer.data)

class StatusCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusUpdateView(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        status_obj = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(status_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusDeleteView(APIView):
    # permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        status_obj = get_object_or_404(Status, pk=pk)
        status_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------
# Category views
# --------------------

class CategoryListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryUpdateView(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(APIView):
    # permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------
# SubCategory views
# --------------------

class SubCategoryListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        subcategories = Subcategory.objects.all()
        serializer = SubcategorySerializer(subcategories, many=True)
        return Response(serializer.data)

class SubCategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SubcategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubCategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        subcategory = get_object_or_404(Subcategory, pk=pk)
        serializer = SubcategorySerializer(subcategory, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubCategoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        subcategory = get_object_or_404(Subcategory, pk=pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------
# API для динамического фильтра
# --------------------

from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories_by_type(request, type_id):
    categories = Category.objects.filter(type_id=type_id)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subcategories_by_category(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id)
    serializer = SubcategorySerializer(subcategories, many=True)
    return Response(serializer.data)
