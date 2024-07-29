from rest_framework import serializers
from .models import Retreat, Booking

class RetreatSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Retreat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        user_email = data.get('user_email')
        user_phone = data.get('user_phone')
        retreat_id = data.get('retreat').id

        if Booking.objects.filter(user_email=user_email,user_phone=user_phone, retreat_id=retreat_id).exists():
            raise serializers.ValidationError("This retreat has already been booked by the user.")
        return data
