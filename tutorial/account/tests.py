from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user or get the existing user
        user, created = User.objects.get_or_create(
            username='myusername',
            password='mypassword'
        )

        # Create a profile associated with the user
        profile, created = Profile.objects.get_or_create(user=user)
        
        # Save the profile to the instance to use in the tests
        cls.profile = profile
        
    def test_profile_str(self):
        profile = Profile.objects.get(id=self.profile.id)
        expected_str = f'{profile.user.username} Profile'
        self.assertEqual(str(profile), expected_str)

    def test_profile_image_upload(self):
        profile = Profile.objects.get(id=self.profile.id)
        profile.image = 'profile_pics/default.jpg'
        self.assertTrue(profile.image.name.startswith('profile_pics/'))


    @classmethod
    def tearDownClass(cls):
        Profile.objects.all().delete()
        User.objects.all().delete()