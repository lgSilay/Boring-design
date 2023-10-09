from django.test import TestCase
from django.urls import reverse

from app.forms import CommentForm
from app.models import Style, Project, Picture, User, Commentary

PROJECT_LIST_URL = reverse("app:projects_list")


class ModelsTest(TestCase):
    def test_style_name(self):
        style = Style.objects.create(name="Style 1")
        self.assertEqual(str(style), "Style 1")

    def test_project_name(self):
        project = Project.objects.create(name="Project 1")
        self.assertEqual(str(project), "Project 1")

    def test_picture_name(self):
        project = Project.objects.create(name="Project 1")
        picture = Picture.objects.create(
            name="Picture 1",
            project=project,
            image="image1.jpg"
        )
        self.assertEqual(str(picture), "Picture 1")


class ProjectDetailViewTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name="Test Project", description="Test Description")

        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_project_detail_view_with_get_request(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("app:projects_detail", args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context["form"], CommentForm))
        self.assertEqual(response.context["project"], self.project)

    def test_project_detail_view_with_post_request_authenticated_user(self):
        self.client.login(username="testuser", password="testpassword")
        post_data = {
            "content": "Test Comment",
            "user": self.user.id,
            "project": self.project.id
        }
        response = self.client.post(reverse("app:projects_detail", args=[self.project.id]), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Commentary.objects.count(), 1)

    def test_project_detail_view_with_post_request_anonymous_user(self):
        post_data = {
            "content": "Test Comment",
            "user": self.user.id,
            "project": self.project.id
        }
        response = self.client.post(reverse("app:projects_detail", args=[self.project.id]), data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "content", "Please log in to add a comment")

    def test_project_detail_view_with_invalid_post_data(self):
        self.client.login(username="testuser", password="testpassword")
        post_data = {"content": ""}
        response = self.client.post(reverse("app:projects_detail", args=[self.project.id]), data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "content", "This field is required.")


class ProjectsFilteredListViewTest(TestCase):
    def setUp(self):
        self.style1 = Style.objects.create(name="Style 1")
        self.style2 = Style.objects.create(name="Style 2")

        self.project1 = Project.objects.create(
            name="Project 1",
            description="Description 1",
        )
        self.project1.style.add(self.style1)

        self.project2 = Project.objects.create(
            name="Project 2",
            description="Description 2"
        )
        self.project2.style.add(self.style2)

        self.picture1 = Picture.objects.create(name="Picture 1", project=self.project1)
        self.picture2 = Picture.objects.create(name="Picture 2", project=self.project2)

        self.user = User.objects.create_user(username="testuser", password="testpassword")

        self.comment1 = Commentary.objects.create(content="Comment 1", user=self.user, project=self.project1)
        self.comment2 = Commentary.objects.create(content="Comment 2", user=self.user, project=self.project2)
