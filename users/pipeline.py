import urllib
from urllib import urlopen
from django.core.files.base import ContentFile
from .models import Profile
from datetime import datetime
import datetime

def update_user_social_data(strategy, *args, **kwargs):
    # if not kwargs['is_new']:
    #     return
    full_name = ''
    backend = kwargs['backend']
    # backend.__class__.__name__
    
    if backend.name == 'facebook':
        user = kwargs['user']
        pk=user.id
        # print user
        full_name = kwargs['response'].get('name')
        # user.full_name = full_name
        # print full_name
        email = kwargs['response'].get('email')
        # user.email = email
        birthday = kwargs['response'].get('birthday')
        # user.birthday = birthday
        dob = datetime.datetime.strptime("09/20/1995", "%m/%d/%Y").strftime("%Y-%m-%d")
        fbuid = kwargs['response']['id']
        image_name = 'fb_avatar_%s.jpg' % fbuid
        image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
        image_stream = urlopen(image_url)
        user.save()
        create_data = Profile.objects.filter(user_id=pk)
        if not create_data:
            data = Profile.objects.create(user_id=pk,birthday=dob,full_name=full_name,image_url=image_url,provider=backend.name).save()
        else:
            pass







# def get_avatar(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     url = None
#     if backend.name == 'FacebookOAuth2':
#         url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
#     if backend.name == 'twitter':
#         url = response.get('profile_image_url', '').replace('_normal','')
#     if backend.name == 'google-oauth2':
#         url = response['image'].get('url')
#         ext = url.split('.')[-1]
#     if url:
#         user.avatar = url
#         user.save()

# from django.contrib.auth.models import User

# def save_profile_picture(backend, user, response, details,is_new=False,*args,**kwargs):
#     print response['id']
#     if backend.__class__.__name__ == 'FacebookOAuth2':
#         up = User.objects.get_or_create(username=user.id) #RETURNS TUPLE (instance, created(boolean))
#         if not up[0].photo:
#             url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
#             response = urllib.request.urlopen(url)
#             io = BytesIO(response.read())
#             up[0].photo.save('profile_pic_{}.jpg'.format(user.pk), File(io))
#             up[0].save()

# def update_user_social_data(strategy, *args, **kwargs):
    
#     # print 'update_user_social_data ::', strategy
#     # if not kwargs['is_new']:
#     #     return

#     full_name = ''
#     backend = kwargs['backend']
#     print backend

#     user = kwargs['user']

#     if (
#         # isinstance(backend, GoogleOAuth2)
#         or isinstance(backend, FacebookOAuth2)
#     ):
#         full_name = kwargs['response'].get('name')
#     elif (
#         # isinstance(backend, LinkedinOAuth)
#         or isinstance(backend, TwitterOAuth)
#     ):
#         if kwargs.get('details'):
#             full_name = kwargs['details'].get('fullname')

#     user.full_name = full_name

#     if isinstance(backend, GoogleOAuth2):
#         if response.get('image') and response['image'].get('url'):
#             url = response['image'].get('url')
#             ext = url.split('.')[-1]
#             user.avatar.save(
#                '{0}.{1}'.format('avatar', ext),
#                ContentFile(urllib2.urlopen(url).read()),
#                save=False
#             )
#     elif isinstance(backend, FacebookOAuth2):
#         fbuid = kwargs['response']['id']
#         image_name = 'fb_avatar_%s.jpg' % fbuid
#         image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
#         image_stream = urlopen(image_url)
#         print image_name
#         print image_url

#         user.avatar.save(
#             image_name,
#             ContentFile(image_stream.read()),
#         )
#     elif isinstance(backend, TwitterOAuth):
#         if kwargs['response'].get('profile_image_url'):
#             image_name = 'tw_avatar_%s.jpg' % full_name
#             image_url = kwargs['response'].get['profile_image_url']
#             image_stream = urlopen(image_url)

#             user.avatar.save(
#                 image_name,
#                 ContentFile(image_stream.read()),
#             )
#     elif isinstance(backend, LinkedinOAuth):
#         if kwargs['response'].get('pictureUrl'):
#             image_name = 'linked_avatar_%s.jpg' % full_name
#             image_url = kwargs['response'].get['pictureUrl']
#             image_stream = urlopen(image_url)

#             user.avatar.save(
#                 image_name,
#                 ContentFile(image_stream.read()),
#             )
#     user.save()