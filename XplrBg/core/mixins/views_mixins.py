from django.contrib.auth.mixins import UserPassesTestMixin


class AuthorizationRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
