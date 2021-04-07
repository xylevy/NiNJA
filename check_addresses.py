import requests
import json
import time
import pickle
from sha_btc import Address, save_objects

with open("addresses.pickle", 'rb') as pkl:
    addresses = pickle.load(pkl)

updated_addresses = list()


def check_addy(add):
    phrase = add.pass_phrase
    pk = add.u_prk

    for address in [add.u_addy, add.c_addy]:

        response = requests.get(f"https://blockchain.info/address/{address}?format=json&offset=0")

        data = json.loads(response.text)

        final_bal = data["final_balance"]

        total_rec = data["total_received"]

        if int(total_rec) > 1:
            time_ = data["txs"][0]["time"]
            at = time.strftime('%Y-%m-%d', time.localtime(int(time_)))
            print(f"{phrase} > {address} used ::  Last Transaction {at}")
            add.set_status("Used")

        else:
            print(f"Address {address} is unused")
            add.set_status("Unused")

        if int(final_bal) > 1:
            print("--*20")
            print(f"Hit {address} > {pk} Final Balance {final_bal}")
            print("--" * 20)
            if not add.status:
                add.set_status(f"Hit {final_bal} btc , {address} > time {int(time.time() * 1000)}")
            else:
                add.set_status2(f"Hit {final_bal} btc , {address} > time {int(time.time() * 1000)}")

    return add


if "__main__" in __name__:

    for addy in addresses:
        updated_addresses.append(check_addy(addy))

    save_objects(updated_addresses, "checked_btc.pickle")
