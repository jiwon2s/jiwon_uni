# jiwon_uni

# 📋 Universal Clipboard Simulation – 기기 간 클립보드 동기화 시스템

이 프로젝트는 서로 다른 기기에서 클립보드를 공유하는 'Universal Clipboard' 시스템을 시뮬레이션한 예제입니다.  
사용자는 단순히 복사/붙여넣기만 하지만, 그 사이에는 암호화, 네트워크 전송, 복호화 등의 복잡한 과정이 자동으로 수행됩니다.

---

## 📊 시퀀스 다이어그램

![Universal Clipboard Diagram](./다이어그램.png)

---

## 💻 샘플 코드 (요약)

```python
class Clipboard:
    def __init__(self):
        self.data = ""

    def copy(self, content):
        print("[Device A] 복사된 데이터:", content)
        self.data = content

    def paste(self):
        print("[Device B] 붙여넣기 결과:", self.data)
        return self.data



