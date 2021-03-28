from __future__ import print_function
from Robinhood import Robinhood
import getpass
import collections
import os
import sys
import uuid
#robinhood = Robinhood()
def get_input():
    if sys.version_info[0] < 3:
        return raw_input()
    else:
        return input()


def collect_login_data(robinhood_obj, username, password, device_token, mfa_code):
    logged_in = False
    while logged_in != True:
        if username == "":
            username = os.getenv("RH_USERNAME", "")
        if username == "":
            print("Robinhood username:", end=' ')
            username = get_input()

        if password == "":
            password = os.getenv("RH_PASSWORD", "")
        if password == "":
            password = getpass.getpass()

        if device_token == None:
            device_token = os.getenv("RH_DEVICE_TOKEN", "")
            print("device token: ", device_token)
        if device_token == "":
            device_token = uuid.uuid1()
            print("Generated device token:", device_token)

        logged_in = robinhood_obj.login(username=username, password=password, device_token=device_token)

        if logged_in != True and logged_in.get('non_field_errors') == None and logged_in.get('mfa_required') == True:
            if mfa_code is None:
                mfa_code = os.getenv("RH_MFA")
            if mfa_code == None:
                print("Robinhood MFA:", end=' ')
                mfa_code = get_input()
            logged_in = robinhood_obj.login(username=username, password=password, device_token=device_token, mfa_code=mfa_code)

        if logged_in != True:
            print("\nInvalid inputs. Please try again.\n")
            username = ""
            password = ""
            device_token = ""
            mfa_code = ""

    return True