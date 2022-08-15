### Data AI, 강화학습

### Auto-Encoder

- Auto Encoder : Target이 존재하지만 지도학습이 아닌 비지도 학습으로 분류함.
- 딥러닝 프레임워크
  - 학습데이터가 주어졌을 때,
  - 최소 손실 함수값을 갖는
  - 딥러닝 모델 파라미터를 찾는 것
- 이상감지를 위한 오토인코더
  - 일반화에 도움이 되는 사전 학습 모델 등장
    - 시각: AlexNet, VGG, Inception, LeNet등
    - 언어: BERT, GPT 등
    - 정형 : TabNet by Google
  - 이상감지: 평균에서벗어나는이상치찾기
    - 핵심정보(예: 평균)를 잘 찾아낼수록 이상감지 성능향상
    - 기존방식: Feature 직접추출
    - Auto-Encoder: Feature 자동추출
- 차원 축소법 : 핵심 정보 뽑아내는 수단
  - PCA 
    - Encoder에서 Component별 중요한 부분만 Compressed
    - Decoder에서 다시 Reconstruction
    - 입력, 출력이 같으면 좋은 성능
  - T-SNE : 비선형 차원 축소법
    - t-SNA는 Reconstruction이 불가(Non-parametric Mapping이므로)
  - Auto-Encoder : Encoding와 Decoding 동시 학습
    - PCA에서 Encoder와 Decoder를 딥러닝 모델로 구현한 것
    - 비지도 학습이지만 지도학습으로 이해 할 수도 있다.
    - 입력과 복원 이 비슷해야 성공적
      - MSE, MAE 등의 손실 함수로 차이를 표현함
- 이상감지
  - Auto Encoder 학습후 이상감지할 Thresholding을 정함
    - 학습에 사용한 손실함수가 중요하게 이용
- Variational 오토인코더
  - 인코딩 과 디코딩 사이에 샘플링이 추가됨.
- Denoising 오토인코더
  - 인풋의 잡음을 제거해주고 깨끗한 아웃풋을 얻음

### 강화학습

- 강화학습 : 주어진 Environment과 상호작용에서 최대 보상을 얻을 수 있는 에이전트를 학습시키는 과정
- Agent
  - Policy와 Action-value 함수가 중요
  - Policy를 구하는 방법
    - 직접 구하기
      - Input : State
      - Output : Action 혹은 각 Action을 선택할 확률
      - Policy는 불랙박스모델
    - Q-Table로 구하기
      - A에서 출발해서 각 칸을 옮길때 마다 Reward 
      - Reward의 합을 최대화 하면서 최종 목적지에 도착하는 경로찾기
        - Bellman Optimality 방정식을 푸는 방법으로 해결
      - State가 Continuos이면 Table 구성 불가한데?
        - Action Value function을 Q-Table로 명명
    - Explore and Exploit: 𝜖-Greedy Policy
      - Explore 초반에는 손해를 감수하고 탐색을 통한 경험 축적
      - Exploit 후반에는 확보된 경험을 활용
    - Action-Value 함수를 사용
      - Deep Q-Network
      - DDPG
      - Actor-Critic
    - 강화학습 프로세스
      - Environment를위한시뮬레이션시스템구성(★★★)
      - 관측값(State),Action 스펙정의
      - 보상의적절한방법설정
      - 정확한Q(s,a)를위한딥러닝모델구조선택
      - Q(s,a)을학습하는데필요한최적화알고리즘선택
      - 최적화알고리즘에들어가는Hyper-parameter 설정
