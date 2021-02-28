from rest_framework import serializers
from users.serializers import RelatedUserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    user = RelatedUserSerializer()

    class Meta:
        model = Room
        exclude = ("modified",)
        read_only_fields = ('user', 'id','created','updated')

    def validate(self,data):
        if not self.instance:
            check_in = data.get('check_in', self.instance.check_in)
            check_out = data.get('check_out', self.instance.check_out)
        else:
            check_in = data.get('check_in', self.instance.check_in)
            check_out = data.get('check_out', self.instance.check_out)

        if check_in == check_out:
            raise serializers.ValidationError("Not Enough time between changes")
        return data
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name')
    #     instance.address = validated_data.get('address')
    #     instance.price = validated_data.get('price')
    #     instance.beds = validated_data.get('beds')
    #     instance.lat = validated_data.get('lat')
    #     instance.lng = validated_data.get('lng')
    #     instance.bedrooms = validated_data.get('bedrooms')
    #     instance.bathrooms = validated_data.get('bathrooms')
    #     instance.check_in = validated_data.get('check_in')
    #     instance.check_out = validated_data.get('check_out')
    #     instance.instant_book = validated_data.get('instant_book')
    #     instance.save()
    #     return instance
