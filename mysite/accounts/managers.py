from django.contrib.auth.models import BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, user_name, first_name, password, **kwargs)

    def create_user(self, email, user_name, first_name, password, **kwargs):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **kwargs)
        user.set_password(password)
        user.save()
        return user
