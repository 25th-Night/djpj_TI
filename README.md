# djpj_TI
> Python, Django를 이용한 소셜 블로그 & 상점 애플리케이션 개발 프로젝트 - 배정만 강사님 강의

<br>
<br>
<br>

# 💡 챕터별 학습 내용 요약

<br>

## [0️⃣1️⃣ Catalog App - Basic](https://www.notion.so/browneyed/32-Catalog-App-Basic-3f00e9ab75584ebcbe4d3e70cbb7ae67?pvs=4)

1. Django의 MVT 패턴을 이용한 기본 앱 생성
2. Model - Meta 클래스에서 ordering과 indexes 설정을 통한 DB 검색 및 정렬 최적화
3. Model - models.TextChoices를 이용한 ChoiceField 설정
4. URL - namespace 와 app_name 지정을 통한 url 호출
5. Model - CustomManager를 통한 효율적인 ORM 사용
6. ORM - QuerySet이 평가되는 시점

<br>

## [0️⃣2️⃣ Catalog App - Advanced](https://www.notion.so/browneyed/32-Catalog-App-Basic-3f00e9ab75584ebcbe4d3e70cbb7ae67?pvs=4)

1. Model - 게시물에 대한 정규 URL 생성
2. Model - SlugField를 이용한 게시물에 대한 SEO 친화적인 URL 생성
3. View - Pagination 사용 : Frontend vs Backend
4. Django로 이메일 보내기 - Google의 STMP & send_mail
5. 댓글 시스템 생성하기

<br>

## [0️⃣3️⃣ Catalog App - Extended](https://www.notion.so/browneyed/35-Catalog-App-Extended-2d684ab5dbb2421fa4eeb6ff518e26aa?pvs=4)

1. django-taggit 라이브러리를 이용한 Tag 필드 사용
2. 게시물 검색 기능 개발
3. Template - 커스텀 템플릿 태그와 필터 생성 및 사용
4. 사이트맵 프레임워크를 이용한 사이트맵 등록하기
5. 신디케이션 피드 프레임워크를 이용한 피드 만들기
6. PostgreSQL - Full-text search 이용하기
7. PostgreSQL - SearchVector를 이용한 여러 필드에 대한 검색
8. PostgreSQL - SearchQuery를 이용한 형태소 추출 사용
9. PostgreSQL - SearchRank를 이용한 쿼리 가중치 설정
10. PostgreSQL - TrigramSimilarity를 이용한 쿼리 유사도 설정

<br>

## [0️⃣4️⃣ 소셜 웹사이트 구축](https://www.notion.so/browneyed/36-0a92a21cadd444feadd846de282a32e8?pvs=4)

1. 사용자 인증 - 세션 인증 방식 사용
2. django.contrib.auth - 회원가입, 로그인 및 로그아웃, 권한 및 그룹 관리, 비밀번호 변경 및 재설정
3. 비밀번호 해싱 알고리즘 변경
4. 사용자 모델 확장 - 프로필 생성
5. Pillow 라이브러리를 이용한 미디어 파일 제공
6. 메시지 프레임워크 사용하기
7. 사용자 정의 인증 백엔드 작성 - 유저명과 이메일을 사용한 로그인

<br>

## [0️⃣5️⃣ 소셜 로그인](https://www.notion.so/browneyed/37-c56e5aad83f4462d964bff0a31c7290d?pvs=4)

1. Python Social Auth를 사용하여 소셜 인증 추가
2. Django Extensions 설치
3. 개발 서버를 HTTPS로 실행 - werkzeug, pyOpenSSL
4. Facebook을 사용한 인증 추가
5. Google을 사용한 인증 추가
6. 소셜 인증으로 등록한 사용자를 위한 프로필 생성

<br>

## [0️⃣6️⃣ 컨텐츠 공유하기](https://www.notion.so/browneyed/38-fbdc6e1d6e0d4662b5d508a88157b110?pvs=4)

1. Model - 다대다 관계 생성하기
2. 폼에 대한 동작 사용자 정의하기
3. JavaScript와 Django를 함께 사용하기
4. JavaScript 북마크릿 만들기
5. request 라이브러리를 이용한 url로부터 이미지 추출
5. `easy-thumbnails`를 사용하여 이미지 썸네일 생성하기
6. JavaScript와 Django를 사용한 비동기 HTTP 요청 구현하기
7. 무한 스크롤 페이지네이션 구축하기

<br>

## [0️⃣7️⃣ 사용자 행동 추적](https://www.notion.so/browneyed/39-f630394f5a4a45198f5451f31f87ebb5?pvs=4)

1. 팔로우 시스템 구축하기
2. 중개 모델을 사용한 다대다 관계 생성하기
3. 활동 스트림 애플리케이션 생성하기
4. 모델에 일반적인 관계 추가하기
5. 관련 객체에 대한 QuerySet 최적화하기
6. 카운트를 비정규화하기 위해 신호(Signal) 사용하기
7. 관련 디버그 정보를 얻기 위해 Django Debug Toolbar 사용하기
8. debugsqlshell을 이용한 ORM 쿼리 테스트
8. Redis를 사용하여 이미지 조회 수 세기
9. Redis를 사용하여 가장 많이 조회된 이미지의 순위 생성하기

<br>

## [0️⃣8️⃣ 온라인 상점 구축](https://www.notion.so/browneyed/40-76305f0fbe9b47c3ae6a287c3fdee09c?pvs=4)

1. 제품 카탈로그 생성
2. Django 세션을 사용하여 쇼핑 카트 생성
3. 커스텀 컨텍스트 프로세서 생성
4. 고객 주문 관리
5. RabbitMQ를 메시지 브로커로 사용하여 프로젝트에 Celery 구성
6. Celery를 사용하여 고객에게 비동기적으로 알림 전송
7. Flower를 사용하여 Celery 모니터링

<br>

## [0️⃣9️⃣ 관리 및 주문 결제](https://www.notion.so/browneyed/44-5285b66d964848faa4dc301417890028?pvs=4)
1. 프로젝트에 Stripe 결제 게이트웨이 통합
2. Stripe를 사용하여 신용카드 결제 처리
3. Stripe 웹훅을 이용한 결제 알림 처리
4. WeasyPrint - 주문을 CSV 파일로 내보내기
5. 관리 사이트에 대한 커스텀 뷰 생성
6. PDF 청구서를 동적으로 생성

<br>

## [1️⃣0️⃣ 상점 확장](https://www.notion.so/browneyed/45-76600626bd674bb58295c0f8b83333ad?pvs=4)

1. 쿠폰 시스템 구축
2. Stripe 결제에 쿠폰 적용
3. Redis를 이용한 추천 엔진 구축

<br>

## [1️⃣1️⃣ 상점 국제화](https://www.notion.so/browneyed/47-f6fcfa9efeba4a46aeea2900993e251c?pvs=4)

1. 프로젝트를 국제화에 맞게 준비하기
2. 번역 파일 관리하기
3. Python 코드 번역하기
4. 템플릿 번역하기
5. Rosetta를 사용하여 번역 관리하기
6. URL 패턴 번역과 URL에 언어 접두사 사용하기
7. 사용자가 언어를 변경할 수 있게 하기
8. django-parler를 사용하여 모델 번역하기
9. ORM과 함께 번역 사용하기
10. 번역을 사용하도록 뷰 수정하기
11. django-localflavor의 로컬라이즈된 폼 필드 사용하기

<br>

## [1️⃣2️⃣ 기타](https://www.notion.so/browneyed/47-f6fcfa9efeba4a46aeea2900993e251c?pvs=4#4a8e4549143a45a998dc2b7e5214b871)
1. 네이버 소셜 로그인
2. 토스 페이먼츠 - 실습 생략

<br>


# 📌 전체 학습 내용 정리
### [📝 Notion - Djanbo by T.I](https://www.notion.so/browneyed/9101324b38654bc38e80100c9b6d87a2?v=9ccf620d3c4e446189106cb9696dc141&pvs=4)
