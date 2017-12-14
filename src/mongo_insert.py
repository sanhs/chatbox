
import sys
import pymongo
import random
from pprint import pprint
from copy import deepcopy


USER_NAME = 'vymo-lms'
PD = 'iQ1jhq8bYTFr8Ql4jDU4f88+NcMsxlkOkJJHI99GgdgVMG+s2KEXXSftEMGVd/WYy2dZmsHvrvuENlM8woKCoSDb9+zJsTV19YJx+OP9Uh27Sy6aqKWhN4VKaMIGCqb'
CONN_IP = '127.0.0.1'
CONN_PORT = 9999

DB_NAME = 'vymo-lms'
USER_COLLECTION_NAME = 'abtest_sugg_py'
CUST_COLLECTION_NAME = 'abtest_sugg_py'

USERS = 64
DATA = []
CUST_DATA = []

USER_DATA = {
    "inputs_map": {
        "role": "SRM",
        "operating_region": "North 1",
        "center": "sdfghjkl",
        "camscode": "1234567890"
    },
    "validated": {
        "phone": True,
        "email": False
    },
    "verification": {
        "phone_skip": 0,
        "email_skip": 0,
        "time": "2017-11-21T15:28:33.045Z"
    },
    "roles": [],
    "job_id": [
        "a25a5d40-ced0-11e7-aeb1-99a858e75a27",
        "b43dfc10-ced0-11e7-aeb1-99a858e75a27",
        "b43e4a30-ced0-11e7-aeb1-99a858e75a27",
        "e3bec820-ced0-11e7-aeb1-99a858e75a27",
        "e3beef30-ced0-11e7-aeb1-99a858e75a27",
        "d0d6e340-ced1-11e7-aeb1-99a858e75a27",
        "d0d70a50-ced1-11e7-aeb1-99a858e75a27",
        "4be2ac90-ced2-11e7-aeb1-99a858e75a27",
        "4be2d3a0-ced2-11e7-aeb1-99a858e75a27"
    ],
    "authenticate_constant": 1511278826967.0,
    "device_whitelist": [
        ""
    ],
    "disabled": False,
    "inputs": [
        {
            "value": "1234567890",
            "_id": "5a144621262b403e4a712fab",
            "name": "CAMSCODE",
            "code": "camscode",
            "type": "text"
        },
        {
            "value" : "sdfghjkl",
            "_id": "5a144621262b403e4a712fac",
            "name": "Center",
            "code": "center",
            "type": "text"
        },
        {
            "value": "North 1",
            "_id": "5a144621262b403e4a712fad",
            "name": "Region",
            "code": "operating_region",
            "type": "number"
        },
        {
            "value": "SRM",
            "_id": "5a144621262b403e4a712fae",
            "name": "Role",
            "code": "role",
            "type": "number"
        }
    ],
    "location_tag_codes": [],
    "salt": "BdRQ1LmyLiLKJaEj2IWh6A==",
    "hashed_password": "r1/JZLCG7UExDmhtWSesqpG3Mla/tbYLtCzANX9YlXUd/szDvcCj0nl+hyCzfC/L4OGO2ECMhy2ADk19FdCabg==",
    "region_hierarchy": [
        "all",
        "13",
        "vymo008",
        "12345678"
    ],
    "region_type": "branch",
    "region": "12345678",
    "phone": "+919971272523",
    "email": "michael@pbg.com",
    "name": "Michael Corleone",
    "code": "12345678",
    "date": "2017-11-21T15:28:33.044Z",
    "__v": 4,
    "lead_module_versions": {
        "activity_new": 108,
        "new": 2
    }
}

CUSTOMER_DATA = {
  "_id": "57d2c15bdd50a5547eeee9dd",
  "region_hierarchy": {
    "S4379": False,
    "A11888": "S4379",
    "S0971": "A11888",
    "N0305": "S0971",
    "VY0001": "N0305",
    "all": "VY0001"
  },
  "inputs_map": {
    "cust_id": "672248900315",
    "name": "MARK RODRIGUES",
    "address1": "4 GRETA STREET GLENVIEW   HAMILTON",
    "address2": ".",
    "address3": ".",
    "city": ".",
    "state": "X",
    "pincode": "3206",
    "email": "crystalisland@gmail.com",
    "phone": "64210431756",
    "emp_code": "S4379",
    "emp_name": "SILVESTRE PEREIRA",
    "location": "{\"latitude\":-37.8203253,\"longitude\":175.2878325}"
  },
  "updates_inputs_map": {
    "customer": {
      "location": {
        "longitude": 175.2878325,
        "latitude": -37.8203253
      },
      "emp_name": "SILVESTRE PEREIRA",
      "emp_code": "S4379",
      "phone": "64210431756",
      "email": "crystalisland@gmail.com",
      "pincode": "3206",
      "state": "Ontario",
      "city": "HAMILTON",
      "address3": ".",
      "address2": ".",
      "address1": "4 GRETA STREET GLENVIEW",
      "name": "MARK RODRIGUES",
      "cust_id": "672248900315"
    }
  },
  "first_update_type": "customer",
  "last_update_date": "2017-04-11T09:04:00.325Z",
  "assigned_by": {
    "name": "SILVESTRE PEREIRA",
    "code": "S4379"
  },
  "created_by": {
    "code": "S4379",
    "name": "SILVESTRE PEREIRA"
  },
  "deleted": False,
  "exported": False,
  "reactivated": False,
  "source": "web",
  "has_meeting": False,
  "can_update": False,
  "last_update_type": "customer",
  "updates": [
    {
      "event_id": "3ce5bd13-ab4c-4a1b-9931-04cd6ca38f95",
      "order": 0,
      "_id": "57d2c15bdd50a5547eeee9ec",
      "inputs": [
        {
          "value": "MARK RODRIGUES",
          "_id": "57d2c15bdd50a5547eeee9df",
          "name": "Name",
          "code": "name",
          "type": "text"
        },
        {
          "value": "64210431756",
          "_id": "57d2c15bdd50a5547eeee9e7",
          "name": "Mobile No",
          "code": "phone",
          "type": "phone"
        },
        {
          "value": "crystalisland@gmail.com",
          "_id": "57d2c15bdd50a5547eeee9e6",
          "name": "Email",
          "code": "email",
          "type": "email"
        }
      ],
      "regions": [
        "all",
        "VY0001",
        "N0305",
        "S0971",
        "A11888",
        "S4379"
      ],
      "name": "Customer",
      "type": "customer",
      "date": "2016-09-09T14:04:11.151Z",
      "hierarchy_key": "15",
      "event_notification_sent": True
    }
  ],
  "location": {
    "latitude": -37.8203253,
    "longitude": 175.2878325
  },
  "additional_inputs": [

  ],
  "inputs": [
    {
      "value": "672248900315",
      "_id": "57d2c15bdd50a5547eeee9de",
      "name": "Reference No",
      "code": "cust_id",
      "type": "text"
    },
    {
      "value": "MARK RODRIGUES",
      "_id": "57d2c15bdd50a5547eeee9df",
      "name": "Name",
      "code": "name",
      "type": "text"
    },
    {
      "value": "4 GRETA STREET GLENVIEW   HAMILTON",
      "_id": "57d2c15bdd50a5547eeee9e0",
      "name": "Address Field 1",
      "code": "address1",
      "type": "text"
    },
    {
      "value": ".",
      "_id": "57d2c15bdd50a5547eeee9e1",
      "name": "Address Field 2",
      "code": "address2",
      "type": "text"
    },
    {
      "value": ".",
      "_id": "57d2c15bdd50a5547eeee9e2",
      "name": "Address Field 3",
      "code": "address3",
      "type": "text"
    },
    {
      "value": ".",
      "_id": "57d2c15bdd50a5547eeee9e3",
      "name": "City",
      "code": "city",
      "type": "text"
    },
    {
      "value": "X",
      "_id": "57d2c15bdd50a5547eeee9e4",
      "name": "State",
      "code": "state",
      "type": "text"
    },
    {
      "value": "3206",
      "_id": "57d2c15bdd50a5547eeee9e5",
      "name": "Pincode",
      "code": "pincode",
      "type": "text"
    },
    {
      "value": "crystalisland@gmail.com",
      "_id": "57d2c15bdd50a5547eeee9e6",
      "name": "Email",
      "code": "email",
      "type": "email"
    },
    {
      "value": "64210431756",
      "_id": "57d2c15bdd50a5547eeee9e7",
      "name": "Mobile Number",
      "code": "phone",
      "type": "text"
    },
    {
      "_id": "57d2c15bdd50a5547eeee9e8",
      "name": "Alternate Number",
      "code": "alt_phone",
      "type": "phone"
    },
    {
      "value": "S4379",
      "_id": "57d2c15bdd50a5547eeee9e9",
      "name": "RM Code",
      "code": "emp_code",
      "type": "text"
    },
    {
      "value": "SILVESTRE PEREIRA",
      "_id": "57d2c15bdd50a5547eeee9ea",
      "name": "RM Name",
      "code": "emp_name",
      "type": "text"
    },
    {
      "value": "{\"latitude\":-37.8203253,\"longitude\":175.2878325}",
      "_id": "57d2c15bdd50a5547eeee9eb",
      "name": "Location",
      "code": "location",
      "type": "location"
    }
  ],
  "user": {
    "code": "S4379",
    "name": "SILVESTRE PEREIRA"
  },
  "visible_regions": [

  ],
  "regions_union": [
    "all",
    "VY0001",
    "N0305",
    "S0971",
    "A11888",
    "S4379"
  ],
  "regions": [
    "all",
    "VY0001",
    "N0305",
    "S0971",
    "A11888",
    "S4379"
  ],
  "name": "MARK RODRIGUES",
  "code": "yoGBISttriv",
  "date": "2016-09-09T14:04:11.149Z",
  "__v": 1,
  "extraRegionAccessibleKey": "",
  "hierarchy_key": "15",
  "version": 1.01,
  "server_date": "2017-10-29T08:52:24.333Z"
}


def user_allotment(i, cus, cus_pointer):
    user = {}
    user["code"] = DATA[i]["code"]
    user["name"] = DATA[i]["name"]
    j = 0
    while j < cus:
        CUST_DATA[j + cus_pointer]["user"] = user
        # print(CUST_DATA[j + cus_pointer]["user"]["code"])
        j += 1


def map_customers():
    cus_pointer = 0
    for i in range(len(DATA)):
        # print('user:', i)
        # print(DATA[i]["code"])
        if i % 5 == 0:
            cus = 50
            user_allotment(i, cus, cus_pointer)
        elif i % 5 == 1:
            cus = 40
            user_allotment(i, cus, cus_pointer)
        elif i % 5 == 2:
            cus = 30
            user_allotment(i, cus, cus_pointer)
        elif i % 5 == 3:
            cus = 20
            user_allotment(i, cus, cus_pointer)
        else:
            cus = 10
            user_allotment(i, cus, cus_pointer)
        cus_pointer += cus
        # pprint(DATA[i])


def main():
    try:
        conn = pymongo.MongoClient()
        # conn = pymongo.MongoClient('127.0.0.1:9999',
        #                            username=USER_NAME,
        #                            password=PD,
        #                            authSource='vymo-lms',
        #                            authMechanism='SCRAM-SHA-1')
    except Exception as e:
        print('DB CONNECTION ERROR:', e)
        sys.exit()
    user_coll = conn[DB_NAME][USER_COLLECTION_NAME]
    # print(coll.index_information())
    for i in range(320):
        user = deepcopy(USER_DATA)
        user["name"] = 'user_' + str(i+1)
        user["code"] = 'code_' + str(i+1)
        user["_id"] = 4567 * (i+1)
        DATA.append(user)
        # pprint(DATA[i])
    coll.insert_many(DATA, True)
    # pprint(DATA)
    for i in range(48000):
        cust = deepcopy(CUSTOMER_DATA)
        cust["name"] = 'user_' + str(i + 1)
        cust["code"] = 'code_' + str(i + 1)
        cust["_id"] = 6523 * (i + 1)
        CUST_DATA.append(cust)
        # print(CUST_DATA[i]["name"])
    customer_coll = conn[DB_NAME][CUST_COLLECTION_NAME]

    map_customers()
    # pprint(DATA)


if __name__ == '__main__':
    main()
