from five import grok
from Acquisition import aq_inner
from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item
from plone.directives import dexterity, form
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from collective.academicprogrammes import MessageFactory as _
from collective.academicprogrammes.interfaces import IICourse
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from collective.academicprogrammes.backref import back_references


class ICourse(IICourse):
    """
    Course Profile
    """

    prerequisites = RelationList(
    title=u"Prerequisites",
    default=[],
    value_type=RelationChoice(title=_(u"Prerequisite"),
                              source=ObjPathSourceBinder(object_provides=IICourse.__identifier__)),
    required=False,
)
class Course(Item):
    grok.implements(ICourse)

    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# course_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    """ sample view class """

    grok.context(ICourse)
    grok.require('zope2.View')

    def semesters(self):
        semester_list = list(self.context.semester)
        semester_list.sort()
        #semester_list.reverse()
        return semester_list
    # grok.name('view')

    # Add view methods here
    @property
    def programme_refs(self):
        context = aq_inner(self.context)
        return back_references(self.context, 'courses')
