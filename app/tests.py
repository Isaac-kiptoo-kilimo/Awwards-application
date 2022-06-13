from django.test import TestCase



from .models import *

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(first_name='isaac',last_name='kiptoo',proc_img='isaac.png',bio='am i a tm',email='isaac@gmail',contacts='0712345678')
        self.profile.save_profile()


    #  title=models.CharField(max_length=100, null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts",null=True,blank=True)
    # url = models.URLField(max_length=255,null=True,blank=True)
    # technologies = models.CharField(max_length=200, blank=True)
    # post_img=CloudinaryField('post_img')
    # description=models.TextField(null=False)
    # created_at=models.DateTimeField(auto_now_add=True)

        self.comment = Rate(rate='10')
        self.comment.save_rate()

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
        self.comment = comment=('Fruits')
        self.comment.save_comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.comment.delete_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment) == 0)


   
    
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.profile = Profile(fullname='isaac kiptoo',profile_img='isaac.png',bio='am i a tm',email_phone='isaac@gmail',followers='2')
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

    
