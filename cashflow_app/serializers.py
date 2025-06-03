from rest_framework import serializers
from .models import CashFlow, Type, Status, Category, Subcategory
from card.models import Account
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'created_at']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)       # для отображения связанного объекта
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type', write_only=True
    )  # для записи через ID

    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'type_id','created_at']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category', 'category_id','created_at']


class CashFlowSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source='status', write_only=True
    )

    type = TypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=Type.objects.all(), source='type', write_only=True
    )

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    subcategory = SubcategorySerializer(read_only=True)
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(), source='subcategory', write_only=True
    )

    account = serializers.SerializerMethodField(read_only=True)
    card_number = serializers.CharField(write_only=True, required=True)

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = CashFlow
        fields = [
            'id',
            'date',
            'account',
            'card_number',
            'status', 'status_id',
            'type', 'type_id',
            'category', 'category_id',
            'subcategory', 'subcategory_id',
            'amount',
            'comment'
        ]

    def get_account(self, obj):
        return {
            'id': obj.account.id,
            'account_number': getattr(obj.account, 'account_number', None),
            'card_number': getattr(obj.account, 'card_number', None),
            'balance': str(getattr(obj.account, 'balance', None)),
            'currency': getattr(obj.account, 'currency', None),
        }

    def validate_card_number(self, value):
        try:
            account = Account.objects.get(card_number=value)
        except Account.DoesNotExist:
            raise serializers.ValidationError("Account with this card number does not exist")
        return value

    def create(self, validated_data):
        card_number = validated_data.pop('card_number')
        account = Account.objects.get(card_number=card_number)

        # Пример простой логики изменения баланса (можешь подкорректировать)
        amount = validated_data.get('amount', 0)
        # Пример: если type_id == 1 — списание, если 2 — пополнение
        # Можно заменить на свои id или логику проверки
        type_obj = validated_data.get('type')

        if type_obj and type_obj.id == 1:  # списание
            if account.balance < amount:
                raise serializers.ValidationError("Insufficient balance on the card")
            account.balance -= amount
        else:  # пополнение или другие типы
            account.balance += amount

        account.save()

        validated_data['account'] = account
        return super().create(validated_data)
