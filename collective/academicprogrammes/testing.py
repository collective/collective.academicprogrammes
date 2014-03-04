# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_ROLES
from plone.app.testing import setRoles
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.textfield import RichTextValue
from plone.dexterity.utils import createContentInContainer
from plone.testing import z2
from z3c.relationfield import RelationValue
from zope.component import getUtility
from zope.intid import IIntIds


class CollectiveAcademicProgrammesLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Configure all packages providing plone.supermodel-fields for our
        # content types as required by plone.supermodel
        # See also: http://plone.293351.n2.nabble.com/SupermodelParseError-Field-type-plone-app-textfield-RichText-specified-for-field-body-is-not-supportd-tp7569207p7569228.html
        import plone.app.textfield
        self.loadZCML(package=plone.app.textfield)
        import plone.namedfile
        self.loadZCML(package=plone.namedfile)

        # Configure collective.academicprogrammes
        import collective.academicprogrammes
        self.loadZCML(package=collective.academicprogrammes)

    def setUpPloneSite(self, portal):
        # Set default workflow chain, because PLONE_FIXTURE has not one
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')
        # Apply profile for collective.academicprogrammes
        self.applyProfile(portal, 'collective.academicprogrammes:default')

    def tearDownZope(self, app):
        pass

ACADEMIC_PROGRAMMES_FIXTURE = CollectiveAcademicProgrammesLayer()

ACADEMIC_PROGRAMMES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACADEMIC_PROGRAMMES_FIXTURE,),
    name='CollectiveAcademicProgrammes:Integration')

ACADEMIC_PROGRAMMES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACADEMIC_PROGRAMMES_FIXTURE,),
    name='CollectiveAcademicProgrammes:Functional')


class CollectiveAcademicProgrammesAcceptanceLayer(PloneSandboxLayer):
    defaultBases = (ACADEMIC_PROGRAMMES_FIXTURE,)

    def setUpPloneSite(self, portal):
        wftool = getToolByName(portal, 'portal_workflow')
        setRoles(portal, TEST_USER_ID, ['Manager'])

        # Create container for courses
        portal.invokeFactory('Folder', 'courses', title=u'Courses')
        wftool.doActionFor(portal['courses'], 'publish')

        # Create course
        ROBOTS001 = createContentInContainer(
            portal['courses'],
            'collective.academicprogrammes.course',
            course_name=u"What is Robot Framework",
            course_code=u"ROBOTS001",
            course_level='1',
            course_semester='1',
            credits='1'
        )
        wftool.doActionFor(ROBOTS001, 'publish')

        # IntIds are required for relations
        intids = getUtility(IIntIds)

        # Create course
        ROBOTS002 = createContentInContainer(
            portal['courses'],
            'collective.academicprogrammes.course',
            course_name=u"More about Robot Framework",
            course_code=u"ROBOTS002",
            course_level='2',
            course_semester='1',
            credits='2',
            prerequisites=[
                RelationValue(intids.getId(ROBOTS001)),
            ]
        )
        wftool.doActionFor(ROBOTS002, 'publish')

        # Create course
        ROBOTS003 = createContentInContainer(
            portal['courses'],
            'collective.academicprogrammes.course',
            course_name=u"Robot Framework plain text syntax",
            course_code=u"ROBOTS003",
            course_level='2',
            course_semester='1',
            credits='3',
            prerequisites=[
                RelationValue(intids.getId(ROBOTS001)),
            ]
        )
        wftool.doActionFor(ROBOTS003, 'publish')

        # Create course
        ROBOTS004 = createContentInContainer(
            portal['courses'],
            'collective.academicprogrammes.course',
            course_name=u"Robot Framework and Plone",
            course_code=u"ROBOTS004",
            course_level='3',
            course_semester='2',
            credits='4',
            prerequisites=[
                RelationValue(intids.getId(ROBOTS002)),
                RelationValue(intids.getId(ROBOTS003)),
            ]
        )
        wftool.doActionFor(ROBOTS004, 'publish')

        # Create course
        ROBOTS005 = createContentInContainer(
            portal['courses'],
            'collective.academicprogrammes.course',
            course_name=u"Robot Framework and Sphinx",
            course_code=u"ROBOTS005",
            course_level='3',
            course_semester='3',
            credits='2',
            prerequisites=[
                RelationValue(intids.getId(ROBOTS002)),
                RelationValue(intids.getId(ROBOTS003)),
            ]
        )
        wftool.doActionFor(ROBOTS005, 'publish')

        # Create group
        createContentInContainer(
            portal,
            'collective.academicprogrammes.coursegroup',
            title=u"All Robot Framework Courses",
            description=u"All courses available about Robot Framework",
            courses=[
                RelationValue(intids.getId(ROBOTS001)),
                RelationValue(intids.getId(ROBOTS002)),
                RelationValue(intids.getId(ROBOTS003)),
                RelationValue(intids.getId(ROBOTS004)),
                RelationValue(intids.getId(ROBOTS005))
            ]
        )

        # Create programme
        programme = createContentInContainer(
            portal,
            'collective.academicprogrammes.programme',
            title=u"Master of Robot Framework",
            description=u"Learn everything and become master",
            details=RichTextValue(
                raw=u"<p>PS. This is cool stuff!</p>",
                mimeType='text/html',
                outputMimeType='text/x-html-safe',
                encoding='utf-8'
            ),
            courses=[
                RelationValue(intids.getId(ROBOTS001)),
                RelationValue(intids.getId(ROBOTS002)),
                RelationValue(intids.getId(ROBOTS003)),
                RelationValue(intids.getId(ROBOTS004)),
                RelationValue(intids.getId(ROBOTS005))
            ]
        )
        wftool.doActionFor(programme, 'publish')

        setRoles(portal, TEST_USER_ID, TEST_USER_ROLES)

ACADEMIC_PROGRAMMES_ACCEPTANCE_FIXTURE =\
    CollectiveAcademicProgrammesAcceptanceLayer()

ACADEMIC_PROGRAMMES_ROBOT_TESTING = FunctionalTesting(
    bases=(ACADEMIC_PROGRAMMES_ACCEPTANCE_FIXTURE,
           REMOTE_LIBRARY_BUNDLE_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name='CollectiveAcademicProgrammes:Robot')
