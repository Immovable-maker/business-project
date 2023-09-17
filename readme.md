(myenv) ➜  full-stack echo $PATH   
/Users/jeonghanko/playground/full-stack/myenv/bin:/Users/jeonghanko/.rbenv/shims:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Users/jeonghanko/.rbenv/shims:/Library/Frameworks/Python.framework/Versions/3.11/bin:/opt/homebrew/bin:/Users/jeonghanko/sdk/flutter/bin:/Users/jeonghanko/.rbenv/bin:/opt/homebrew/bin:/usr/local/bin:/Users/jeonghanko/sdk/flutter/bin:/Users/jeonghanko/.rbenv/bin

(myenv) ➜  full-stack deactivate
➜  full-stack echo $PATH
/Users/jeonghanko/.rbenv/shims:/Library/Frameworks/Python.framework/Versions/3.11/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Users/jeonghanko/.rbenv/shims:/Library/Frameworks/Python.framework/Versions/3.11/bin:/opt/homebrew/bin:/Users/jeonghanko/sdk/flutter/bin:/Users/jeonghanko/.rbenv/bin:/opt/homebrew/bin:/usr/local/bin:/Users/jeonghanko/sdk/flutter/bin:/Users/jeonghanko/.rbenv/bin


맨 위줄에서 bin을 가리키는게 다름 myenv 내부의 bin 이 한줄 추가되었음 activate했을때,
가상 환경을 활성화한 후 pip 명령을 사용하여 패키지를 설치하거나 관리할 때, 해당 가상 환경에 속한 패키지만 영향을 받게 됩니다. 시스템 전체에 영향을 주지 않고 가상 환경 내에서 독립적으로 패키지를 관리할 수 있습니다.

python manage.py runserver

source myenv/bin/activate