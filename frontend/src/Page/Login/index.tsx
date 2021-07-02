import React from "react";
import { Col, Row, Form, Input, Button, Typography, Checkbox } from "antd";
import styled from "@emotion/styled";
import LoginImage from "../../image/login.jpg";
import SignUpForm from './components/SignUpPage';
import LoginForm from './components/LoginForm'

import moment from "moment";

const { Title, Text } = Typography;

const StyledWrapper = styled('div')`
  background: #e9f9ff;
// background:#F2FAFF;
  position:relative;
  min-height:100vh;


`;

const StyledButton = styled(Button)`
    margin:2em 0;
    background:transparent;
    border-radius:30px;
    color:white;
    width: 150px;
    height: 50px;
    border: 2px solid white;
`
const StyledDiv = styled('div')`
overflow: hidden;
  box-sizing: border-box;
margin:0 auto;
font-size:1vw;
@media only screen and (max-width: 1023px) {
 font-size:10px;
}
`


const LoginPage = (props: any) => {
  const [animation, setAnimation] = React.useState(false);


  const StyledContainer = styled(Row)`
@media only screen and (max-width: 1023px) {
 justify-content:center;
 }
`
  const ShadeLayout = styled('div')`
   position: absolute;
//     background: #1dce78;
   background: #42a7ff;
    z-index: 1000;
    width: 100%;
    left: 0;
    height: 100vh;
    opacity: 0.9;
    top:0;
    display:flex;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    text-align:center;
    padding:0 17vw;
    color:white;

      
     
`
  const StyledFormContainer = styled(Col)`
padding:${animation ? '4em 3em 4em 0px' : '4em 0px 4em 3em'};

@media only screen and (max-width: 1023px) {
  transform:translateX(0%);
   padding:4em 0px 4em 3em;
 };
 @media only screen and (min-width: 1024px) {
  animation: ${animation ? 'slide-in-rights 0.6s linear both' : 'slide-in-lefts 0.6s linear both'};
  @keyframes slide-in-rights {
    0% {
      opacity:0.5;
    }
    100% {
      opacity:1;
      transform:translateX(140%);
    }
  };
  @keyframes slide-in-lefts {
    0% {
      opacity:0.5;
      transform:translateX(140%);
    }
    50%{
    }
    100% {
      opacity:1;
      transform:translateX(0%);
  
    }
 };
z-index:99;

}

`
  const StyledOverlayContainer = styled(Col)`
position:absolute;
right:0;
padding:${animation ? '4em 0px 4em 3em' : '4em 3em 4em 0px'};
min-height:100%;
width:100%;
z-index:100;
left:${animation && '0'};
animation: ${animation ? 'slide-in-right 0.6s linear both' : 'slide-in-left 0.6s linear both'};
@keyframes slide-in-right {
  0% {
            transform: translateX(1000px);
  }
  100% {
            transform: translateX(0);
  }
};
@keyframes slide-in-left {
  0% {
    -webkit-transform: translateX(-1000px);
            transform: translateX(-1000px);
  }
  100% {
    -webkit-transform: translateX(0);
            transform: translateX(0);
  }
}
`
  const StyledImage = styled("img")`
box-shadow:-3px 18px 35px rgba(0,0,0,0.12);
  width: 100%;
  object-fit:cover;
  height: 85vh;
  z-index:15;
`;

  return (

    <StyledDiv>
      <StyledWrapper >
        <StyledContainer>
          <StyledFormContainer xs={23} lg={10}>
            {animation ?
              <SignUpForm setAnimation={setAnimation} animation={animation} /> : <LoginForm setAnimation={setAnimation}  animation={animation} />}
          </StyledFormContainer>
          <StyledOverlayContainer xs={0} lg={14} >
            <ShadeLayout >
              <Title style={{ fontSize: '45px', color: 'white', borderBottom: '1px solid white' }}>WELCOME</Title>
              <Text style={{ fontSize: '15px', color: 'white' }}>We are passionate about our clients' problems and we bring a fierce focus to get the job done right, every time. By sharing our knowledge and understanding our clients' businesses, we deliver the right results for them.</Text>
              <StyledButton size='large' onClick={() => setAnimation(!animation)}>{animation ? 'Log In' : 'Sign Up'}</StyledButton>
            </ShadeLayout>
            <StyledImage src={LoginImage} />
          </StyledOverlayContainer>
        </StyledContainer>
      </StyledWrapper>

    </StyledDiv>
  );
};

export default LoginPage;
