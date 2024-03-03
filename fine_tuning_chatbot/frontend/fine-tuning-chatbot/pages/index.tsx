import React, { useState, useEffect } from 'react';

// config.ts
export const BACKEND_URL = 'http://127.0.0.1:8000/';

const Home: React.FC = () => {
  // State to store the data fetched from the backend
  const [data, setData] = useState<any>(null); // 초기값을 null로 설정하고 데이터의 타입을 any로 지정

  // useEffect hook to fetch data from the backend when the component mounts
  useEffect(() => {
    // Fetch data from the backend API using the '/api/hello' endpoint
    fetch(`${BACKEND_URL}api/hello`)
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  // Render the component JSX
  return (
    <div>
      <h1>Welcome to Fine-Tuning Chatbot!</h1>
      <p>{data}</p>
    </div>
  );
};

export default Home;
