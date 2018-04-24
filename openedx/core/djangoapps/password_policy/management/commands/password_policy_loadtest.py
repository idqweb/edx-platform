from __future__ import print_function

from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

from openedx.core.djangoapps.password_policy.constants import PASSWORD_POLICY_COMPLIANT_USERS_GROUP_NAME


class Command(BaseCommand):
    """
    Management command to setup the environment for load-testing the password policy enforcement logic.
    """

    # The maximim number of user IDs to grab per query and add to group.user_set.
    MAX_SLICE_SIZE = 100000

    def add_arguments(self, parser):
        parser.add_argument('--mode', choices=['setup', 'cleanup'], required=True)
        parser.add_argument('--target-member-count', type=int, default=1000000)

    def handle(self, *args, **options):
        mode = options['mode']
        if mode == 'setup':
            self.run_setup(options['target_member_count'])
        elif mode == 'cleanup':
            self.run_cleanup()
        else:
            raise Exception('Invalid mode: {}'.format(mode))

    def run_setup(self, target_member_count):
        print('Starting setup for password policy loadtest')

        group = Group.objects.get(name=PASSWORD_POLICY_COMPLIANT_USERS_GROUP_NAME)
        user_count = User.objects.count()

        target_count = min([user_count, target_member_count])
        print(
            'Attempting to bring the total membership of the {group_name} group to {count} users'.format(
                group_name=PASSWORD_POLICY_COMPLIANT_USERS_GROUP_NAME,
                count=target_count,
            )
        )

        current_count = 0
        last_id = 0
        while current_count < target_count:
            slice_size = min([target_count - current_count, self.MAX_SLICE_SIZE])
            ids = User.objects.filter(id__gt=last_id).order_by('id').values_list('id', flat=True)[:slice_size]
            if not ids:
                break

            group.user_set.add(*ids)
            last_id = ids[len(ids) - 1]
            current_count += len(ids)

        print(
                'Finished adding users to the {group_name} group. Final membership count: {count}'.format(
                group_name=PASSWORD_POLICY_COMPLIANT_USERS_GROUP_NAME,
                count=group.user_set.count()
            )
        )
        print('Finished setup for password policy loadtest')

    def run_cleanup(self):
        print('Starting cleanup for password policy loadtest')

        group = Group.objects.get(name=PASSWORD_POLICY_COMPLIANT_USERS_GROUP_NAME)
        group.user_set.clear()

        print(
            'Removed all users from the {group_name} group. Final membership count: {count}'.format(
                group_name=PASSWORD_POLICY_COMPLIANT_USERS_GROUP_NAME,
                count=group.user_set.count()
            )
        )
        print('Finished cleanup for password policy loadtest')
