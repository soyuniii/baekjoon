# baekjoon
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

## 환경 설정
- **Language**: Python 3.13.5
- **IDE**: VS Code

## Python으로 문제 풀이 시작하기

### 1. 새 문제 풀이 파일 생성
```bash
# 예: Bronze/문제번호. 문제이름/문제이름.py
touch "백준/Bronze/1234. 문제이름/문제이름.py"
```

### 2. 기본 입출력 템플릿
```python
# 한 줄 입력
n = int(input())

# 여러 개 입력 (공백 구분)
a, b = map(int, input().split())

# 리스트로 입력받기
arr = list(map(int, input().split()))

# 여러 줄 입력
import sys
input = sys.stdin.readline  # 빠른 입력

# 출력
print(결과)
```

### 3. Python 파일 실행 방법

#### VS Code에서 실행:
1. 파일 열기
2. `Ctrl + Shift + P` (Mac: `Cmd + Shift + P`)
3. "Python: Run Python File in Terminal" 선택
4. 또는 우측 상단 ▶️ 버튼 클릭

#### 터미널에서 실행:
```bash
python3 파일명.py
# 또는 입력 파일 사용 시
python3 파일명.py < input.txt
```

### 4. 자주 사용하는 패턴
```python
# 빠른 입출력
import sys
input = sys.stdin.readline

# 무한 루프
while True:
    try:
        # 코드
        pass
    except:
        break

# EOF까지 입력
import sys
for line in sys.stdin:
    # 처리
    pass
```
