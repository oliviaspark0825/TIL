README

1) 목표

2) 요구사항

3) 목표 서비스 구현 및 실제 구현정도

4) 데이터베이스 모델링

5) 핵심기능

6) 배포서버 URL

----


1. ##### 목표

   - 영화 추천 서비스 구현
   - HTML/CSS, Javascript(Vue.js/Vanilla JS, etc), Django, Database 등을  활용한 실제 서비스 설계
   - Git을 통한 소스코드 버전 관리 및 협업
   - 서비스 배포

2. ##### 요구사항

   - 영화진흥위원회, TheMovieDB 등 영화 정보 API에서 데이터크롤링을 통해 데이터 파일 생성
   - 

3. ##### 팀원정보 및 분담 내역

   ```
   a. 전영진
   
   - 데이터 크롤링
   - 백엔드
   - 메인페이지 및 영화 정보 기능 구현
   
   b. 박수현
   
   - 모델링
   - 사용자 계정 기능 구현
   ```

   

4. ##### 목표 서비스 구현 및 실제 구현 정도

   사용자가 좋아하는 장르(복수), 감독, 배우 데이터를 저장하여 이를 기반으로 추천 알고리즘 및 기능 구현 성공

    

5. ##### 데이터베이스 모델링

   1) models

   ​	a. movie 

   ![img](https://lh4.googleusercontent.com/nFkPGnTxXFL2pXU3l1jX7aPhJiNbYGpyW8ZfnbWpfde9cli6M5hOfb2WRArK15xSZaZny543rib6bwyPKZ00E--TaXff-Iq40oPFy-S8VAgJsAkX5wG0uXeyL7RNfE2u0DYp1jbR)

   ​	b. account model

   ![img](https://lh3.googleusercontent.com/a2hGup6Bh-o4a8ghIGkLSxLyB3Qs-Tu98didG-TQKlgT8Dk2DsfQQF2TQRcgA5cOfOhb9KUVn5awCp9OaEI4Qru6hQYdWJkvmLbzSne5ARsqzK__0Bw4ZIzTuFmUAtn_VZTvCSiy)

   2) ERD

   ![img](https://lh5.googleusercontent.com/E-aLgKTjiX-lxglhmEGTZxcg4PvuGK57618xGihmVBMmrdoVl_rBGp4kgVTcqNt36SuufNSSspjgiGbl2_1za4wA-0a9rtkLdpJzl0nqT27yRW4Br_tHwh3vDbNdNxa6smWAM31e)

6. ##### 핵심 기능

   1) 좋아하는 영화 장르 저장

   - 회원가입 시 / 개인 정보 수정 시 16개의 장르 중 본인이 선호하는 장르 정보 저장 가능

   2) 사용자 선호도 기반 추천

    -  좋아하는 장르 기준 영화 추천
    -  좋아하는 감독이 제작한 영화 추천
    -  좋아하는 배우 선택

   3) 사용자 평점 기준 영화 추천

   - 필터를 적용하여 리뷰 작성시 7점 이상의  평점을 부여했던 영화리스트 제공

   

   

7. #####  배포 서버 URL

   ```
   http://movie-pjt-dev.ap-northeast-2.elasticbeanstalk.com
   ```

   

8. ##### 느낀점

   모델관계를 명확히 설계해서 그 정보를 기반으로 데이터를 준비해야 수월하다는 것을 느꼈습니다.
