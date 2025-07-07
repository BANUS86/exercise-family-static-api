"""
This file contains the FamilyStructure class to manage the Jackson family.
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": 92736207,
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 58199304,
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 94141980,
                "first_name": "Jimy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        for i, m in enumerate(self._members):
            if m["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    def get_all_members(self):
        return self._members