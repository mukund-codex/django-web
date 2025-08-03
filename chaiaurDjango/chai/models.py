from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    decscription = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

# One to Many Relationship with User
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.username} for {self.chai.name} - Rating: {self.rating}'

# Many to Many Relationship with User
class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name
    

# One to One Relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100, unique=True)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name} - Number: {self.certificate_number}'

