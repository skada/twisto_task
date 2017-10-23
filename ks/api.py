from rest_framework import routers, serializers, viewsets
from drf_writable_nested import WritableNestedModelSerializer
from ks.models import KSTask, InputItem, ResultItem


class InputItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputItem
        fields = ['index', 'value', 'weight', ]


class ResultItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultItem
        fields = ['index', 'value', 'weight', ]


class KSTaskSerializer(WritableNestedModelSerializer):
    items = InputItemSerializer(many=True)
    results = ResultItemSerializer(many=True, read_only=True)

    class Meta:
        model = KSTask
        exclude = ['task_id', ]


class KSTaskViewSet(viewsets.ModelViewSet):
    serializer_class = KSTaskSerializer
    queryset = KSTask.objects.all()
    http_method_names = ['get', 'post', 'head']


router = routers.DefaultRouter()
router.register('task', KSTaskViewSet)
