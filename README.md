# Python GUI - Shortcut Launcher

## 목표 및 목적
* 약간의 설정이 가능한 단축키 프로그램을 개발한다.
    * 지정된 명령어를 클릭 한번으로 바로 실행할 수 있는 프로그램을 개발한다.
    * 설정을 통해 프로그램의 옵션을 작은 폭에서 변경할 수 있다.

### 문제 분석
  
* 최종 목적 : 단축키 실행 프로그램인 Shortcut Launcher를 완성한다.
    * 상위 목적 1 : GUI에 버튼을 구현한다.
        * 하위 목적 1 : 2행 4열 그리드의 버튼을 구현한다.
        * 하위 목적 2 : 버튼을 클릭하면 지정된 명령어를 실행한다.
    * 상위 목적 2 : 프로그램을 수정할 수 있는 설정을 구현한다.
        * 하위 목적 1 : 프로그램을 설정하는 메뉴를 새로운 윈도우에 구현한다.
            * 최하위 목적 1 : 창 크기를 직접 수정할 수 있게 하되, 버튼 또한 비율에 맞춰 변하도록 한다.
            * 최하위 목적 2 : 항상 위 옵션을 추가한다.
            * 최하위 목적 3 : 프로그램 색상을 RGB 값을 통해 수정할 수 있게 한다.
        * 하위 목적 2 : 프로그램의 정보를 표현하는 메뉴를 구현한다.
        * 하위 목적 3 : 프로그램을 종료하는 메뉴를 구현한다.
    * 상위 목적 3 : 난이도 변경에 따른 수정 가능성을 염두에 두고, 프로그램을 작성한다.

## 개발 사양

### 하드웨어
* CPU : Intel(R) Core(TM) i5-6600 CPU @ 3.30GHz, 3301Mhz, 4 코어, 4 논리 프로세서
* RAM : 8192MB RAM
* HDD/SSD : Western Digital 240GB WD Green Internal PC SSD
* GPU : NVIDIA GeForce GTX 970

### 소프트웨어
* OS : Microsoft Windows 10 Pro 10.0.19042 build 19042
* 개발 스택 : Tkinter (라이브러리 추가를 하지 않아도 된다는 간편성, 체계적으로 정리된 사이트 발견)
* 개발 프로그램 : Visual Studio Code
* 개발 언어 : Python v3.9

### 코드룰
* 예시 프로그램

```
    # 변수명
    test_variable = 13

    # 클래스명
    class TestClass:
        def __init__(self):
            # 프로퍼티명
            self.testProperty = 41

        # 메소드명
        def TestMethod(self):
            print(self.testProperty)
    
    if __name__ == "__main__":
        test_variable = TestClass(43)
        test_variable.TestMethod()
```

* 본인의 코드 룰 

```
    # 변수명
    test_variable = 13

    # 클래스명
    class TestClass:
        def __init__(self):
            #프로퍼티명
            self.testProperty = 41
        
        #메소드명
        def TestMethod(self):
            print(self.testProperty)
    
    if __name__ == "__main__":
        test_variable = TestClass(43)
        test_variable.TestMethod()