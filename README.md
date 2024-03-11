# python의 boto3를 활용한 aws 인스턴스 동적 관리 툴 제작 


> 인스턴스 동적 생성을 gui가 아닌 파이썬을 통해 관리하는 실습

<br>

## 개발 

- python boto3 api


## 주요 기능

![image](https://github.com/attlet/cloud_project/assets/62745451/1d1820c0-dad2-4477-b1ee-5e93773b18ff)


### 실행중인 인스턴스 목록 확인 
- 내 계정에서 실행되고 있는 인스턴스 목록 확인
  <br>
![image](https://github.com/attlet/cloud_project/assets/62745451/e96253b2-f4e3-4f72-b412-ae772b87bd05)


### 인스턴스 생성 및 삭제
- 미리 생성되어 있는 ami를 통해 인스턴스 생성

#### ami의 모습<br>
![image](https://github.com/attlet/cloud_project/assets/62745451/075f4775-7665-4d60-b79f-3187b960ca9d)

#### 인스턴스를 생성한 모습<br>
![image](https://github.com/attlet/cloud_project/assets/62745451/14985243-f569-4916-8cba-1683076ccf74)

이 옵션을 실행 후 다시 인스턴스 목록을 확인하면 새로 실행되는 모습을 볼 수 있다.
<br>
![image](https://github.com/attlet/cloud_project/assets/62745451/96ea9428-f888-419c-aed7-e4731106289b)


### condor_status 확인

- slave 인스턴스 생성 시, 실행되고 있는 master 노드에 조인이 되는 지 확인할 수 있다.
- htcondor라는 HTC을 통해 작업을 유휴 컴퓨팅 자원 노드에 할당할 수 있다.

####master노드에서 처음 확인한 condor_status <br>
![image](https://github.com/attlet/cloud_project/assets/62745451/d60c5464-5b3f-4c54-89d4-36a8cbccdac3)

####slave노드 새로 생성 후 master의 status <br>
![image](https://github.com/attlet/cloud_project/assets/62745451/7375d8e7-82de-4ce3-bf77-115ec7d8edf4)

### 이미지 생성
- 노드 기반으로 이미지를 생성할 수 있다.

![image](https://github.com/attlet/cloud_project/assets/62745451/f318a9d3-ae27-42b4-a684-63d74431bf2c)



##배운 점, 아쉬운 점

- 파이썬의 boto3를 이용해 aws 인스턴스를 동적으로 생성, 삭제하고, 유휴 자원 상태를 원격으로 관리해보는 경험이었다.
- 작업을 할당해서 조인된 노드끼리 작업이 나눠지는 지 확인을 해보지 못한 게 아쉽다. aws 무료가 끝나 다른 블로그 글들로 공부해 봐야겠다.




