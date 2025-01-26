import re

def search_params_get(url: str, params: str) -> str:
    url = url.replace('https://gift.truemoney.com/campaign/?v=', '')
    params = f'{params}='
    params_index = url.find(params)
    start_index = 0
    if params_index != -1:
        start_index: int = params_index + len(params)
    end_index: int = url.find("&", start_index) if url.find("&", start_index) != -1 else len(url)
    return url[start_index:end_index]

def mobile_number_get(mobile_number: str) -> str:
    mobile_number = mobile_number.replace('-', '')
    if re.fullmatch(r"\d{10}", mobile_number):
        return mobile_number
    raise ValueError({ 'message': 'รูปแบบหมายเลขโทรศัพท์ไม่ถูกต้อง', 'code': 'INVALID_MOBILE_NUMBER'})