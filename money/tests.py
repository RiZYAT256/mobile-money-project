from types import SimpleNamespace

from django.contrib.auth.models import AnonymousUser, User
from django.template.loader import render_to_string
from django.test import Client, RequestFactory, SimpleTestCase, TestCase, override_settings
from money.models import Agent, Customer
from money.views import index_view


@override_settings(
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class BaseNavigationTests(SimpleTestCase):
    def test_dashboard_redirects_anonymous_users_to_login(self):
        request = RequestFactory().get("/")
        request.user = AnonymousUser()

        response = index_view(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/login/?next=/")

    def test_root_displays_login_before_dashboard_for_anonymous_users(self):
        response = Client().get("/", follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [("/login/?next=/", 302)])
        self.assertContains(response, "Login")

    def test_authenticated_navigation_uses_application_urls(self):
        user = SimpleNamespace(
            is_authenticated=True,
            username="tester",
            first_name="",
        )
        request = RequestFactory().get("/")
        request.user = user

        response = index_view(request)
        html = response.content.decode()

        for path in (
            "/",
            "/money_list/",
            "/deposit/",
            "/withdraw/",
            "/transfer/",
            "/add_agent/",
            "/add_customer/",
        ):
            with self.subTest(path=path):
                self.assertIn(f'href="{path}"', html)
        self.assertIn('action="/logout/"', html)
        self.assertIn("Great to have you back", html)
        self.assertNotIn('href="dashboard.html"', html)
        self.assertNotIn("Today's Money", html)

    def test_anonymous_navigation_links_to_sign_in_and_sign_up(self):
        html = render_to_string("index.html", {"user": AnonymousUser()})

        self.assertIn('href="/login/"', html)
        self.assertIn('href="/signup/"', html)
        self.assertNotIn('action="/logout/"', html)

    def test_login_layout_hides_dashboard_activity_links_for_anonymous_users(self):
        html = render_to_string("base.html", {"user": AnonymousUser()})

        for path in (
            "/money_list/",
            "/deposit/",
            "/withdraw/",
            "/transfer/",
            "/add_agent/",
            "/add_customer/",
        ):
            with self.subTest(path=path):
                self.assertNotIn(f'href="{path}"', html)
        self.assertIn('href="/login/"', html)

    def test_login_and_signup_pages_render_with_shared_layout(self):
        login_html = render_to_string(
            "registration/login.html",
            {"user": AnonymousUser()},
        )
        signup_html = render_to_string(
            "registration/sign_up.html",
            {"user": AnonymousUser()},
        )

        self.assertIn("Mobile Money", login_html)
        self.assertIn("Mobile Money", signup_html)


@override_settings(
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class MoneyListTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="money-list-test", password="test-password")
        self.client = Client()
        self.client.force_login(user)
        self.agent = Agent.objects.create(
            name="Test Agent",
            phone_number="0700000000",
            location="Test",
        )
        self.sender = Customer.objects.create(
            name="Sender",
            phone_number="0711111111",
        )
        self.receiver = Customer.objects.create(
            name="Receiver",
            phone_number="0722222222",
        )

    def test_money_list_includes_saved_deposits_withdrawals_and_transfers(self):
        deposit_response = self.client.post(
            "/deposit/",
            {"customer": self.sender.pk, "agent": self.agent.pk, "amount": "100.00"},
        )
        withdraw_response = self.client.post(
            "/withdraw/",
            {"customer": self.sender.pk, "agent": self.agent.pk, "amount": "25.00"},
        )
        transfer_response = self.client.post(
            "/transfer/",
            {
                "sender": self.sender.pk,
                "receiver": self.receiver.pk,
                "amount": "50.00",
            },
        )

        self.assertContains(deposit_response, "Deposit Successful")
        self.assertContains(withdraw_response, "Withdraw Successful")
        self.assertContains(transfer_response, "Successful")

        response = self.client.get("/money_list/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deposit")
        self.assertContains(response, "Withdraw")
        self.assertContains(response, "Transfer")
        self.assertContains(response, "<th>Sender</th>")
        self.assertContains(response, "<th>Receiver</th>")
        self.assertContains(response, "Sender")
        self.assertContains(response, "Receiver")
        self.assertContains(response, "100.00")
        self.assertContains(response, "25.00")
        self.assertContains(response, "50.00")
