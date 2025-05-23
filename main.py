import time
import base64

class Clipboard:
    def __init__(self):
        self.data = ""

    def copy(self, content):
        print("[Device A] 복사된 데이터:", content)
        self.data = content

    def paste(self):
        print("[Device B] 붙여넣기 결과:", self.data)
        return self.data

class Crypto:
    @staticmethod
    def encrypt(data: str) -> str:
        encoded = base64.b64encode(data.encode()).decode()
        print("[암호화 완료] →", encoded)
        return encoded

    @staticmethod
    def decrypt(data: str) -> str:
        decoded = base64.b64decode(data.encode()).decode()
        print("[복호화 완료] →", decoded)
        return decoded

class NetworkSimulator:
    def __init__(self):
        self.shared_data = ""

    def send(self, encrypted_data):
        print("[네트워크] 데이터 전송 중...")
        time.sleep(1)
        self.shared_data = encrypted_data

    def receive(self):
        print("[네트워크] 데이터 수신 완료")
        return self.shared_data

# 시뮬레이션 실행
device_a_clipboard = Clipboard()
device_b_clipboard = Clipboard()
crypto = Crypto()
network = NetworkSimulator()

# 1. Device A에서 복사
data = "hello from MacBook!"
device_a_clipboard.copy(data)

# 2. 암호화
encrypted = crypto.encrypt(device_a_clipboard.data)

# 3. 네트워크 전송
network.send(encrypted)

# 4. 수신 및 복호화
received = network.receive()
decrypted = crypto.decrypt(received)

# 5. Device B에서 붙여넣기
device_b_clipboard.copy(decrypted)
device_b_clipboard.paste()
