쟝고에서 css, javascript 같은 파일 및 미디어파일을 관리해봅시다.

정적 파일 
- CSS 파일, JavaScript 파일 및 이미지와 같이 애플리케이션 수명 동안 변경되지 않는 파일이 포함됩니다
- 각 애플리케이션 한곳에서 관리 위해서 설정 파일에 STATIC_URL, STATIC_ROOT 및 STATICFILES_DIRS를 설정해야 합니다.

미디어 파일 
- 애플리케이션이 실행 중에 사용자가 업로드하는 파일입니다. 
- 프로필 사진, 업로드된 문서 등이 될 수 있습니다.
- 사용자가 파일을 업로드하면 Django는 MEDIA_ROOT 설정에서 지정한 디렉터리에 파일을 저장합니다. 
- 개발 중에는 MEDIA_URL 설정을 사용하여 파일을 제공하지만, 제품 환경에서는 웹 서버나 클라우드 저장소 서비스에서 처리합니다.


settings.py 에 STATIC ROOT와 MEDIA URL을 추가해
