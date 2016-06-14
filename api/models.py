from django.db import models
from core.models import Group
from core.models import Room
from core.models import Semester
from core.models import Teacher

from core.fields import DayOfTheWeekField
from core.fields import PairField
from core.fields import ParityField


class Schedule(models.Model):
    group = models.ForeignKey(Group)
    semester = models.ForeignKey(Semester)

    def __str__(self):
        return "Группа - %s, семестр %s" % \
               (str(self.group), str(self.semester))


class Exercise(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    teacher = models.ManyToManyField(Teacher)

    exercise_name = models.CharField("Название занятия", max_length=100)
    pair = PairField("Номер пары", default=1)
    day = DayOfTheWeekField("День недели", default=1)
    parity = ParityField("Четность", default=1)

    def __str__(self):
        return "%s пара в %s, %s" % \
               (self.get_pair_display(), self.get_day_display(), str(self.exercise_name))
