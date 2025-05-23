# jiwon_uni

# 🖥️ Universal Clipboard Simulation – 기기 간 클립보드 동기화 시스템

## 📌 프로젝트 개요

Universal Clipboard는 애플 생태계에서 제공하는 기능으로,  
**서로 다른 기기 간에 클립보드(복사한 내용)를 실시간으로 공유**할 수 있도록 지원합니다.  
예: MacBook에서 복사한 텍스트를 iPhone에서 바로 붙여넣을 수 있음.

이 프로젝트는 해당 시스템을 간단한 Python 코드로 시뮬레이션하여,  
**시퀀스 다이어그램 기반 시스템 분석 → 코드 구현 → 모듈 구조 평가**의 과정을 수행합니다.

---

## 🎯 사용 시나리오

1. 사용자가 MacBook에서 어떤 텍스트를 복사합니다.
2. 운영체제가 클립보드 변경을 감지하고 암호화합니다.
3. 근처의 연결된 iPhone을 Bluetooth/Wi-Fi로 탐색합니다.
4. 기기 간 인증 후 암호화된 데이터를 전송합니다.
5. 사용자가 iPhone에서 붙여넣기를 누르면 복호화하여 적용합니다.

---

## 📊 시퀀스 다이어그램

![Universal Clipboard Diagram](./다이어그램.png)

---

## 💻 샘플 코드 (일부 발췌)

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


