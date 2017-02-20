from rest_framework import serializers
from course.models import Course, Chapter, Unit, CourseParticipation, Video


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        remove_fields = kwargs.pop('remove_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = fields
            existing = self.fields.keys()
            for field_name in existing - allowed:
                try:
                    self.fields.pop(field_name)
                except KeyError:
                    continue

        if remove_fields is not None:
            for field_name in remove_fields:
                try:
                    self.fields.pop(field_name)
                except KeyError:
                    continue


class CourseSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class ChapterSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class UnitSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class CourseParticipationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CourseParticipation
        fields = '__all__'


class VideoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

