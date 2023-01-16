# 경매24 : 눈치보고 경매하기
---
![frame](https://user-images.githubusercontent.com/108874833/212066720-bf377567-fccc-430d-aecb-87bb52cd3ffa.png)
> 2023.1.16 ~ 2023.1.17
## Stack
* HTML
* CSS
* Python
* JQuery
---
## TEAMMATES
| 김영현 | 이기웅 | 조성재 | 조영준 |
|---|---|---|---|
| FE | BE | BE | BE |

---

## HOME
![home](https://user-images.githubusercontent.com/108874833/212066873-5e61e8a9-78e2-4dba-b5bc-f6e5b33075ae.jpg)
### you have to sign in without having any ID/PW

---
# API명세서
| 기능 | Method | url | request | response |
|---|---|---|---|---|
| 로그인 | POST | /auth/login |  |  |
| 회원가입 | POST | /auth/login |  | 회원 가입 메세지 |
| 로그아웃 | POST | /logout |  | 로그아웃 메세지 |
| 홈 | GET | /items |  | allItems |
| 마이페이지 | GET | /users |  |  |
| 경매 등록 | POST | /upload |  | 경매 등록 메세지 |
| 경매 입찰 | POST | /items/{itemNum} |  | 이름,입찰가 메세지? |
| 입찰 취소 | GET | /items |  | 입찰 취소 메세지 |

---
# DB FORM
## users
| ID | PW | 이름 |
|---|---|---|
| string | string | string |

## items
| itemNum | title | pic | minBid | nowBid | unitBid | status | desc | owner |
|---|---|---|---|---|---|---|---|---|
| int | string | string | int | int | int | int | string | string |

- itemNum은 DB 전체 조회후 length+1 해줌
- pic은 static폴더에 저장후 url로 지정
- status : [0 : 경매 진행중, 1 : 경매 완료]

---
# 기능명세서
---

## 네비게이션 바

- [x] session ID를 이용해 session ID가 존재할경우 상단 네비게이션 바에 환영 message를 띄운다.
- [x] users에 저장된 정보를 이용해 user의 정보(경매중인 물건, 낙찰된 물건)을 보러갈 수 있는 onclick함수를 구현한다.
- [x] logout 버튼을 통해 session값을 제거한다.

## 로그인 / 회원가입
- [x] Id-valid double check를 통해 오류를 제거한다.
- [x] 비밀번호는 회원이 충분히 인지할 수 있게 한 칸은 star-shaped, 한 칸은 raw한 데이터를 보여준다.
- [x] 5중 유효성 검사를 통해 회원가입을 강화한다.
- [x] 성공할 경우와 실패할 경우 모두 alert로 message를 띄운다.

## Main 
- [x] 로그인한 sessionID가 아닌 모든 사용자의 items를 렌더링한다.
- [x] 우측 하단의 + 버튼으로 사용자의 경매 물건을 등록할 수 있다.

## Upload
- [ ] 물건의 상세 정보를 받아 db에 저장한다..
- [x] img는 url link형식이 아닌 filebox형태로 등록하게 한다.

## Specific page
- [ ] 물건의 title, image, desc, 현재 bidding중인 금액, unit bid등을 렌더링한다
- [ ] 입찰 버튼으로 bidnow에 unitbid만큼 올려준다.
- [ ] msg를 전달하고 새로고침한다
- [ ] 입찰금액이 숨겨진 최종금액에 달하면 owner를 sessionId로 바꾼다.
- [ ] timer를 설정해 시간 안에 낙찰되지 않으면, 현재경매가가 낙찰액이 된다.

## Mypage
- [ ] 내가 현재 등록중인 물건과, 내가 낙찰받은 물건을 표시한다.
  - [ ] 두 가지의 물품들은 분리해놔야 한다.
---

# 유의사항

---

즐거운 코딩 하기