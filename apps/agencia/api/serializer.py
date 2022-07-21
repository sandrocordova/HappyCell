from rest_framework.serializers import ModelSerializer
from apps.agencia.models import Post


# Create your views here.
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','EMPR_CODIGO','EMPR_NOMBRE','EMPR_IDENTIFICACION']