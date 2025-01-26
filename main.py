response = verify_voucher(voucher_url_10_baht, mobile_number)
status_code = response['status']['code']
if status_code == 'SUCCESS':
    pass
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