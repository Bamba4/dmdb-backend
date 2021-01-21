import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


def serializerEmployee(data, modelSerializer):
    serializer = modelSerializer(data)
    content = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream)
    serializer = modelSerializer(data=data)
    return serializer


