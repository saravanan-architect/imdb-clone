from rest_framework import serializers

from watchlist_app.models import Movie


#  class bases ModelSerializer -  it just serializes the data and sends it to the client
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description', 'active'], it will exclude the active field, and include all other fields
        # exclude = ['active']

    def get_len_name(self, obj):
        return len(obj.name)

    # Field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value

    # Object level validation
    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError(
                "Name and Description should be different"
            )
        return data


# # instance level validation
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError(f"{value} - Name is too short")
#     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     # instance carries old data, validated_data carries new data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

# # field level validation
# def validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     return value

#     # complete object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different")
#         return data


# Serializers are used to convert complex data types, such as Django model instances, to native
# Python datatypes that can then be easily rendered into JSON, XML or other content types.
# Serializers also provide deserialization, allowing parsed data to be converted back
# into complex types, after first validating the incoming data.

# from rest_framework import serializers

# from watchlist_app.models import Movie


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     # instance carries old data, validated_data carries new data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance
