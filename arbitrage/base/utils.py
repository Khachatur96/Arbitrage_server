from datetime import datetime, timezone, timedelta
from .models import Dex
from .abi import *
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/4b1db8d17da142f3861622b56cfdb3e7'))


def get_coins_pair_price(pair):
    """
    :param tuple with pairs info params:
    :return:
        pair_price
    """
    dexes = Dex.objects.all()
    result = {}
    for swap in dexes:
        contract = web3.eth.contract(address=swap.address, abi=swap.abi)
        if swap.name == 'OneSplit':
            try:
                response_result = result_by_get_expected_return(address_1=pair[0], address_2=pair[1],
                                                                amount=int(pair[3]), decimal=pair[-1],
                                                                contract=contract)
            except Exception as e:
                pass
        elif swap.name == 'Balancer':
            try:
                response_result = result_by_view_split_exact_out(address_1=pair[0], address_2=pair[1],
                                                                 amount=int(pair[3]), contract=contract)
            except Exception as e:
                pass

        elif swap.name == 'Kyber':
            try:
                response_result = result_by_get_expected_rate(address_1=pair[0], address_2=pair[1],
                                                              amount=int(pair[3]), contract=contract)
            except Exception as e:
                pass
        elif swap.name == 'Curve':
            try:
                response_result = result_by_get_estimated_swap_amount(address_1=pair[0], address_2=pair[1],
                                                                      amount=int(pair[3]), decimal=pair[-1],
                                                                      contract=contract)
            except Exception as e:
                pass
        else:

            try:
                response_result = result_by_get_amounts_out(address_1=pair[0], address_2=pair[1],
                                                            amount=int(pair[3]), decimal=pair[-1], contract=contract)
            except Exception as e:
                pass

        result[swap.name] = float(response_result)
    result['pair'] = pair[-3]

    return result


def get_time_now_in_local_timezone(timezone_offset=0.4):
    """

    :param timezone_offset:
    :return: datetime in string representation
    """
    timezone_info = timezone(timedelta(hours=timezone_offset))

    return datetime.now(timezone_info)


