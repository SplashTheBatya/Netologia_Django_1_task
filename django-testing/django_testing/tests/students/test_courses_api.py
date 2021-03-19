import pytest
from django.urls import reverse
from rest_framework.status import *

from students.models import *


@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    # arrange
    course = course_factory()
    url = reverse('courses-detail', args=(course.id,))

    # act
    resp = api_client.get(url)

    # assert
    assert resp.status_code == HTTP_200_OK
    assert resp.json()["id"] == course.id


@pytest.mark.django_db
def test_get_courses_list(api_client, course_factory):
    # arrange
    course1 = course_factory()
    course2 = course_factory()
    url = reverse('courses-list')

    # act
    resp = api_client.get(url)

    # assert
    assert resp.status_code == HTTP_200_OK

    resp_json = resp.json()
    assert len(resp_json) == 2

    resp_ids = {r["id"] for r in resp_json}
    assert resp_ids == {course1.id, course2.id}


@pytest.mark.django_db
def test_sort_courses_by_id(api_client, course_factory):
    # arrange
    url = reverse('courses-list')
    course1 = course_factory()
    course2 = course_factory()
    course3 = course_factory()

    # act
    resp = api_client.get(url)
    sorted_coursers = {course1.id, course2.id, course3.id}

    # assert
    assert resp.status_code == HTTP_200_OK

    resp_json = resp.json()
    resp_ids = {r["id"] for r in resp_json}
    assert resp_ids == sorted_coursers


@pytest.mark.django_db
def test_sort_courses_by_name(api_client, course_factory):
    # arrange
    url = reverse('courses-list')
    course1 = course_factory(name='Python')
    course2 = course_factory(name='Java')
    course3 = course_factory(name='C++')

    # act
    resp = api_client.get(url)
    sorted_courses = {course3.name, course2.name, course1.name}

    # assert
    assert resp.status_code == HTTP_200_OK

    resp_json = resp.json()
    resp_ids = {r["name"] for r in resp_json}
    assert resp_ids == sorted_courses


@pytest.mark.django_db
def test_post_course(api_client):
    # arrange
    url = reverse('courses-list')
    payload = {
        "name": "New Course"
    }

    # act
    courses_count = Course.objects.count()
    resp = api_client.post(url, payload, format="json")

    # assert
    assert resp.status_code == HTTP_201_CREATED
    assert Course.objects.count() > courses_count


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    # arrange
    course = course_factory()
    url = reverse('courses-detail', args=(course.id,))
    payload = {
        "name": "New Course"
    }

    # act
    resp = api_client.patch(url, payload, format="json")
    resp_json = resp.json()
    expected_name = payload["name"]

    # assert
    assert resp.status_code == HTTP_200_OK
    assert resp_json["name"] == expected_name


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    # arrange
    course = course_factory()
    url = reverse('courses-detail', args=(course.id,))

    # act
    resp = api_client.delete(url)

    # assert
    assert resp.status_code == HTTP_204_NO_CONTENT
