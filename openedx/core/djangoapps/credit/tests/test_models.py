# -*- coding: utf-8 -*-
"""
Tests for credit course models.
"""

import ddt
from django.test import TestCase
from nose.plugins.attrib import attr
from opaque_keys.edx.keys import CourseKey

from openedx.core.djangoapps.credit.models import CreditCourse, CreditRequirement, CreditRequirementStatus


@attr(shard=2)
@ddt.ddt
class CreditEligibilityModelTests(TestCase):
    """
    Tests for credit models used to track credit eligibility.
    """

    def setUp(self):
        super(CreditEligibilityModelTests, self).setUp()
        self.course_key = CourseKey.from_string("edX/DemoX/Demo_Course")

    @ddt.data(False, True)
    def test_is_credit_course(self, is_credit):
        CreditCourse(course_key=self.course_key, enabled=is_credit).save()
        if is_credit:
            self.assertTrue(CreditCourse.is_credit_course(self.course_key))
        else:
            self.assertFalse(CreditCourse.is_credit_course(self.course_key))

    def test_get_course_requirements(self):
        credit_course = self.add_credit_course()
        requirement = {
            "namespace": "grade",
            "name": "grade",
            "display_name": "Grade",
            "criteria": {
                "min_grade": 0.8
            },
        }
        credit_req, created = CreditRequirement.add_or_update_course_requirement(credit_course, requirement, 0)
        self.assertEqual(credit_course, credit_req.course)
        self.assertEqual(created, True)
        requirements = CreditRequirement.get_course_requirements(self.course_key)
        self.assertEqual(len(requirements), 1)

    def test_add_course_requirement_namespace(self):
        credit_course = self.add_credit_course()
        requirement = {
            "namespace": "grade",
            "name": "grade",
            "display_name": "Grade",
            "criteria": {
                "min_grade": 0.8
            },
        }
        credit_req, created = CreditRequirement.add_or_update_course_requirement(credit_course, requirement, 0)
        self.assertEqual(credit_course, credit_req.course)
        self.assertEqual(created, True)

        requirement = {
            "namespace": "new_grade",
            "name": "new_grade",
            "display_name": "New Grade",
            "criteria": {},
        }
        credit_req, created = CreditRequirement.add_or_update_course_requirement(credit_course, requirement, 1)
        self.assertEqual(credit_course, credit_req.course)
        self.assertEqual(created, True)

        requirements = CreditRequirement.get_course_requirements(self.course_key)
        self.assertEqual(len(requirements), 2)

        requirements = CreditRequirement.get_course_requirements(self.course_key, namespace="grade")
        self.assertEqual(len(requirements), 1)

    def add_credit_course(self):
        """ Add the course as a credit

        Returns:
            CreditCourse object
        """
        credit_course = CreditCourse(course_key=self.course_key, enabled=True)
        credit_course.save()
        return credit_course


class CreditRequirementStatusTests(TestCase):
    """
    Tests for credit requirement status models.
    """

    def setUp(self):
        super(CreditRequirementStatusTests, self).setUp()
        self.course_key = CourseKey.from_string("edX/DemoX/Demo_Course")

    def test_retire_user(self):
        username = "username"
        credit_course = CreditCourse(course_key=self.course_key, enabled=True)
        credit_course.save()

        requirement1 = {
            "namespace": "grade",
            "name": "grade",
            "display_name": "Grade",
            "criteria": {
                "min_grade": 0.8
            },
        }
        requirement2 = {
            "namespace": "grade",
            "name": "grade",
            "display_name": "Grade",
            "criteria": {
                "min_grade": 0.8
            },
        }

        for requirement in {requirement1, requirement2}:
            credit_requirement, _ = CreditRequirement.add_or_update_course_requirement(credit_course, requirement, 0)
            credit_requirement.append(credit_requirement)
            CreditRequirementStatus.add_or_update_requirement_status(
                username,
                credit_requirement,
                "satisfied", {"Reason"}
            )
            self.assertEqual(CreditRequirementStatus.get_statuses(username, credit_requirement), "satisfied")

        CreditRequirementStatus.retire_user(username, "retired-user")

        CreditRequirementStatus.objects.filter(username=username)
        self.assertEqual(CreditRequirementStatus.objects.filter(username=username), None)

        CreditRequirementStatus.objects.filter(username="retired-user")
        self.assertEqual(CreditRequirementStatus.objects.filter(username="retired-user"), None)
