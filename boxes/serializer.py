from rest_framework.fields import IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from boxes.models import Box


class BoxSerializer(ModelSerializer):
    length = IntegerField()
    breadth = IntegerField()
    height = IntegerField()

    def get_updated_at(self, obj):
        return obj.updated_at.isoformat()

    class Meta:
        model = Box

    def get_fields(self):

        if self.context["request"] and self.context["request"].method == "GET":
            fields = self.get_get_fields()
        else:
            fields = self.get_post_fields()

        return fields

    def get_post_fields(self):
        if self.instance is None:
            return {
                "length": IntegerField(),
                "breadth": IntegerField(),
                "height": IntegerField(),
                "created_by_id": IntegerField(required=True)
            }
        else:
            return {
                "length": IntegerField(),
                "breadth": IntegerField(),
                "height": IntegerField(),
            }

    def get_get_fields(self):
        fields = {
            "length": IntegerField(),
            "breadth": IntegerField(),
            "height": IntegerField()
        }
        if self.context["request"] and self.context["request"].user and self.context["request"].user.is_staff:
            fields["created_by_id"] = IntegerField()
            fields["updated_at"] = SerializerMethodField()

        return fields

    def get_extra_kwargs(self):
        extra_kwargs = super(BoxSerializer, self).get_extra_kwargs()
        extra_kwargs.update({
            "created_by_id": {"read_only": True},
            "created_at": {"read_only": True}
        })

