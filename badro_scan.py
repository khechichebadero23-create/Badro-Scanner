import socket

print("--- أداة بادرو لفحص شبكات المواقع ---")

# 1. نطلب من المستخدم إدخال رابط الموقع
target_url = input("Enter the website URL (e.g., google.com): ")

try:
    # 2. نطلب من بايثون جلب عنوان الـ IP الحقيقي للموقع
    ip_address = socket.gethostbyname(target_url)
    
    # 3. نطبع النتيجة للمستخدم
    print("\n[+] الفحص تم بنجاح!")
    print(f"Website: {target_url}")
    print(f"IP Address: {ip_address}")

except:
    # في حال كتب المستخدم الموقع بشكل خاطئ أو لم يكن هناك إنترنت
    print("\n[-] عذراً، تعذر جلب معلومات هذا الموقع. تأكد من الرابط.")

