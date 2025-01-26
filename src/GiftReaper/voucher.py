import cloudscraper
from .utils import search_params_get, mobile_number_get

requests = cloudscraper.create_scraper()

def verify_voucher(voucher_url: str, mobile_number: str):
    try:
        hash = search_params_get(str(voucher_url), "v")
        mobile = mobile_number_get(str(mobile_number))
    except Exception as error:
        error_message = error.args[0] if error.args else {}
        return {'status': {'message': error_message.get('message', 'Unknown Error'), 'code': error_message.get('code', 'UNKNOWN')}, 'data': None}
    else:
        response = requests.get(f'https://gift.truemoney.com/campaign/vouchers/{hash}/verify?mobile={mobile}')
        return response.json()

def redeem_voucher(voucher_url: str, mobile_number: str):
    try:
        voucher_hash = search_params_get(str(voucher_url), "v")
        mobile = mobile_number_get(str(mobile_number))
    except Exception as error:
        error_message = error.args[0] if error.args else {}
        return {'status': {'message': error_message.get('message', 'Unknown Error'), 'code': error_message.get('code', 'UNKNOWN')}, 'data': None}
    else:
        data = {
            'mobile': mobile,
            'voucher_hash': voucher_hash
        }
        response = requests.post(f'https://gift.truemoney.com/campaign/vouchers/{voucher_hash}/redeem', json=data)
        return response.json()

def is_voucher_balance_sufficient(voucher_url: str, mobile_number: str, product_price: float) -> bool:
    try:
        if isinstance(product_price, int):
            product_price = float(product_price)
        response = verify_voucher(voucher_url, mobile_number)
        if response['status']['code'] == 'SUCCESS' and isinstance(product_price, float):
            if float(response['data']['voucher']['amount_baht']) == product_price:
                return True
        return False
    except:
        return False

def check_voucher_amount_baht(voucher_url: str, mobile_number: str) -> float:
    try:
        response = verify_voucher(voucher_url, mobile_number)
        if response['status']['code']:
            return float(response['data']['voucher']['amount_baht'])
        return 0.00
    except:
        return 0.00