from unittest import TestCase

from core.models import Room, Location


class RoomTestCase(TestCase):
    location_name = "Кафедра САПРиУ"
    room_name = "ауд. 6"

    def setUp(self):
        Room.objects.create(name=self.room_name, location=Location.objects.create
        (name=self.location_name, geo_position="None"))

    def test_room_str_is_equal_to_location_str(self):
        room = Room.objects.get(pk=1)
        self.assertEqual(str(room), self.location_name)
