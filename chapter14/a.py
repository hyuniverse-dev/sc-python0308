'''
파일명: a.py

- import 문
    그대로 사용하면 해당 모듈에 저장된 모든 코드를 가져온다.

- from - import 문
    모듈에 포함된 함수 또는 클래스 중 특정 대상만 골라서 가져오는 방법이다.
    (1) from 모듈(파이썬 파일) import 함수명/클래스명 - 해당 함수/클래스 하나만 가져오는 방법
    (2) from 모듈 import 함수명/클래스명, 함수명/클래스명 - 2개 이상의 함수/클래스를 가져오는 방법
    (3) from 모듈 import * - 모듈의 모든 함수/클래스를 가져오는 방법

- alias 사용하기
    특정 모듈에 대해 별칭을 지어서 사용한다.
    모듈에 따라 관례적으로 사용하는 별칭도 존재한다.
'''

##### import / from-import 문 사용하기
# import b
# from chapter14.b import hello_b, hello_b2
from chapter14.b import *

hello_b()
hello_b2()
hello_b3()


##### alias 사용하기
import very_long_module_name as vlm


vlm.function1()











