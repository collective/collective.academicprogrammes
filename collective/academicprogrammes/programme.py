from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item
from plone.directives import dexterity, form
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from collective.academicprogrammes import MessageFactory as _
from collective.academicprogrammes.course import ICourse
from plone.supermodel import model

# Interface class; used to define content-type schema.

class _IProgramme(form.Schema, IImageScaleTraversable):
    """
    Programme
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/programme.xml to define the content type.

    form.model("models/programme.xml")

class IProgramme(_IProgramme,model.Schema):
    """
    Programme Profile
    """

    courses = RelationList(
    title=u"Courses",
    default=[],
    value_type=RelationChoice(title=_(u"Course"),
                              source=ObjPathSourceBinder(object_provides=ICourse.__identifier__)),
    required=False,
)

class Programme(Item):
    grok.implements(IProgramme)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# programme_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    """ sample view class """

    grok.context(IProgramme)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
