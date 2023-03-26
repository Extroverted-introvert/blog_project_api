from blog.dynamic_field_serializer import DynamicFieldsModelSerializer
from .models import BlogPost
import socket


class CustomBlogData(DynamicFieldsModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        HOSTIP = socket.gethostbyname(socket.gethostname())
        ret["thumbnail"] = "https://blogprojectapi.parthtripathi1.repl.co" + ret["thumbnail"]
        return ret
