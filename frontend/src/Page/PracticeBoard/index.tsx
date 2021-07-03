import React, { useEffect, useState } from "react";
import styled from "@emotion/styled";
import HeaderComponent from "../../Components/Header";
import { useLocation } from "react-router-dom";
import axios from "axios";
import Text from "antd/lib/typography/Text";
import MathJax from "react-mathjax";

const Header = styled("div")`
  height: 100px;
  width: 100%;
  background-color: #6d60b0;
  padding: 0px 70px 0px 70px;
`;
const Wrapper = styled("div")`
  background: #f4f8f9;
  height: 100vh;
  width: 100%;
`;

const BodyContainer = styled("div")`
  padding: 0px 70px 0px 70px;
`;

const PracticeContainer = styled("div")`
  padding-top: 40px;
  display: flex;
  justify-content: space-between;
`;

const QuestionContainer = styled("div")`
  height: 380px;
  width: 450px;
  border: 1px solid black;
  padding: 10px 0px 0px 18px;
`;

const InstructionContainer = styled("div")`
  height: 380px;
  width: 450px;
  border: 1px solid black;
`;

const PracticeBoard = () => {
  const location: any = useLocation();
  const id = location.state.id;
  const [allQuestions, setAllQuestions] = useState<any>();

  const fetchAllQuestions = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/getQuestion/${id}`);
      console.log(response);
      setAllQuestions(response);
    } catch (e) {}
  };

  useEffect(() => {
    fetchAllQuestions();
  }, []);
  return (
    <Wrapper>
      <MathJax.Provider>
        <Header>
          <HeaderComponent />
        </Header>
        <BodyContainer>
          <PracticeContainer>
            <QuestionContainer>
              <MathJax.Node
                inline
                formula={allQuestions && allQuestions.data && allQuestions.data.title}
              />
            </QuestionContainer>
            <InstructionContainer></InstructionContainer>
          </PracticeContainer>
        </BodyContainer>
      </MathJax.Provider>
    </Wrapper>
  );
};

export default PracticeBoard;
