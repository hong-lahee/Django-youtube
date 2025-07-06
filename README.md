# Django-youtube

## (1) project settings

- git Hub

## Model의 구조 -> ORM
    
    (1) Users
      - email
      - password
      - nickname
      - is_business
    
    (2) Videos
      - title
      - description
      - link
      - views_count
      - thumbnail
      - video_file: link
      - User: FK
    
    ex) 파일(이미지, 동영상)
    => 장고에 부하가 걸림.
    => S3 Bucket(저렴, 속도가 빠름) -> 결과물: 링크
    
    (3) Reactions
      - User: FK
      - Video: FK
      - reaction (like, dislike, cancel) => 실제 youtube rest api
    
    (4) Comments
      - User: FK
      - Video: FK
      - content
      - like
      - dislike
    
    (5) Subscriptions
      - User: FK => subscriber (내가 구독한 사람)
      - User: FK => subscribed_to (나를 구독한 사람)
    
    (6) Common
      - created_at
      - updated_at
