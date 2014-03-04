.. code:: robotframework

   *** Settings ***

   Resource  plone/app/robotframework/server.robot
   Resource  Selenium2Screenshots/keywords.robot

   Suite Setup  Suite Setup
   Suite Teardown  Suite Teardown

   *** Keywords ***

   Suite Setup
       Setup Plone site
       ...  collective.academicprogrammes.testing.ACADEMIC_PROGRAMMES_ROBOT_TESTING
       Set window size  640  480
       Import library  Remote  ${PLONE_URL}/RobotRemote

   Suite Teardown
       Teardown Plone Site

   *** Test Cases ***
