from datetime import datetime
from django.utils import timezone
from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

toy_release_date = timezone.make_aware(datetime.now(),
timezone.get_current_timezone())
toy1 = Toy(name='New action about our feature', 
    description='Angola, have more one languages', 
    release_date=toy_release_date, 
    toy_category='Speakres', 
    was_included_in_home=False)
toy1.save()
toy2 = Toy(name='JUG Huila', 
    description='The best event about tech in Angola',
    release_date=toy_release_date, toy_category='Tech',
    was_included_in_home=True)
toy2.save()

serializer_for_toy1 = ToySerializer(toy1)
print(serializer_for_toy1.data)

serializer_for_toy2 = ToySerializer(toy2)
print(serializer_for_toy2.data)

json_renderer = JSONRenderer()
toy1_rendered_into_json = json_renderer.render(serializer_for_toy1.data)
toy2_rendered_into_json = json_renderer.render(serializer_for_toy2.data)
print(toy1_rendered_into_json)
print(toy2_rendered_into_json)

json_string_for_new_toy = '{"name":"GDG Huila","description":"Comming soon", "release_date":"2022-10-09T12:10:00.776594Z","toy_category":"GDG","was_included_in_home":false}'
json_bytes_for_new_toy = bytes(json_string_for_new_toy, encoding="UTF-8")
stream_for_new_toy = BytesIO(json_bytes_for_new_toy)
parser = JSONParser()
parsed_new_toy = parser.parse(stream_for_new_toy)
print(parsed_new_toy)

new_toy_serializer = ToySerializer(data=parsed_new_toy)
if new_toy_serializer.is_valid():
    toy3 = new_toy_serializer.save()
    print(toy3.name)

