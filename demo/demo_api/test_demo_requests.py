"""Exercise on Request Library"""
import json

import requests
from assertpy import assert_that


class TestPetStoreAPI:
    base_url = "https://petstore.swagger.io/v2"
    pet_id = 0

    def test_add_valid_pet(self):
        resource = "/pet"
        request_body = json.load(open("test_data/add_pet.json"))
        header = {'Content-Type': 'application/json'}
        response = requests.post(url=TestPetStoreAPI.base_url + resource, json=request_body, headers=header)
        assert_that(200).is_equal_to(response.status_code)
        response_body = response.json()
        assert_that('test_pet').is_equal_to(response_body['name'])
        assert_that('pet').is_equal_to(response_body['category']['name'])
        TestPetStoreAPI.pet_id = response_body['id']

    def test_get_valid_pet_id(self):
        resource = "/pet/" + str(TestPetStoreAPI.pet_id)
        response = requests.get(TestPetStoreAPI.base_url + resource)
        assert_that(200).is_equal_to(response.status_code)
        response_body = response.json()
        assert_that(TestPetStoreAPI.pet_id).is_equal_to(response_body['id'])
        assert_that('test_pet').is_equal_to(response_body['name'])
        assert_that('pet').is_equal_to(response_body['category']['name'])

    def test_get_non_existing_pet_id(self):
        resource = "/pet/99999999"
        response = requests.get(TestPetStoreAPI.base_url + resource)
        assert_that(404).is_equal_to(response.status_code)

    def test_get_valid_pet_by_status(self):
        status = 'available'
        resource = "/pet/findByStatus?status=" + status
        response = requests.get(TestPetStoreAPI.base_url + resource)
        assert_that(200).is_equal_to(response.status_code)
        response_body = response.json()
        for pet in response_body:
            assert_that(status).is_equal_to(pet['status'])

    def test_update_valid_pet(self):
        resource = "/pet"
        request_body = json.load(open("test_data/update_pet.json"))
        request_body['id'] = TestPetStoreAPI.pet_id
        header = {'Content-Type': 'application/json'}
        response = requests.put(url=TestPetStoreAPI.base_url + resource, json=request_body, headers=header)
        assert_that(200).is_equal_to(response.status_code)
        response_body = response.json()
        assert_that('updated_test_pet').is_equal_to(response_body['name'])
        assert_that('updated_pet_category_name').is_equal_to(response_body['category']['name'])
        assert_that('updated_tag_name').is_equal_to(response_body['tags'][0]['name'])
        assert_that('Updated_url').is_equal_to(response_body['photoUrls'][0])
        assert_that('sold').is_equal_to(response_body['status'])

    def test_delete_valid_pet(self):
        resource = "/pet/" + str(TestPetStoreAPI.pet_id)
        response = requests.delete(TestPetStoreAPI.base_url + resource)
        assert_that(200).is_equal_to(response.status_code)
