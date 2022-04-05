from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
def profile_image_filepath(self, filename):
  return 'profile_images/' + str(self.pk) + '/profile_image.png'
def get_default_profile_image():
  return "default_image/Tse.png"
class MyAccountManagaer(BaseUserManager):
  def create_user(self, email, username, password=None):
    if not email:
      raise ValueError("Users must have an email address")
    if not username:
      raise ValueError("Users must have username")
    user = self.model(
      email = self.normalize_email(email),
      username = username
    )
    user.set_password(password)
    user.save(using = self.db)
    return user
  def create_superuser(self, email, username, password):
    user = self.create_user(
      email= self.normalize_email(email),
      username= username,
      password=password,
    )
    user.is_admin = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using = self.db)
    return user
class Account(AbstractUser):
  email = models.EmailField(verbose_name="Email",max_length=60, unique=True)
  username = models.CharField(max_length=30, unique=True)
  date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
  last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False) 
  is_superuser = models.BooleanField(default=False)
  profile_image = models.ImageField(max_length=255,
   upload_to=profile_image_filepath,null=True,blank=True,
    default=get_default_profile_image())
  hide_email = models.BooleanField(default=True)
  objects = MyAccountManagaer()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  def get_profile_image_filename(self):
    return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]
  def __str__(self):
    return self.username + self.email
  def has_perm(self, perm, obj=None):
    return self.is_admin
  def has_module_perms(self, app_label):
    return True
class Event(models.Model):
  name = models.CharField(max_length=32, null=False)
  description = models.TextField(max_length=300, null=False)
  schedule_date = models.DateTimeField(verbose_name="schedule date", null=False)
  def __str__(self):
    return self.name
class Attendance(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  def __str__(self):
    return str(self.event) + " " + str(self.account)
