*** Settings ***

Resource  plone/app/robotframework/selenium.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Scenario: As an editor I add course to a programme
    Given a site owner
      and a course
      and a programme
     When I edit the programme
      and I select the course into its courses
     Then I can view the course in the programme

*** Variables ***

${CONTENTVIEW_EDIT_LINK}  css=#contentview-edit a
${COURSES_FIELD_WIDGETS}  css=#formfield-form-widgets-courses
${COURSES_CONTENTTREE}  css=#form-widgets-courses-contenttree

*** Keywords ***

# Given

A site owner
    Enable autologin as  Site Administrator

A course
    Create content
    ...  type=collective.academicprogrammes.course
    ...  container=/${PLONE_SITE_ID}/courses  id=new-course
    ...  course_name=New Course
    ...  course_code=001
    ...  course_level=1

A programme
    Create content
    ...  type=collective.academicprogrammes.programme
    ...  id=new-programme  title=New Programme

# When

I edit the programme
    Go to  ${PLONE_URL}/new-programme
    Element should be visible  ${CONTENTVIEW_EDIT_LINK}

    Click link  ${CONTENTVIEW_EDIT_LINK}
    Page should contain element  css=body.template-edit

I select the course into its courses
    Element should be visible  ${COURSES_FIELD_WIDGETS}

    Click Element  ${COURSES_FIELD_WIDGETS} .searchButton
    Wait until element is visible
    ...  ${COURSES_CONTENTTREE} a[href$='/plone/courses']
    Click Element  ${COURSES_CONTENTTREE} a[href$='/plone/courses']

    Wait until element is visible
    ...  ${COURSES_CONTENTTREE} a[href$='/plone/courses/new-course']
    Click Element  ${COURSES_CONTENTTREE} a[href$='/plone/courses/new-course']

    Click Element  css=.contentTreeAdd
    Element should not be visible  ${COURSES_CONTENTTREE}
    Element should contain  ${COURSES_FIELD_WIDGETS}  001 New Course

    Click button  css=#form-buttons-save
    Page should not contain element  css=body.template-edit

# Then

I can view the course in the programme
    Go to  ${PLONE_URL}/new-programme
    Element should contain  css=#content-core  001 New Course
