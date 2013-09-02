from zope.component import adapts 
from zope.interface import Interface 
from zope.interface import implements
from plone.app.content.interfaces import INameFromTitle
from collective.academicprogrammes.interfaces import INameFromCourseCodeAndTitle

class NameFromCourseCodeAndTitle(object):
    """ Adapter to INameFromTitle """
    implements(INameFromTitle)
    adapts(INameFromCourseCodeAndTitle)

    def __init__(self, context):
        self.context = context
        pass

    @property
    def ztitle(self):
        return u"%s %s" % (self.context.course_code,
                        self.context.course_name)
  
    def __new__(cls, context):
        code = context.course_code
        name = context.course_name
        #Title()
        mytitle = u'%s %s' % (code,name)
        instance = super(NameFromCourseCodeAndTitle, cls).__new__(cls)
        instance.title = mytitle
        context.setTitle(mytitle)

        return instance