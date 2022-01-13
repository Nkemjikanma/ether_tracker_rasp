
import json
from web3 import Web3, EthereumTesterProvider
from web3.gas_strategies.time_based import *
import json
import time


class TRACKER:
    def __init__(self):
        self.remote_provider_url = "https://url_provider"
        self.w3 = Web3(Web3.HTTPProvider(self.remote_provider_url))
        self.current_gas = 0

    # TODO: Get the current gas price
    def get_gas_price(self):
        pending_1000 = []
        self.current_gas = 0

        while True:
            start_time = time.time()
            pending = self.w3.eth.get_block('pending')['baseFeePerGas']
            pending_1000.append(pending)
            # print(pending_1000)
            if len(pending_1000) != 100:
                # time.sleep(5)
                continue
            else:
                for i in range(len(pending_1000)):
                    self.current_gas += pending_1000[i]
                self.current_gas = self.current_gas/len(pending_1000)
                self.current_gas = self.w3.fromWei(self.current_gas, 'gwei')
                # print(self.current_gas)
                #print(f'New gas in about{time.time()-start_time}')
                pending_1000 = []
                # time.sleep(5)
            return self.current_gas

    def display_on_pi(self):

        current_gas = self.current_gas
        print(current_gas)
        #print(f'New gas in about{time.time()-start_time}')


run = TRACKER()
# run.get_balance()

while True:
    run.get_gas_price()
    run.display_on_pi()
