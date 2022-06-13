from django.test import TestCase

from .models import *

# Create your tests here.
class PostTestClass(TestCase):
    def setUp(self):
        self.profile = Profile('8',first_name='isaac',last_name='kiptoo',proc_img='isaac.png',bio='am i a tm',email='isaac@gmail',contacts='0712345678')
        self.profile.save_profile()

        self.rate = Rate(scores='10')
        self.rate.save_rate()

        self.initial_test= Post(title='creativity',user='isaac',url='',technologies = 'django/python',post_img='isaac.png',  description='the image is in good condition',created_at='25-04-2022',profile=self.profile,rate=self.rate)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.initial_test,Post))

    # Testing the saved methods
    def test_saved_method(self):
        self.initial_test.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)



    def test_delete_post(self):
        self.initial_test.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)==0)

    def test_update_post(self):
        self.initial_test.save_post()
        self.initial_test.update_post(self.initial_test.id, 'images/test.jpg')
        new_post = Post.objects.filter(post='images/test.jpg')
        self.assertTrue(len(new_post)>0)

    def test_search_by_title(self):
        self.initial_test.save_post()
        posts = self.initial_test.search_by_title(search_term='creativity')
        self.assertTrue(len(posts) ==0)



    def tearDown(self):
        Post.objects.all().delete()
        Profile.objects.all().delete()
        Rate.objects.all().delete()

class RateTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rate = Rate(scores='10')
        self.rate.save_rate()

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rate))

    def test_save_rate(self):
        self.rate.save_rate()
        rates = Rate.objects.all()
        self.assertTrue(len(rates) > 0)

    def test_delete_rate(self):
        self.rate.delete_rate()
        rate = Rate.objects.all()
        self.assertTrue(len(rate) == 0)


   
    
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.profile = Profile('3',first_name='isaac',last_name='kiptoo',proc_img='isaac.png',bio='am i a tm',email='isaac@gmail',contacts='0712345678')
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profiless = Profile.objects.all()
        self.assertTrue(len(profiless) == 0)

    
