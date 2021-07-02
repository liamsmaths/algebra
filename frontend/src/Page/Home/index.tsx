import React from "react";
import styled from "@emotion/styled";
import StudentDashboard from "../StudentDashboard";
import HeaderComponent from "../../Components/Header";
import LoginPage from "../Login";

const Wrapper = styled("div")`
  background: #f4f8f9;
  height: 100vh;
  width: 100%;
`;

const Header = styled("div")`
  height: 100px;
  width: 100%;
  background-color: #6d60b0;
  padding: 0px 70px 0px 70px;
`;

const BodyContainer = styled("div")`
  padding: 0px 70px 0px 70px;
`;

const Home = () => {
  return (
    <Wrapper>
      <Header>
        <HeaderComponent />
      </Header>
      <BodyContainer>
        <StudentDashboard />
      </BodyContainer>
    </Wrapper>
    // <React.Fragment>
    //   <LoginPage/>
    // </React.Fragment>
  );
};
export default Home;
