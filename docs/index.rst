collective.academicprogrammes
=============================

.. include:: robot.rst

This is how your programme might look to your visitors:

.. figure:: programme.png
.. code:: robotframework

   Show programme
      Go to  ${PLONE_URL}/master-of-robot-framework

      Capture page screenshot  programme.png

And this is how it might look to your editors:

.. figure:: programme-edit.png
.. code:: robotframework

   Show programme edit
      Enable autologin as  Manager
      Go to  ${PLONE_URL}/master-of-robot-framework/@@edit

      Capture and crop page screenshot
      ...  programme-edit.png  css=#content

      Disable autologin
