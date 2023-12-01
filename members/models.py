from django.db import models


class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    portrait = models.ImageField(null=True, blank=True, upload_to="images/")
    role_choices = [('regular', 'Regular - Can\'t Delete Members'), ('admin', 'Admin - Can Delete Members')]
    role = models.CharField(max_length=10, choices=role_choices, default='regular')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def is_admin(self):
        """
        Checks if the current team member is an admin.

        :return: True if the team member is an admin, False otherwise.
        """
        return self.role == "admin"
