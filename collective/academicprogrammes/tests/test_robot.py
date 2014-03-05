# -*- coding: utf-8 -*-
import unittest

import robotsuite
from plone.testing import layered

from collective.academicprogrammes.testing import \
    ACADEMIC_PROGRAMMES_ROBOT_TESTING


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite('acceptance'),
                layer=ACADEMIC_PROGRAMMES_ROBOT_TESTING),
    ])
    return suite