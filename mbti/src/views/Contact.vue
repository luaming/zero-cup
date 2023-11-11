<template>
    <div class="about-us">
      <div class="overlay">
        <h1>关于我们</h1>
        <p>欢迎来到我们的网站！我们是武汉大学计算机学院海底小纵队。</p>
        <p>如您所见，本网站旨在借助创意网页形式，通过互动式的测评和生动的角色例子，来帮助您更深入地理解不同的MBTI性格类型及其潜在影响。</p>
        <p>如果您想了解更多信息，或者想提出批评建议，请联系我们。</p>
        
        <div class="contact-info">
          <h2>联系方式</h2>
          <ul>
            <li>Github项目地址：https://github.com/luaming/zero-cup.git</li>
            <li>邮箱：luaming@whu.edu.com</li>
            <li>地址：武汉大学计算机学院</li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutUs',
  };
  </script>
  
  <style scoped>
  .about-us {
    position: relative;
    background: url('../assets/image/Octonauts1.jpg') no-repeat center center;
    background-size: cover;
    color: #fff; 
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.6);
    height: 100vh;
    font-family: kaishu;
  }
  
  .overlay {
    background-color: rgba(0, 0, 0, 0.5); 
    padding: 50px;
    height: 100%;
    box-sizing: border-box;
  }
  
  .about-us h1 {
    font-size: 3rem;
    text-align: center;
    margin-bottom: 0.5em;
  }
  
  .about-us p {
    font-size: 1.2rem;
    line-height: 1.6;
    margin-bottom: 1em;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .contact-info {
    background: rgba(255, 255, 255, 0.5); 
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
    max-width: 700px;
    margin: 20px auto;
  }
  
  .contact-info h2 {
    text-align: center;
    font-size: 2rem;
  }
  
  .contact-info ul {
    list-style-type: none;
    padding: 0;
    text-align: center;
  }
  
  .contact-info li {
    padding: 10px;
  }
  
  @media (max-width: 768px) {
    .about-us h1 {
      font-size: 2rem;
    }
  
    .contact-info h2 {
      font-size: 1.5rem;
    }
  }
  </style>
  
  