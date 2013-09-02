from plone.directives import dexterity, form
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model
from collective.academicprogrammes import MessageFactory as _
from plone.app.content.interfaces import INameFromTitle

class INameFromCourseCodeAndTitle(INameFromTitle):
  
    def title(context):
        """Return a custom title"""

class _ICourse(form.Schema, IImageScaleTraversable):
    """
    Course
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/course.xml to define the content type.

    form.model("models/course.xml")

class IICourse(_ICourse,model.Schema):
    """
    Course Profile
    """

