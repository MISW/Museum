from django.contrib.auth.mixins import UserPassesTestMixin

class OnlyAdminMixin(UserPassesTestMixin):
    raise_exception = False

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return user.is_admin
        else:
            return False

