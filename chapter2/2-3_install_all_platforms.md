# Create React App을 사용하여 새로운 React 프로젝트 초기화하기

node 검색해서 깔고 

``` 
node --version
npm --version
```

으로 테스트 해보기

cd ~my-react-app
npm start
로 애플리케이션 확인

# React 프로젝트에 Next.js 설치하기
cd my-react-app
npm install --save next react react-dom (npm audit fix --force 이것도 했음) 

위의 커맨드가 SSR, static site를 생성하는 Next.js에 필요한 종속성을설치할수있는 커맨드

원래꺼는 이거고, 바꾼게 package.json에 들어가있음

// "scripts": {
  //   "start": "react-scripts start",
  //   "build": "react-scripts build",
  //   "test": "react-scripts test",
  //   "eject": "react-scripts eject"
  // },


바꾼것들이 **Next.js 개발 서버를 실행**하고, **애플리케이션의 프로덕션 버전을 빌드**하고, **프로덕션 서버를 시작**하며, 애플리케이션을 **정적 사이트로 내보내는 데 사용**됩니다.

cd pages 

하고 애플리케이션의 진입점이 될 코드 추가

cd my-react-app 하고
npm run dev
