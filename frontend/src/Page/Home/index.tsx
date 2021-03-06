import React from "react";
import styled from "@emotion/styled";
import StudentDashboard from "../StudentDashboard";
import HeaderComponent from "../../Components/Header";

const Wrapper = styled("div")`
  background: #f4f8f9;
  width: 100%;
  height: 100vh;
`;

const Header = styled("div")`
  height: 75px;
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
  );
};
export default Home;
