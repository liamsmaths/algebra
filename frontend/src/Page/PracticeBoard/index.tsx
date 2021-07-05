import React, { useEffect, useState } from "react";
import styled from "@emotion/styled";
import HeaderComponent from "../../Components/Header";
import { useLocation } from "react-router-dom";
import axios from "axios";
import Text from "antd/lib/typography/Text";
import MathJax from "react-mathjax";
import { Input, Button, Row, Col, Divider } from "antd";
const { TextArea } = Input;

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
  padding: 70px 70px 0px 70px;
`;

const PracticeContainer = styled("div")`
  padding-top: 40px;
  display: flex;
  justify-content: space-between;
`;

const QuestionContainer = styled("div")`
  padding: 18px 18px 18px 18px;
  box-shadow: 0 4px 6px rgb(0 0 0 / 10%), 0 1px 3px rgb(0 0 0 / 10%);
  background-color: #fff;
  border-radius: 4px;
`;

const InstructionContainer = styled("div")`
  padding: 10px 0px 0px 18px;
  box-shadow: 0 4px 6px rgb(0 0 0 / 10%), 0 1px 3px rgb(0 0 0 / 10%);
  background-color: #fff;
  border-radius: 4px;
`;

const StyledButton = styled(Button)`
  background: #6d60b0;
  color: white;
  border-radius: 5px;
  height: 40px;
  &:hover,
  &:focus {
    background: #6d60b0;
    color: white;
  }
  border: none;
`;

const PracticeBoard = () => {
  const location: any = useLocation();
  const id = location.state.id;
  const name = location.state.name;
  const [allQuestions, setAllQuestions] = useState<any>();
  const [isDisabled, setIsDisabled] = useState<boolean>(true);
  const [inputAnswer, setInputAnswer] = useState("");
  const [correct, setCorrect] = useState<number>(0);
  const [totalAttempts, setTotalAttempts] = useState<number>(0);

  const fetchAllQuestions = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/getQuestion/${id}`);
      setAllQuestions(response);
    } catch (e) {}
  };

  useEffect(() => {
    fetchAllQuestions();
  }, []);

  const handleChange = (e: any) => {
    const inputValue = e.target.value;
    setInputAnswer(inputValue);
    if (inputValue.length >= 6) {
      setIsDisabled(false);
    }
    if (inputValue.length < 6) {
      setIsDisabled(true);
    }
  };

  const handleCheckAnswer = () => {
    setTotalAttempts(totalAttempts + 1);
    const inputAnswerStringify = inputAnswer.toString();
    const correctAnswerStringify = allQuestions.data.answer.toString();

    if (inputAnswerStringify === correctAnswerStringify) {
      setCorrect(correct + 1);
    }
  };

  const handleNextQuestion = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/getQuestion/${id}`);
      setAllQuestions(response);
    } catch (e) {}
  };
  return (
    <Wrapper>
      <MathJax.Provider>
        <Header>
          <HeaderComponent />
        </Header>
        <BodyContainer>
          <Row gutter={64}>
            <Col span={16}>
              <QuestionContainer>
                <Text style={{ fontSize: "20px", fontWeight: 600, paddingRight: "10px" }}>
                  {name} :
                </Text>

                <Text style={{ fontSize: "18px" }}>
                  <MathJax.Node
                    inline
                    formula={allQuestions && allQuestions.data && allQuestions.data.title}
                  />
                </Text>

                <Divider orientation="left">Answer</Divider>
                <Row gutter={64}>
                  <Col xs={24} sm={24} md={10}>
                    <TextArea rows={4} onChange={handleChange} />
                  </Col>
                  <Col xs={24} sm={24} md={7}>
                    <div style={{ display: "flex", flexDirection: "column", gap: "5px" }}>
                      <Text style={{ fontSize: "18px", fontWeight: 600 }}>Correct</Text>
                      <Text style={{ fontSize: "18px", fontWeight: 600 }}>{correct}</Text>
                    </div>
                  </Col>
                  <Col xs={24} sm={24} md={7}>
                    <div style={{ display: "flex", flexDirection: "column", gap: "5px" }}>
                      <Text style={{ fontSize: "18px", fontWeight: 600 }}>Total Attempts</Text>
                      <Text style={{ fontSize: "18px", fontWeight: 600 }}>{totalAttempts}</Text>
                    </div>
                  </Col>
                </Row>
                <Row gutter={12} style={{ marginTop: "12px", paddingTop: "15px" }}>
                  <Col xs={24} sm={3}>
                    <StyledButton disabled={isDisabled}>Get Help</StyledButton>
                  </Col>
                  <Col xs={15} sm={4}>
                    <StyledButton disabled={isDisabled} onClick={handleCheckAnswer}>
                      Check Answer
                    </StyledButton>
                  </Col>
                  <Col xs={24} sm={3}>
                    <StyledButton onClick={handleNextQuestion}>Next Question</StyledButton>
                  </Col>
                </Row>
              </QuestionContainer>
            </Col>
            <Col span={8}>
              <InstructionContainer></InstructionContainer>
            </Col>
          </Row>
        </BodyContainer>
      </MathJax.Provider>
    </Wrapper>
  );
};

export default PracticeBoard;
