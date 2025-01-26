# GiftReaper
GiftReaper เป็นแพ็กเกจสำหรับช่วยในการทำธุรกรรมจากการส่งซองทรูมันนี่
## _ความสามารถของแพ็กเกจ_
- ตรวจสอบข้อมูลจากซองทรูมันนี่
- รับเงินจากซองทรูมันนี่
- เปรียบเทียบจำนวนเงินจากซองทรูมันนี่กับราคาสินค้าที่สนใจ
- ตรวจสอบจำนวนเงินจากซองทรูมันนี่
## วิธีติดตั้ง
```sh
pip install GiftReaper
```
#### วิธีตรวจสอบข้อมูลจากซองทรูมันนี่
```sh
verify_voucher(${ลิงก์บัตรกำนัลหรือรหัสบัตรกำนัล}, ${หมายเลขโทรศัพท์ของบัญชีรับเงิน})
```
#### วิธีรับเงินจากซองทรูมันนี่
```sh
redeem_voucher(${ลิงก์บัตรกำนัลหรือรหัสบัตรกำนัล}, ${หมายเลขโทรศัพท์ของบัญชีรับเงิน})
```
#### วิธีเปรียบเทียบจำนวนเงินจากซองทรูมันนี่กับราคาสินค้าที่สนใจ
```sh
is_voucher_balance_sufficient(${ลิงก์บัตรกำนัลหรือรหัสบัตรกำนัล}, ${หมายเลขโทรศัพท์ของบัญชีรับเงิน}, ${ราคาสินค้าที่สนใจ})
```
#### วิธีตรวจสอบจำนวนเงินจากซองทรูมันนี่
```sh
check_voucher_amount_baht(${ลิงก์บัตรกำนัลหรือรหัสบัตรกำนัล}, ${หมายเลขโทรศัพท์ของบัญชีรับเงิน})
```
#### ตัวอย่างรูปแบบข้อมูลต่าง ๆ
```sh
# รูปแบบลิงก์หรือรหัสบัตรกำนัล
voucher_url_first_format: str = 'https://gift.truemoney.com/campaign/?v={รหัสบัตรกำนัล}'
voucher_url_second_format: str = '{รหัสบัตรกำนัล}'

# รูปแบบหมายเลขโทรศัพท์
mobile_number_first_format: str = '08x-xxx-xxxx'
mobile_number_second_format: str = '08xxxxxxxx'

# รูปแบบราคาสินค้า
product_price_500: int = 500
product_price_500_0: float = 500.0
```
#### ตัวอย่าง
```sh
from GiftReaper import verify_voucher, redeem_voucher, is_voucher_balance_sufficient, check_voucher_amount_baht

voucher_url_10_baht: str = '{รหัสบัตรกำนัล}'
mobile_number: str = '08x-xxx-xxxx'

product_price_9_50: float = 9.50
product_price_10: int = 10
product_price_10_50: float = 10.50

if __name__ == '__main__':
    # check_voucher_amount_baht()
    print(check_voucher_amount_baht(voucher_url_10_baht, mobile_number)) # ผลลัพธ์ 10.0

    # is_voucher_balance_sufficient()
    print(is_voucher_balance_sufficient(voucher_url_10_baht, mobile_number, product_price_9_50)) # ผลลัพธ์ False
    print(is_voucher_balance_sufficient(voucher_url_10_baht, mobile_number, product_price_10)) # ผลลัพธ์ True
    print(is_voucher_balance_sufficient(voucher_url_10_baht, mobile_number, product_price_10_50)) # ผลลัพธ์ False

    # verify_voucher()
    response = verify_voucher(voucher_url_10_baht, mobile_number)
    status_code = response['status']['code']
    if status_code == 'SUCCESS':
        print(response)
    elif status_code == 'INVALID_MOBILE_NUMBER':
        print('รูปแบบหมายเลขโทรศัพท์ไม่ถูกต้อง')
    elif status_code == 'CANNOT_GET_OWN_VOUCHER':
        print('เจ้าของซองทรูมันนี่ไม่สามารถรับเงินจากซองของตนเองได้')
    elif status_code == 'TARGET_USER_NOT_FOUND':
        print('ไม่พบหมายเลขโทรศัพท์นี้ในระบบ')
    elif status_code == 'INTERNAL_ERROR':
        print('ระบบของทรูมันนี่นี้ขัดข้อง')
    elif status_code == 'VOUCHER_OUT_OF_STOCK':
        print('เงินจากซองทรูมันนี่นี้มีคนก่อนหน้ารับไปหมดแล้ว')
    elif status_code == 'VOUCHER_NOT_FOUND':
        print('ไม่พบซองทรูมันนี่นี้ในระบบ')
    elif status_code == 'VOUCHER_EXPIRED':
        print('ซองทรูมันนี่นี้หมดอายุ')
    
    # redeem_voucher()
    response = redeem_voucher(voucher_url_10_baht, mobile_number)
    status_code = response['status']['code']
    if status_code == 'SUCCESS':
        print(response)
    elif status_code == 'INVALID_MOBILE_NUMBER':
        print('รูปแบบหมายเลขโทรศัพท์ไม่ถูกต้อง')
    elif status_code == 'CANNOT_GET_OWN_VOUCHER':
        print('เจ้าของซองทรูมันนี่ไม่สามารถรับเงินจากซองของตนเองได้')
    elif status_code == 'TARGET_USER_NOT_FOUND':
        print('ไม่พบหมายเลขโทรศัพท์นี้ในระบบ')
    elif status_code == 'INTERNAL_ERROR':
        print('ระบบของทรูมันนี่นี้ขัดข้อง')
    elif status_code == 'VOUCHER_OUT_OF_STOCK':
        print('เงินจากซองทรูมันนี่นี้มีคนก่อนหน้ารับไปหมดแล้ว')
    elif status_code == 'VOUCHER_NOT_FOUND':
        print('ไม่พบซองทรูมันนี่นี้ในระบบ')
    elif status_code == 'VOUCHER_EXPIRED':
        print('ซองทรูมันนี่นี้หมดอายุ')
```

#### คำเตือน
เนื่องจาก GiftReaper อาจมีการคืนค่าเป็น UTF-8 หากเกิดปัญหาด้านการแสดงผลอักขระ (เช่น ภาษาไทยไม่แสดงผล) ให้ลองเพิ่มโค้ดนี้ที่ต้นไฟล์ของคุณ:
```shell
import sys
import io

# ตั้งค่า stdout ให้รองรับ UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```
