from django.core.management.base import BaseCommand
from blog.models import Post 
from users.models import User


class Command(BaseCommand):
    help = "Populate database with sample data"
    
    def handle(self, *args, **kwargs):
        self.stdout.write(
            self.style.SUCCESS("Populate command is running...")
        )
        
        # Create Users 
        
        admin_user, created = User.objects.get_or_create(
            username='admin_user',
            defaults={
                'role':'admin',
                'email':'admin@gmail.com'
            }
        )
        
        if created:
            admin_user.set_password('admin123')
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.save()
            
            
        
        author1 , created = User.objects.get_or_create(
            username = 'author1',
            defaults= {
                'role':'author',
                'email':'author1@gmail.com'
            }
        )
        
        if created:
            author1.set_password('author1234')
            author1.save()
            
        
        author2 , created = User.objects.get_or_create(
            username = 'author2',
            defaults= {
                'role':'author',
                'email':'author2@gmail.com'
            }
        )
        
        if created:
            author1.set_password('ayomide123')
            author1.save()
            
            
        
        reader1, created = User.objects.get_or_create(
            username='reader1',
            defaults={
                'role':'reader',
                'email':'reader1@fgmail.com'
            }
        )
        
        if created:
            reader1.set_password('reader1234')
            reader1.save()
        
        
        # Create the sample Post
        
        Post.objects.get_or_create(
            title = 'Title of the Sample Post',
            defaults ={
                'description':'Description of the sample post',
                'content':'Content of the Sample Post',
                'owner':author1
            }
        )    
        
        
        self.stdout.write(
            self.style.SUCCESS('Data populated successfuly!')
        )
    
    
            
        



