# -*- coding: utf-8 -*-
import doctest
import unittest

from plone.testing import layered

from collective.academicprogrammes.testing import \
    ACADEMIC_PROGRAMMES_INTEGRATION_TESTING


OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('INTEGRATION.txt',
                                     package='collective.academicprogrammes',
                                     optionflags=OPTION_FLAGS),
                layer=ACADEMIC_PROGRAMMES_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('CourseGroup.txt',
                                     package='collective.academicprogrammes',
                                     optionflags=OPTION_FLAGS),
                layer=ACADEMIC_PROGRAMMES_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('Programme.txt',
                                     package='collective.academicprogrammes',
                                     optionflags=OPTION_FLAGS),
                layer=ACADEMIC_PROGRAMMES_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('Course.txt',
                                     package='collective.academicprogrammes',
                                     optionflags=OPTION_FLAGS),
                layer=ACADEMIC_PROGRAMMES_INTEGRATION_TESTING),
    ])
    return suite
